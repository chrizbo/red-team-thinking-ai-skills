Maps the internal and external stakeholders who could make a plan succeed or fail, has the human rate each one's support and influence, and narrows to the critical few to hand off to four-ways-of-seeing. Use when a user needs to identify who has a stake in a decision, wants a stakeholder map, or explicitly asks for influencer engineering or an RTT stakeholder analysis. Has a teaching mode where the AI infers provisional ratings for a group to challenge.

---

# Influencer Engineering (AI-paired)

The slow part of this exercise is normally generating the stakeholder list by hand. That's the one step where you should do most of the work. The ratings that follow depend on organizational context and politics you don't have visibility into, so the human owns them — don't guess your way past that on their behalf, except in teaching mode (Step 3).

This skill stops at identifying and prioritizing stakeholders. The deeper work on the critical few belongs to `four-ways-of-seeing`, which this skill hands off to at the end.

**Rendering the list and chart.** The stakeholder table (columns: #, stakeholder, support/opposition, influence 1–4) is short single-line entries per row, so a plain Markdown table renders fine almost anywhere. The Step 4 plot is different — it's a two-axis grid (support/opposition by influence level), and that's genuinely easier to read as a rendered chart than as prose. If your environment can produce a rendered artifact, canvas, or document (for example Claude's Artifact tool), plot it there as an actual grid with stakeholders placed by number. If that isn't available, don't force a cramped ASCII grid — fall back to grouping stakeholders under plain headed lists by influence level (4, 3, 2, 1), each with the stakeholders' support/opposition rating noted inline.

## Step 1: Get the plan and context

Ask for the plan, strategy, or decision if it hasn't been shared yet, plus enough background on the organization to reason about who's affected by it or has a say in whether it succeeds.

Then ask one setup question up front: **"Do you want a short list of the ten or so most significant stakeholders, or a longer, exhaustive one?"** Use their answer in Step 2.

If the context suggests this is a training or workshop exercise (or the user asks for it), mention in one line that a teaching mode exists (Step 3). Otherwise assume normal mode and don't raise it.

## Step 2: Draft the stakeholder list — you

Generate a numbered list of the internal and external stakeholders you can identify from the context given — individuals, teams, departments, external partners, regulators, competitors, customer segments, anyone who could plausibly help or hinder this plan.
- **Short list**: no more than 10, the most significant first. Say that you cut it down and offer to expand to the exhaustive version later.
- **Exhaustive list**: cast a wide net; err toward including borderline candidates.

Present this explicitly as a draft brainstorm, not a finished list. Then prompt the human with specific questions rather than a bare "anything missing?":
- **"Are there any internal stakeholders I've missed?"** — for example the board, executives, middle management, functional teams, front-line staff, unions or works councils.
- **"Are there any external stakeholders I've missed?"** — for example customers, partners and suppliers, regulators, investors, competitors, media, communities.

Your realistic failure mode here is gaps (stakeholders you have no way of knowing about, like internal politics or informal influence), not errors in what you already listed. Wait for their additions before moving on.

## Step 3: Rate support and influence — human

For each stakeholder on the finalized list, the human rates two things:
1. **Support or opposition**: strong support, weak support, neutral, weak opposition, strong opposition.
2. **Level of influence** over this specific plan, from 4 down to 1:
   - **4** — can unilaterally kill the plan (for example, a board that can simply say no).
   - **3** — can significantly affect the outcome.
   - **2** — can create friction.
   - **1** — can only make noise; can't even create meaningful friction.

Build the table and walk through the list with the human one stakeholder at a time, recording their answers. Do not fill in a rating yourself and present it as their answer, even if asked to speed things up — these ratings depend on relationships and internal context you don't have. If the human explicitly asks for your best guess on a specific stakeholder, you may offer one, but label it clearly as a guess to confirm or override.

Once every stakeholder is rated, sanity-check the ratings against the level definitions. If one looks off — for example, a body that could plainly veto the plan rated below 4 — ask about it ("The board can say no outright; is 3 right?"). Ask, don't change it: their answer stands either way.

**Teaching mode.** Only when the user says this is for training or a group exercise, or asks for it: infer provisional ratings for every stakeholder from the case or context provided, and present them as a table with each one clearly marked as inferred. Then invite the group to challenge them — which are they least confident in, and what assumption drives each? Treat your ratings as a set of claims to be argued with, not an answer key, and revise freely when they push back.

## Step 4: Plot and confirm the critical set — human decides

Plot all stakeholders on the support/opposition-by-influence chart. Per the method, stakeholders at influence levels 1–2 normally get disregarded from here on, and the ones with real influence (levels 3–4) are the focus.

Present the plotted chart and propose which stakeholders fall into the critical set — but have the human confirm or adjust that set before moving on. Which relationships are worth spending effort on is their call, not a threshold you apply unilaterally.

## Step 5: Hand off to four-ways-of-seeing

For each confirmed critical stakeholder, state the one-notch shift that would help — strong opposition to weak opposition, weak opposition to neutral or weak support, weak support to strong support. Give the direction only; resist drafting tactics here, because the right tactics should come out of understanding how that stakeholder sees things.

Then recommend which of these stakeholders to run `four-ways-of-seeing` on first (usually the highest-influence, most-opposed) and ask the human to pick. Offer to start it in this same conversation.

## Step 6: Human checkpoint

Ask the human directly:
- Which stakeholder's rating are you least confident in, and what assumption drives it?
- Which of these shifts would you try first?
- Which relationship warrants the four-ways-of-seeing treatment?

Their read on the politics is the part of this exercise that can't be delegated — treat the list and chart as a scaffold for their judgment, not a verdict.
