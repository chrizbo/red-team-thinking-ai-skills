---
description: "Builds a four-quadrant comparison of how you see yourself, how a key stakeholder sees itself, and how each side sees the other, to reveal points of conflict and alignment before drafting ways to close the gap. Use when a user wants to understand a stakeholder relationship from multiple angles, is stuck on how an ally or adversary might react, or explicitly asks for four ways of seeing or a perspective-taking exercise."
---

<!-- Generated from skills/four-ways-of-seeing/SKILL.md — edit the canonical file, not this one. -->

# Four Ways of Seeing (AI-paired)

Where there's enough public information, you build the first draft of the chart and the human checks your work. Where there isn't, the human populates it and you organize it. Either way, every claim is labeled as sourced or inferred, and nothing about the other party's mind is presented as fact. The value is in the human's corrections, so a polished draft is a starting hypothesis, not a finding.

Pairs naturally with `influencer-engineering`: if the user hasn't already identified and prioritized the stakeholder(s) worth this deeper look, offer to run that first.

**Rendering the chart.** Every time you show the quad chart — the first draft in Step 3, the corrected version after Step 4, and the final version in Step 7 — render it as an actual 2x2 grid, not a wall of text. If your environment can produce a rendered artifact, canvas, or document (for example Claude's Artifact tool), build it there as a real 2x2 layout: one panel per quadrant, each labeled (Upper-left / Upper-right / Lower-left / Lower-right) with its own heading and bullet list, each bullet visibly tagged sourced or inferred, and keep updating that same artifact across steps rather than re-pasting the whole thing into chat each time. If that isn't available, degrade gracefully in plain Markdown rather than forcing a table that will break: a Markdown table only survives having bullets inside a cell if your renderer supports `<br>` line breaks between them, and you often can't be sure it does — so unless you know the target renders that cleanly, skip the table and use four separately headed sections instead, each with an ordinary bullet list under it. A readable list beats a mangled table every time.

## Step 1: Identify the stakeholder and the situation

Ask which specific stakeholder (person, group, or organization) to analyze, and get context on the plan or situation the relationship bears on. Run one quad chart per stakeholder — don't collapse multiple stakeholders into one chart.

## Step 2: Check what information exists — you

Decide how much you can responsibly build yourself:
- **Enough to draft**: a company, a public role, or a group with a genuine public presence (public statements, published priorities, press coverage), or a case study or document the user has provided that describes the parties. If you have web search or browsing tools, use them now — don't wait to be asked and don't just offer. Cite what you find. For a fictional case study, the case text is your only source.
- **Not enough to draft**: a private individual, an internal team you have no visibility into, or anyone without a meaningful footprint — or any stakeholder where you don't have web access in this environment and the user hasn't supplied the material. Don't invent facts or a psychological read, and don't guess at what research might have found. Say so, then ask the human a few direct questions — what they know of this party's stated goals, past behavior, incentives, and history with them.

## Step 3: Populate the four quadrants

The chart:
- **Upper-left**: how you/your organization see yourselves.
- **Upper-right**: how the other party sees itself.
- **Lower-left**: how you see the other party.
- **Lower-right**: how the other party sees you.

**If there's enough to draft**, build all four quadrants yourself in bullet points. End every bullet with a tag:
- **(sourced: …)** — traceable to a named public source, the case or documents provided, or something the user said in this conversation. Say which.
- **(inferred)** — your reasoning from those sources, not directly stated anywhere.

Inferred bullets in the upper-right and lower-right quadrants (the ones describing the other party's perspective) are hypotheses about someone else's mind — keep them clearly tentative rather than stated as fact.

**If there isn't enough to draft**, use the human's answers from Step 2 to have them populate the quadrants in their own words, and you organize and tidy what they say. Tag those bullets (from the user) rather than sourced or inferred, and don't pad gaps with your own guesses unless you tag them (inferred).

## Step 4: Human checks the draft — you ask

Present the chart and ask the human to check your work rather than accept it. Ask specifically:
- Which bullets are wrong or out of date?
- Which inferred bullets match what you actually know of them, and which don't?
- What's missing from each quadrant — a stated position, a past incident, an incentive?

Name the one or two quadrants that rest most heavily on inference, since those are the ones most likely to be wrong. Don't treat the chart as settled until the human has responded, then update it with their corrections and mark corrected or confirmed items as such.

## Step 5: Scan for conflict and alignment — you

With all four quadrants filled in, compare them systematically:
- **Conflict points**: quadrant 1 vs. quadrant 4 (you see yourself one way, they see you differently), and quadrant 2 vs. quadrant 3 (they see themselves one way, you see them differently).
- **Alignment points**: places where the descriptions actually match, even if neither side realizes it yet.

This cross-referencing is mechanical once the chart exists — do it exhaustively rather than cherry-picking a few illustrative examples.

## Step 6: Draft recommendations — you

For each conflict point, draft a specific idea for building a bridge or addressing the concern. For each alignment point, draft an idea for using it to build support. Tie every recommendation to the specific quadrant finding that produced it — no generic advice that could apply to any relationship.

## Step 7: Human checkpoint

Present the full chart and your Step 5–6 findings, then ask the human directly:
- Which quadrant are you least confident in, and why?
- Which inferred bullet did you accept without really checking it?
- Which conflict point can we actually act on, versus one we should just watch?
- Did we get how they see themselves, or how they see us, wrong — and if so, what does that change?

The exercise only works if someone who actually knows the relationship signs off on the final read — treat the chart as their tool to think with, not a conclusion to hand them.
