#!/usr/bin/env python3
"""Generate per-platform variants from the canonical skills/<slug>/SKILL.md files.

Canonical source: skills/<slug>/SKILL.md (Claude, Codex CLI, Gemini CLI
extensions — all read this format natively).

Generated:
  gemini/commands/<slug>.toml   - Gemini CLI custom slash command
  copilot/prompts/<slug>.prompt.md - GitHub Copilot Chat/CLI prompt file
  prompts/<slug>.md             - plain-text version for Gemini Gems or
                                   pasting into any chat model

Run from the repo root: python3 scripts/build_variants.py
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
GEMINI_DIR = ROOT / "gemini" / "commands"
COPILOT_DIR = ROOT / "copilot" / "prompts"
PROMPTS_DIR = ROOT / "prompts"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


def parse_skill_md(text: str) -> tuple[dict, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("SKILL.md missing YAML frontmatter block")
    frontmatter_block, body = match.groups()
    fields = {}
    for line in frontmatter_block.splitlines():
        if not line.strip():
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields, body.strip() + "\n"


def yaml_dquote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def write_gemini_toml(slug: str, description: str, body: str) -> None:
    GEMINI_DIR.mkdir(parents=True, exist_ok=True)
    content = (
        f"# Generated from skills/{slug}/SKILL.md — edit the canonical file, not this one.\n"
        f"description = '''{description}'''\n\n"
        f"prompt = '''\n{body}'''\n"
    )
    (GEMINI_DIR / f"{slug}.toml").write_text(content)


def write_copilot_prompt(slug: str, description: str, body: str) -> None:
    COPILOT_DIR.mkdir(parents=True, exist_ok=True)
    content = (
        "---\n"
        f"description: {yaml_dquote(description)}\n"
        "---\n\n"
        f"<!-- Generated from skills/{slug}/SKILL.md — edit the canonical file, not this one. -->\n\n"
        f"{body}"
    )
    (COPILOT_DIR / f"{slug}.prompt.md").write_text(content)


def write_plain_prompt(slug: str, description: str, body: str) -> None:
    PROMPTS_DIR.mkdir(parents=True, exist_ok=True)
    content = (
        f"{description}\n\n"
        "---\n\n"
        f"{body}"
    )
    (PROMPTS_DIR / f"{slug}.md").write_text(content)


def main() -> None:
    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if (p / "SKILL.md").exists())
    if not skill_dirs:
        raise SystemExit(f"No skills found under {SKILLS_DIR}")

    for skill_dir in skill_dirs:
        slug = skill_dir.name
        fields, body = parse_skill_md((skill_dir / "SKILL.md").read_text())
        description = fields.get("description", "")
        write_gemini_toml(slug, description, body)
        write_copilot_prompt(slug, description, body)
        write_plain_prompt(slug, description, body)
        print(f"[OK] generated variants for {slug}")


if __name__ == "__main__":
    main()
