"""Validate AJC package metadata and local instruction links (no network calls)."""
import json
import re
from pathlib import Path

import yaml

root = Path(__file__).resolve().parents[1]
plugin_root = root / "plugins/ajc"
skill_root = plugin_root / "skills/ajc"
plugin = json.loads((plugin_root / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
marketplace = json.loads((root / ".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
ui = yaml.safe_load((skill_root / "agents/openai.yaml").read_text(encoding="utf-8"))
cases = json.loads((root / "tests/技能路由测试场景.json").read_text(encoding="utf-8"))

assert (plugin_root / plugin["skills"]).is_dir(), "Plugin skill directory is missing"
assert (root / marketplace["plugins"][0]["source"]["path"]).resolve() == plugin_root.resolve()
assert ui["policy"]["allow_implicit_invocation"] is True
assert "$ajc" in ui["interface"]["default_prompt"]
assert 25 <= len(ui["interface"]["short_description"]) <= 64

catalog_ids = {entry["id"] for entry in cases["catalog"]}
assert len(catalog_ids) == len(cases["catalog"]), "Duplicate fixture skill ids"
case_ids = set()
for case in cases["cases"]:
    assert case["id"] not in case_ids, "Duplicate scenario ids"
    case_ids.add(case["id"])
    assert set(case["available"]) <= catalog_ids, "Unknown fixture skill"

# Validate maintained entrypoints and references without changing original-source files.
documents = [root / "README.md", skill_root / "SKILL.md", *sorted((skill_root / "references").glob("*.md"))]
links = 0
for document in documents:
    content = document.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
            continue
        target = target.split("#", 1)[0]
        assert (document.parent / target).exists(), f"Broken link in {document.name}: {target}"
        links += 1

print(f"Package metadata valid; {links} local links resolve; {len(case_ids)} routing scenarios have valid inputs.")
