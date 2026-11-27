"""Shared library for the Digital Product Planning Framework scripts.

Standard library only. MIT licensed (see LICENSE). Not meant to be run directly;
use the wrappers in this directory (validate-metadata, check-links, ...).
"""
import json
import os
import re
import sys

REQUIRED = ["id", "title", "domain", "tier", "status", "version", "owner", "last_updated", "depends_on", "feeds"]
TIERS = {"mandatory", "recommended", "optional", "package"}
STATUSES = {"draft", "in-review", "approved", "superseded", "archived", "not-applicable"}
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)


# ---------------------------------------------------------------- parsing
def parse_frontmatter(text):
    """Parse the flat YAML subset used by the framework. Returns dict or None."""
    m = FM_RE.match(text)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#") or line.startswith(" "):
            continue
        k, _, v = line.partition(":")
        v = re.sub(r"\s+#.*$", "", v.strip())
        if v.startswith("[") and v.endswith("]"):
            fm[k.strip()] = [x.strip().strip("\"'") for x in v[1:-1].split(",") if x.strip()]
        else:
            fm[k.strip()] = v.strip("\"'")
    return fm


def iter_markdown(root, subdirs=None):
    """Yield (path, relpath) for every .md file under root (or the given subdirs)."""
    bases = [os.path.join(root, s) for s in subdirs] if subdirs else [root]
    for base in bases:
        for dp, dn, fs in os.walk(base):
            dn[:] = sorted(d for d in dn if not d.startswith(".") and d not in ("node_modules",))
            for f in sorted(fs):
                if f.endswith(".md"):
                    p = os.path.join(dp, f)
                    yield p, os.path.relpath(p, root)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def load_profiles():
    return json.loads(read(os.path.join(SCRIPT_DIR, "profiles.json")))


def framework_root():
    return os.path.dirname(SCRIPT_DIR)


# ---------------------------------------------------------------- reporting
class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, where, msg):
        self.errors.append(f"ERROR   {where}: {msg}")

    def warn(self, where, msg):
        self.warnings.append(f"warning {where}: {msg}")

    def finish(self, name, strict=False):
        for line in self.errors + self.warnings:
            print(line)
        print(f"{name}: {len(self.errors)} error(s), {len(self.warnings)} warning(s)")
        failed = bool(self.errors) or (strict and bool(self.warnings))
        return 1 if failed else 0


# ---------------------------------------------------------------- metadata
def validate_metadata(root, report, doc_dirs=None, known_stems=None):
    docs = {}
    for path, rel in iter_markdown(root, doc_dirs):
        fm = parse_frontmatter(read(path))
        if fm is None:
            continue
        if "tier" not in fm and "domain" not in fm:
            continue  # not a framework document (README, guides, ...)
        docs[rel] = (fm, read(path))
    stems = {os.path.basename(r)[:-3] for r in docs}
    stems |= {"project-manifest"}
    ids = {}
    for rel, (fm, text) in sorted(docs.items()):
        for k in REQUIRED:
            if k not in fm:
                report.error(rel, f"missing frontmatter field '{k}'")
        if fm.get("tier") and fm["tier"] not in TIERS:
            report.error(rel, f"invalid tier '{fm['tier']}'")
        if fm.get("status") and fm["status"] not in STATUSES:
            report.error(rel, f"invalid status '{fm['status']}'")
        if fm.get("version") and not re.fullmatch(r"\d+\.\d+\.\d+", fm["version"]):
            report.error(rel, f"version '{fm['version']}' is not major.minor.patch")
        if "id" in fm:
            if fm["id"] in ids:
                report.error(rel, f"duplicate id '{fm['id']}' (also {ids[fm['id']]})")
            ids[fm["id"]] = rel
        for key in ("depends_on", "feeds"):
            v = fm.get(key, [])
            if not isinstance(v, list):
                report.error(rel, f"'{key}' must be a list")
                continue
            for s in v:
                if s not in stems and not (known_stems and s in known_stems):
                    report.error(rel, f"{key} references unknown document '{s}'")
        stem = os.path.basename(rel)[:-3]
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", stem) and not re.fullmatch(r"adr-\d{4}-[a-z0-9-]+", stem):
            report.warn(rel, "file name is not kebab-case")
        if "Completion Criteria" not in text and fm.get("tier") in ("mandatory", "recommended", "optional", "package"):
            report.warn(rel, "no 'Completion Criteria' section")
        if fm.get("status") == "approved":
            if re.search(r"YYYY-MM-DD", text):
                report.warn(rel, "approved document still contains 'YYYY-MM-DD' placeholder")
            if re.search(r"\b[A-Z]{2,5}-(xx|0x|00x)\b", text):
                report.warn(rel, "approved document still contains placeholder ids (e.g. RISK-xx)")
    return docs


# ---------------------------------------------------------------- links
LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE_RE = re.compile(r"^```.*?^```", re.S | re.M)


def check_links(root, report, template_stems=None, report_unselected=False):
    for path, rel in iter_markdown(root):
        text = FENCE_RE.sub("", read(path))
        for target in LINK_RE.findall(text):
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            t = target.split("#")[0]
            if not t:
                continue
            full = os.path.normpath(os.path.join(os.path.dirname(path), t))
            if not os.path.exists(full):
                stem = os.path.basename(t)
                stem = stem[:-3] if stem.endswith(".md") else stem
                if template_stems and stem in template_stems:
                    if report_unselected:
                        report.warn(rel, f"link to framework document not in this project: {target}")
                else:
                    report.error(rel, f"broken link: {target}")


# ---------------------------------------------------------------- guidance stripping
def strip_guidance(text, examples=False):
    text = re.sub(r"<details>\s*<summary><strong>About this template</strong>.*?</details>\n*", "", text, flags=re.S)
    out, skipping = [], False
    for line in text.split("\n"):
        is_guid = line.startswith("> **Guidance")
        is_ex = examples and re.match(r"^> \*Example", line)
        if is_guid or is_ex:
            skipping = True
            continue
        if skipping and line.startswith(">"):
            continue
        if skipping and line.strip() == "":
            skipping = False
            # drop one blank line that followed the removed block
            if out and out[-1].strip() == "":
                continue
        skipping = False if not line.startswith(">") else skipping
        out.append(line)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))


# ---------------------------------------------------------------- traceability
ID_RE = re.compile(r"\b(GOAL|MET|PER|ASM|CON|DEP|FR|US|UC|BR|NFR|ADR|RISK|DEC|Q|TS|TC|EVT|MON|SR|TH|PD|CMP|EX|UAT|API|INT|UF|PR|F|C)-(\d{1,4}(?:\.\d+)?)\b")
DEF_ROW_RE = re.compile(r"^\|\s*(?:\*\*)?([A-Z]{1,5}-\d{1,4}(?:\.\d+)?)(?:\*\*)?\s*\|")
DEF_HEAD_RE = re.compile(r"^#{2,6}\s+([A-Z]{1,5}-\d{1,4}(?:\.\d+)?)\b")
RANGE_RE = re.compile(r"\b([A-Z]{1,5})-(\d{1,4})\s*[–-]\s*(?:\1-)?(\d{1,4})\b")


CANONICAL = {
    "GOAL": ["goals-and-metrics"], "MET": ["goals-and-metrics"], "PER": ["persona", "prd"],
    "ASM": ["assumption-map", "prd"], "CON": ["prd", "project-charter"], "FR": ["prd"],
    "US": ["user-stories"], "AC": ["user-stories"], "UC": ["use-cases"], "BR": ["business-rules"],
    "NFR": ["non-functional-requirements"], "ADR": ["adr", "architecture-overview"], "RISK": ["risk-register"],
    "DEP": ["prd", "project-charter"], "Q": ["prd", "decision-log"], "DEC": ["decision-log"],
    "TS": ["test-scenarios"], "TC": ["test-case"], "EVT": ["event-tracking-plan"], "MON": ["observability-strategy"],
    "SR": ["security-requirements"], "EX": ["security-requirements"], "TH": ["threat-model"],
    "PD": ["privacy-requirements"], "CMP": ["compliance-assessment"], "UAT": ["uat-plan"],
    "API": ["api-specification"], "INT": ["integration-specification", "enterprise-integration"],
    "UF": ["user-flow"], "S": ["information-architecture", "wireframe-spec"], "I": ["information-architecture"],
    "M": ["wireframe-spec"], "PR": ["prototype-review"], "F": ["user-research"], "C": ["mvp-and-prioritization"],
    "N": ["push-notifications"],
}


def _stem(rel):
    b = os.path.basename(rel)[:-3]
    return "adr" if re.fullmatch(r"adr-\d{4}-.+", b) else b


def check_traceability(root, report, subdirs=None):
    """Definitions count only in an ID's canonical document (the first listed one that exists in the project)."""
    raw_defs = {}  # id -> set(rel)
    refs = {}
    texts = {}
    for path, rel in iter_markdown(root, subdirs):
        t = read(path)
        fm = parse_frontmatter(t)
        if not fm or "tier" not in fm:
            continue
        body = FM_RE.sub("", t, count=1)
        body = re.sub(r"<details>.*?</details>", "", body, flags=re.S)
        texts[rel] = body
        for line in body.split("\n"):
            m = DEF_ROW_RE.match(line) or DEF_HEAD_RE.match(line)
            if m:
                raw_defs.setdefault(m.group(1), set()).add(rel)
        for m in ID_RE.finditer(body):
            refs.setdefault(f"{m.group(1)}-{m.group(2)}", set()).add(rel)
        for m in RANGE_RE.finditer(body):
            a, b = int(m.group(2)), int(m.group(3))
            if 0 < b - a < 50:
                width = len(m.group(2))
                for n in range(a, b + 1):
                    refs.setdefault(f"{m.group(1)}-{n:0{width}d}", set()).add(rel)
    present = {_stem(r) for r in texts}
    chosen = {}
    for prefix, cands in CANONICAL.items():
        existing = [c for c in cands if c in present]
        chosen[prefix] = set(existing[:1]) if existing else None
    defs = {}
    for i, files in raw_defs.items():
        prefix = i.split("-")[0]
        allowed = chosen.get(prefix)
        if allowed is None:      # unknown prefix, or canonical document absent: accept any
            keep = set(files)
        else:
            keep = {f for f in files if _stem(f) in allowed}
            if prefix == "ADR":
                keep = {f for f in files if _stem(f) in ("adr", "architecture-overview")} or keep
        if keep:
            defs[i] = keep
    for i, files in sorted(defs.items()):
        if len(files) > 1 and not (i.startswith("ADR-") and all(_stem(f) in ("adr", "architecture-overview") for f in files)):
            report.error(", ".join(sorted(files)), f"id {i} is defined in more than one document")
    for i, files in sorted(refs.items()):
        if i not in defs:
            report.warn(", ".join(sorted(files)), f"{i} is referenced but not defined in its canonical document")

    # coverage rules
    prd = next((t for r, t in texts.items() if r.endswith("prd.md")), "")
    stories = "\n".join(t for r, t in texts.items() if r.endswith("user-stories.md"))
    tests = "\n".join(t for r, t in texts.items() if "07-quality" in r)
    must_frs = []
    for line in prd.split("\n"):
        m = DEF_ROW_RE.match(line)
        if m and m.group(1).startswith("FR-") and re.search(r"\|\s*Must\s*\|", line):
            must_frs.append(m.group(1))
    for fr in must_frs:
        if not re.search(r"^\|.*\b" + re.escape(fr) + r"\b.*\|", stories, re.M):
            report.error("user-stories", f"Must requirement {fr} has no user story")
    story_ids = [i for i in defs if i.startswith("US-")]
    for us in story_ids:
        num = us.split("-")[1]
        if not re.search(r"\bAC-" + re.escape(num) + r"\.\d+\b", stories):
            report.error("user-stories", f"{us} has no acceptance criteria")
    for ac in sorted(i for i in defs if i.startswith("AC-")):
        num = ac.split("-")[1].split(".")[0]
        direct = re.search(r"\b" + re.escape(ac) + r"\b", tests)
        ranged = re.search(r"\bAC-" + num + r"\.\d+\s*[–-]\s*AC-" + num + r"\.(\d+)\b", tests)
        if not direct and not (ranged and int(ac.split(".")[1]) <= int(ranged.group(1))):
            report.warn("07-quality", f"{ac} is not referenced by any test scenario")
    for nfr in sorted(i for i in defs if i.startswith("NFR-")):
        if not re.search(r"\b" + re.escape(nfr) + r"\b", tests) and not re.search(r"\bMON-\d+", "\n".join(
                t for r, t in texts.items() if "observability" in r)):
            report.warn("nfr", f"{nfr} is not verified by a test scenario or monitoring rule")
    return defs, refs


# ---------------------------------------------------------------- catalog / document map
def collect_catalog(fw_root):
    rows = []
    for base in ("templates", "packages"):
        for path, rel in iter_markdown(fw_root, [base]):
            fm = parse_frontmatter(read(path))
            if not fm:
                continue
            fm["_rel"] = rel.replace(os.sep, "/")
            fm["_stem"] = os.path.basename(rel)[:-3]
            rows.append(fm)
    return rows


DOMAIN_NAMES = {
    "00-foundation": "00 Foundation", "01-discovery": "01 Product Discovery", "02-strategy": "02 Product Strategy",
    "03-requirements": "03 Requirements Engineering", "04-ux-ui": "04 UX/UI Design", "05-architecture": "05 System Architecture",
    "06-project-mgmt": "06 Project Management", "07-quality": "07 Quality Assurance", "08-security": "08 Security and Compliance",
    "09-release-ops": "09 Release and Operations", "10-analytics": "10 Product Analytics",
}


def render_catalog(rows):
    out = ["## 5. Catalog\n"]
    by = {}
    for r in rows:
        by.setdefault(r["domain"], []).append(r)
    for d in sorted(k for k in by if k[0].isdigit()):
        out.append(f"\n### {DOMAIN_NAMES[d]}\n\n| Document | Tier | Owner | Depends on |\n|---|---|---|---|\n")
        for r in by[d]:
            dep = ", ".join(r.get("depends_on", [])) or "—"
            out.append(f"| [{r['title']}](../{r['_rel']}) | {r['tier']} | {r['owner']} | {dep} |\n")
    out.append("\n### Product-Specific Packages\n\n| Document | Applies to | Owner | Depends on |\n|---|---|---|---|\n")
    for r in rows:
        if r["tier"] == "package":
            out.append(f"| [{r['title']}](../{r['_rel']}) | {', '.join(r.get('applies_to', []))} | {r['owner']} | {', '.join(r.get('depends_on', []))} |\n")
    out.append("\n*Also in `00-foundation`: [project-manifest.yaml](../templates/00-foundation/project-manifest.yaml), the register of which documents your project uses.*\n")
    return "".join(out)


def update_document_map(fw_root, check_only=False):
    rows = collect_catalog(fw_root)
    path = os.path.join(fw_root, "guides", "document-map.md")
    text = read(path)
    head, sep, _ = text.partition("## 5. Catalog")
    if not sep:
        raise SystemExit("document-map.md has no '## 5. Catalog' heading")
    counts = {t: sum(1 for r in rows if r["tier"] == t) for t in ("mandatory", "recommended", "optional", "package")}
    for t, label in (("mandatory", "Mandatory"), ("recommended", "Recommended"), ("optional", "Optional"), ("package", "Package")):
        head = re.sub(r"(\| \*\*%s\*\* \|.*?\| )\d+( \|)" % label, lambda m: f"{m.group(1)}{counts[t]}{m.group(2)}", head)
    new = head + render_catalog(rows)
    if check_only:
        return new == text
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(new)
    return True


# ---------------------------------------------------------------- scaffold
TYPE_TO_PACKAGE = {
    "saas": "saas", "mobile": "mobile", "api-platform": "api-platform", "api": "api-platform",
    "enterprise": "enterprise", "internal": "enterprise", "developer-tools": "developer-tools", "web": None, "other": None,
}
UI_PROTOTYPE_ASSET = "04-ux-ui/ui-prototype.html"


def select_documents(fw_root, profile, packages):
    profiles = load_profiles()
    if profile not in profiles:
        raise SystemExit(f"unknown profile '{profile}'. Choose from: {', '.join(profiles)}")
    spec = profiles[profile]
    rows = collect_catalog(fw_root)
    chosen = []
    for r in rows:
        if r["tier"] == "package":
            pkg = r["_rel"].split("/")[1]
            if pkg in packages:
                chosen.append(r)
            continue
        stem = r["_stem"]
        if stem in spec.get("include", []) or r["tier"] in spec.get("tiers", []) or stem in spec.get("extra", []):
            chosen.append(r)
    # solo profile may add 'when applicable' documents on request through --also
    return chosen


def rewrite_links(text, rel, framework_url):
    parts = rel.split("/")
    if parts[0] == "templates":
        text = text.replace("](../../packages/", "](../packages/")
        text = text.replace("](../../guides/", "](" + framework_url + "guides/")
        text = text.replace("](../../GLOSSARY.md", "](" + framework_url + "GLOSSARY.md")
    elif parts[0] == "packages":
        text = text.replace("](../../templates/", "](../../")
    return text


def scaffold(fw_root, out, profile, packages, strip=False, examples=False, framework_url="", also=()):
    chosen = select_documents(fw_root, profile, packages)
    stems_wanted = {r["_stem"] for r in chosen}
    for r in collect_catalog(fw_root):
        if r["_stem"] in also and r["_stem"] not in stems_wanted:
            chosen.append(r)
    count = 0
    for r in chosen:
        src = os.path.join(fw_root, r["_rel"])
        parts = r["_rel"].split("/")
        dst = os.path.join(out, *parts[1:]) if parts[0] == "templates" else os.path.join(out, *parts)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        text = rewrite_links(read(src), r["_rel"], framework_url)
        if strip:
            text = strip_guidance(text, examples)
        with open(dst, "w", encoding="utf-8") as fh:
            fh.write(text)
        count += 1
    if any(r["_stem"] == "ui-design" for r in chosen):
        src = os.path.join(fw_root, "templates", UI_PROTOTYPE_ASSET)
        dst = os.path.join(out, UI_PROTOTYPE_ASSET)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(src, encoding="utf-8") as fh:
            prototype = fh.read()
        with open(dst, "w", encoding="utf-8") as fh:
            fh.write(prototype)
    # manifest
    man_src = os.path.join(fw_root, "templates", "00-foundation", "project-manifest.yaml")
    man_dst = os.path.join(out, "00-foundation", "project-manifest.yaml")
    os.makedirs(os.path.dirname(man_dst), exist_ok=True)
    m = read(man_src)
    m = re.sub(r"profile: \w+", f"profile: {profile}", m, count=1)
    m = re.sub(r"packages:\n(?:  .*\n)+", "packages:\n" + "".join(f"  - {p}\n" for p in sorted(packages)) if packages else "packages: []\n", m, count=1)
    docs = "documents:\n" + "".join(
        f"  - {{ doc: {r['_stem']}, status: not-started }}\n" for r in sorted(chosen, key=lambda x: x["_rel"]) if r["tier"] != "package")
    m = re.sub(r"documents:\n(?:  .*\n|\s*#.*\n)+", docs, m, count=1)
    with open(man_dst, "w", encoding="utf-8") as fh:
        fh.write(m)
    return count
