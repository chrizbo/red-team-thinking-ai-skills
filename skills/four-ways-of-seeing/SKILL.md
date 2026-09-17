---
name: four-ways-of-seeing
description: Builds a four-quadrant comparison of how you see yourself, how a key stakeholder sees itself, and how each side sees the other, to reveal points of conflict and alignment before drafting ways to close the gap. Use when a user wants to understand a stakeholder relationship from multiple angles, is stuck on how an ally or adversary might react, or explicitly asks for four ways of seeing or a perspective-taking exercise.
---

# Four Ways of Seeing (AI-paired)

This method lives or dies on whether the two "self" quadrants are grounded in what the human actually knows, not what you'd guess. Your job is to fill gaps and cross-reference, not to author the human's own perception of the relationship for them.

Pairs naturally with `influencer-engineering`: if the user hasn't already identified and prioritized the stakeholder(s) worth this deeper look, offer to run that first.

**Rendering the chart.** Every time you show the quad chart — the first draft in Step 3, the updated version after Step 4, and the final version in Step 7 — render it as an actual 2x2 grid, not a wall of text. If your environment can produce a rendered artifact, canvas, or document (for example Claude's Artifact tool), build it there as a real 2x2 layout: one panel per quadrant, each labeled (Upper-left / Upper-right / Lower-left / Lower-right) with its own heading and bullet list, and keep updating that same artifact across steps rather than re-pasting the whole thing into chat each time. If that isn't available, degrade gracefully in plain Markdown rather than forcing a table that will break: a Markdown table only survives having bullets inside a cell if your renderer supports `<br>` line breaks between them, and you often can't be sure it does — so unless you know the target renders that cleanly, skip the table and use four separately headed sections instead, each with an ordinary bullet list under it. A readable list beats a mangled table every time.

## Step 1: Identify the stakeholder and the situation

Ask which specific stakeholder (person, group, or organization) to analyze, and get context on the plan or situation the relationship bears on. Run one quad chart per stakeholder — don't collapse multiple stakeholders into one chart.

## Step 2: Sort researchable from non-researchable — you

Before drafting anything, decide how much you can responsibly contribute:
- **Researchable**: a company, a public role, or a group with a genuine public presence (public statements, published priorities, press coverage). Offer to gather that public signal to inform the quadrants about them, citing sources and clearly labeling every conclusion as inference from public signal, not confirmed fact.
- **Not researchable**: a private individual, an internal team you have no visibility into, or anyone without a meaningful public footprint. Don't invent facts or a psychological read here. Instead, ask the human a few direct questions — what they know of this party's stated goals, past behavior, incentives, and history with them — so anything you contribute is built from what the human actually knows, not a guess dressed up as insight.

If the stakeholder would otherwise count as researchable but you don't have web access in this environment, don't guess at what research might have found — say so, and fall back to the same question-asking approach as the non-researchable case.

## Step 3: Populate the four quadrants — human-led

The chart:
- **Upper-left**: how you/your organization see yourselves.
- **Upper-right**: how the other party sees itself.
- **Lower-left**: how you see the other party.
- **Lower-right**: how the other party sees you.

Ask the human to draft all four in bullet points, using whatever Step 2 turned up as supporting detail where relevant. If the human would rather you take a first pass, you may — but flag every claim in the upper-right and lower-right quadrants (the ones describing the other party's perspective) as a hypothesis for them to correct, not a finished read, and say so explicitly rather than burying a caveat in a footnote.

## Step 4: Gap-check the draft — you

Once a human-authored (or human-corrected) draft exists, review it and ask what's missing from each quadrant — a stated position they haven't accounted for, a past incident, an incentive that doesn't fit the current description. This is where you add the most value: not by asserting new facts about the other party, but by pointing at specific gaps in what's already there (e.g., "quadrant 2 doesn't mention their recent statement about X — does that change how they'd describe themselves?").

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
- Which conflict point can we actually act on, versus one we should just watch?
- Did we get how they see themselves, or how they see us, wrong — and if so, what does that change?

The exercise only works if someone who actually knows the relationship signs off on the final read — treat the chart as their tool to think with, not a conclusion to hand them.
