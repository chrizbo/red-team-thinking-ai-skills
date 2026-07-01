# Editing a skill

Each skill has exactly one file you should hand-edit: `skills/<slug>/SKILL.md`. Everything else — `gemini/commands/<slug>.toml`, `copilot/prompts/<slug>.prompt.md`, `prompts/<slug>.md` — is generated from it and gets overwritten the next time the build script runs. Don't edit those directly; the edit will be lost.

## Workflow

1. Edit `skills/<slug>/SKILL.md` (frontmatter `description` and/or the markdown body).
2. From the repo root, run:
   ```
   python3 scripts/build_variants.py
   ```
   This regenerates the Gemini, Copilot, and plain-prompt files for every skill under `skills/`.
3. Run `git diff` and confirm only the expected files changed.
4. Commit the `SKILL.md` change together with the regenerated files in the same commit.

## Adding a new skill

1. `mkdir skills/<new-slug>`
2. Create `skills/<new-slug>/SKILL.md` with frontmatter containing only `name` and `description` — that's the portable subset Claude, Codex CLI, and Gemini CLI extensions all read. Adding other frontmatter fields (e.g. Claude-only `allowed-tools`) will still work in Claude but gets dropped when generating the other formats.
3. Run `python3 scripts/build_variants.py` — it auto-discovers every folder under `skills/` with a `SKILL.md`, so the new skill's variants are created automatically.
4. Add a row for the new skill to the table in `README.md`.

## Writing the description field

The `description` is the only thing an agent sees before deciding to use the skill — it must state both **what** the skill does and **when** to use it (trigger phrases, situations). Keep the markdown body to imperative, numbered steps; avoid restating the "when to use" framing there since it isn't loaded until the skill has already been triggered.
