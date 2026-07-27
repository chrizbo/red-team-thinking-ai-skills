# Red Team Thinking + AI Skills

AI-paired critical-thinking skills built for the **Red Team Thinking in the Age of AI** course. Each skill takes a Red Team Thinking technique and adapts it specifically for using AI to red team a human plan.

These are original instructional adaptations for AI use, not reproductions of the Red Team Thinking / TruThinking Corp workbooks. Technique names carry their original trademarks; the step-by-step instructions here were written from scratch for this course.

## Skills

| Skill | Use it to... |
| --- | --- |
| [`assumptions-challenge`](skills/assumptions-challenge/SKILL.md) | Surface a plan's stated and unstated assumptions, then interrogate them — including ones the AI introduced itself. |
| [`provocateur`](skills/provocateur/SKILL.md) | Run a panel of harsh adversarial personas against a plan for blunt, no-holds-barred pushback. |
| [`socratic-partner`](skills/socratic-partner/SKILL.md) | Spar live with an AI that defends a critique of your plan and interrogates whatever you push back with. |
| [`no-rubber-stamp`](skills/no-rubber-stamp/SKILL.md) | Mark up pasted AI output inline for the seven spots where a machine is prone to fail, plus a ranked chat summary. |

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

See [INSTALL.md](INSTALL.md) for copy-paste steps to get this repo and install the skills into Claude Code/Desktop, Codex CLI, Gemini CLI, GitHub Copilot, Microsoft 365 Copilot, or Gemini Gems/any other chat tool.

## Course context

Built for the **Red Team Thinking in the Age of AI** intensive (Bryce Hoffman, Chris Butler, Scott Henderson), pairing AI with Red Team Thinking to stress-test human plans.
