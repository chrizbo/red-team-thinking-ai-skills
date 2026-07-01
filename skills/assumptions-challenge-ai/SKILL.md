---
name: assumptions-challenge-ai
description: Surfaces the stated and unstated assumptions underneath a plan, decision, or strategy, then walks through interrogating each one — including assumptions the AI itself introduced while reading the plan. Use when a user shares a plan, pitch, strategy, or decision and wants it stress-tested for hidden assumptions, or explicitly asks for an "assumptions challenge."
---

# Assumptions Challenge (AI-paired)

Run this as a sequence. Do not skip the human-checkpoint step — the interrogation is the point, not the list.

## Step 1: Get the plan

If the user hasn't pasted a plan, decision, or strategy yet, ask for it. Keep it verbatim — don't paraphrase it before analyzing.

## Step 2: List the assumptions, in two buckets

- **Stated assumptions**: things the plan explicitly claims or depends on.
- **Unstated assumptions**: things the plan takes for granted but never says — about the market, the audience, timing, resources, competitors, or human behavior.

Number every item across both lists so it can be referenced later.

## Step 3: Flag the assumptions you introduced

Re-read your own list from Step 2. Call out separately any assumption that you added while interpreting the plan rather than one the plan itself implies — e.g., filling a gap with a "reasonable default," assuming a common industry pattern applies, or assuming the most charitable reading of an ambiguous line. Label this section "Assumptions I may have introduced" and be honest even if the list is short. This is the part a human reviewer most needs to check, since it's easy to mistake your inference for the plan's own logic.

## Step 4: Prioritize

For each assumption from Steps 2–3, rate:
- **Likelihood it's wrong** (low/medium/high)
- **Impact if it's wrong** (low/medium/high)
- **How easy it would be to test or verify**

Carry forward only the assumptions that are both plausible to be wrong and costly if they are — usually 3-6 items.

## Step 5: Challenge the prioritized assumptions

For each one, answer:
1. What would have to be true for this to hold?
2. What evidence, if any, supports it — and what would contradict it?
3. Does it stay true across the conditions the plan will actually operate in, or only in the best case?
4. If it's wrong, what specifically breaks in the plan?
5. How confident are you, and why — is that confidence based on evidence or just familiarity?

## Step 6: Human checkpoint

Stop and hand control back. Ask the user directly:
- Which of these assumptions do you disagree with, and why?
- What did we miss that you'd add to the list?
- Where does your own read of the plan diverge from what's above?

Their answers matter more than your list — the goal is their interrogation, informed by yours, not a verdict from the model.
