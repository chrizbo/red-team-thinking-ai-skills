---
description: "Maps the internal and external stakeholders who could make a plan succeed or fail, rates each one's support and influence, and drafts concrete ways to move opposition toward support. Use when a user needs to identify who has a stake in a decision, wants a stakeholder map, or explicitly asks for influencer engineering or an RTT stakeholder analysis."
---

<!-- Generated from skills/influencer-engineering/SKILL.md — edit the canonical file, not this one. -->

# Influencer Engineering (AI-paired)

The slow part of this exercise is normally generating the stakeholder list by hand. That's the one step where you should do most of the work. The rating and prioritization steps that follow depend on organizational context and politics you don't have visibility into — don't guess your way past those on the human's behalf.

Pairs naturally with `four-ways-of-seeing`: once the stakeholders here are identified and prioritized, the top few are good candidates for a deeper quad-chart look at how each side actually sees the other.

**Rendering the list and chart.** The Step 2/3 stakeholder list is short single-line entries per row, so a plain Markdown table (columns: #, stakeholder, support/opposition, influence) renders fine almost anywhere and there's no need for anything fancier. The Step 5 plot is different — it's a two-axis grid (support/opposition by influence level), and that's genuinely easier to read as a rendered chart than as prose. If your environment can produce a rendered artifact, canvas, or document (for example Claude's Artifact tool), plot it there as an actual grid with stakeholders placed by number. If that isn't available, don't force a cramped ASCII grid — fall back to grouping stakeholders under plain headed lists by influence level (Showstoppers, Significant impact, Friction/noise, No influence), each with the stakeholders' support/opposition rating noted inline.

## Step 1: Get the plan and context

Ask for the plan, strategy, or decision if it hasn't been shared yet, plus enough background on the organization to reason about who's affected by it or has a say in whether it succeeds.

## Step 2: Draft the stakeholder long-list — you

Generate a numbered list of every internal and external stakeholder you can identify from the context given — individuals, teams, departments, external partners, regulators, competitors, customer segments, anyone who could plausibly help or hinder this plan. Cast a wide net; err toward including borderline candidates.

Present this explicitly as a draft brainstorm, not a finished list. Then ask the human: **"Who's missing?"** — not "which of these are wrong." Your realistic failure mode here is gaps (stakeholders you have no way of knowing about, like internal politics or informal influence), not errors in what you already listed. Frame the ask accordingly and wait for their additions before moving on.

## Step 3: Rate support and influence — ask, don't guess

For each stakeholder on the finalized list, the human rates two things:
1. **Support or opposition**: strong support → weak support → neutral → weak opposition → strong opposition.
2. **Level of influence** over this specific plan: no influence, ability to create friction/noise, ability to significantly impact the outcome, or showstopper.

Build the table or chart structure and walk through the list with the human one stakeholder at a time, recording their answers. Do not fill in a rating yourself and present it as their answer, even if asked to speed things up — these ratings depend on relationships and internal context you don't have. If the human explicitly asks for your best guess on a specific stakeholder, you may offer one, but label it clearly as a guess to confirm or override, and only do this when they've asked for it.

## Step 4: Optional research assist — you, with limits

For stakeholders that are publicly documented organizations, companies, or people acting in a public professional capacity (not private individuals, and not internal teams you have no way to observe), offer to gather public signal that might inform their likely stance — recent public statements, published priorities, open job postings that hint at direction, industry commentary. Cite what you found. Label every inference drawn from it as inference, not fact, and never present it as confirming a specific rating from Step 3 — hand it to the human as input to their own rating instead.

Skip this step entirely for anyone not genuinely public, and don't go looking for information on private individuals beyond their professional public presence.

If you don't have web access in this environment, don't guess at what research might have found. Say so, and instead ask the human directly what they already know of that stakeholder's stated priorities or recent public moves — the same question-asking fallback as for a non-public stakeholder.

## Step 5: Plot and confirm the critical set — human decides

Plot all stakeholders on the support/opposition-by-influence chart. Per the method, stakeholders rated "no influence" or "ability to create friction/noise" (levels 1–2) normally get disregarded from here on, and the ones with real influence (levels 3–4) are the focus.

Present the plotted chart and propose which stakeholders fall into the critical set — but have the human confirm or adjust that set before moving on. Which relationships are worth spending effort on is their call, not a threshold you apply unilaterally.

## Step 6: Draft moves for the critical set — you

For each confirmed critical stakeholder, draft specific, concrete ideas for moving them one notch toward support: strong opposition → weak opposition → neutral/weak support → strong support. Tie each idea to something specific about that stakeholder (their stated concerns, their incentives, what Step 4's research turned up), not a generic tactic that could apply to anyone.

## Step 7: Human checkpoint

Present the full list, chart, and moves, then ask the human directly:
- Which stakeholder's rating are you least confident in, and why?
- Which of these moves would you actually attempt, and which are we kidding ourselves about?
- Is there a relationship here worth the deeper look that `four-ways-of-seeing` gives?

Their read on the politics is the part of this exercise that can't be delegated — treat the list and chart as a scaffold for their judgment, not a verdict.
