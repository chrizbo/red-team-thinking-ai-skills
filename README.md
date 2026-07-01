# Red Team Thinking + AI Skills

AI-paired critical-thinking skills built for the **Red Team Thinking in the Age of AI** course. Each skill takes a Red Team Thinking technique and adapts it specifically for working with an AI: either using AI to red team a plan (Day 1), or turning that same discipline back on the AI's own output (Day 2).

These are original instructional adaptations for AI use, not reproductions of the Red Team Thinking / TruThinking Corp workbooks. Technique names carry their original trademarks; the step-by-step instructions here were written from scratch for this course.

## Skills

| Skill | Use it to... |
| --- | --- |
| [`assumptions-challenge-ai`](skills/assumptions-challenge-ai/SKILL.md) | Surface a plan's stated and unstated assumptions, then interrogate them — including ones the AI introduced itself. |
| [`ai-as-provocateur`](skills/ai-as-provocateur/SKILL.md) | Run a panel of harsh adversarial personas against a plan for blunt, no-holds-barred pushback. |
| [`argument-dissection-ai`](skills/argument-dissection-ai/SKILL.md) | Dissect an AI's own answer for hallucination, false confidence, sycophancy, and framing bias. |
| [`four-ways-of-seeing-ai`](skills/four-ways-of-seeing-ai/SKILL.md) | Compare how you framed a question against how the AI implicitly reframed it. |
| [`devils-advocacy-ai`](skills/devils-advocacy-ai/SKILL.md) | Force an AI to build the strongest case against its own recommendation. |

## Repo layout

```
skills/<slug>/SKILL.md      canonical source — Claude, Codex CLI, Gemini CLI extensions read this format natively
gemini/commands/<slug>.toml generated — Gemini CLI custom slash command
copilot/prompts/<slug>.prompt.md generated — GitHub Copilot Chat/CLI prompt file
prompts/<slug>.md           generated — plain text for Gemini Gems or pasting into any chat model
scripts/build_variants.py   regenerates the three generated formats from skills/*/SKILL.md
```

Edit `skills/<slug>/SKILL.md`, then run `python3 scripts/build_variants.py` to regenerate everything else. Don't hand-edit the generated files — they'll be overwritten. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full editing workflow.

## Getting and installing the skills

See [INSTALL.md](INSTALL.md) for copy-paste steps to get this repo and install the skills into Claude Code/Desktop, Codex CLI, Gemini CLI, GitHub Copilot, or Gemini Gems/any other chat tool.

## Course context

Built for the two-day **Red Team Thinking in the Age of AI** intensive (Bryce Hoffman, Chris Butler, Scott Henderson). Day 1 pairs AI with Red Team Thinking to stress-test human plans; Day 2 inverts the discipline to stress-test the AI's own output.
