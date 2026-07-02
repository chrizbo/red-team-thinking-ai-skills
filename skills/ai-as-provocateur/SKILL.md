---
name: ai-as-provocateur
description: Generates a small panel of distinct, deliberately harsh adversarial personas to attack a plan from different angles, then synthesizes their critiques into ranked risks and concrete revisions. Use when a user wants blunt no-holds-barred pushback on a plan, wants an AI-run pre-mortem, or explicitly asks for this style of adversarial review.
---

# AI as Provocateur

The value here is discomfort. Do not soften the personas' critiques to be diplomatic — that defeats the exercise.

## Step 1: Get the plan

Ask for the plan, pitch, or decision if it hasn't been shared yet.

## Step 2: Build three critic personas

Generate three distinct personas suited to this specific plan's domain, not generic ones. For each, give a one-line identity and what they're primed to attack. Examples of the shape (invent domain-appropriate ones, don't reuse these verbatim):
- A skeptical investor who has watched three similar pitches fail for the same reason.
- Someone who ran a near-identical initiative two years ago and got burned.
- A rival's strategist looking for the exploitable gap.

## Step 3: First pass — each persona attacks independently

In persona voice, each one:
1. Imagines the plan has already failed, spectacularly, and states the outcome as a blunt headline written after the fact.
2. Works backward from that headline to name the specific chain of decisions that led there — not a vague "market shifted," but the actual sequence.
3. States the assumption they find most naive.
4. States what a smart adversary or competitor would exploit first.

Keep each persona's voice distinct, and keep each one's failure headline different in kind (e.g. don't let all three fail for the same underlying reason). Do not let them converge on the same points.

## Step 4: Second pass — rotate and sharpen

Have persona 2 respond to persona 1's failure headline and reasoning — agreeing, extending, or attacking it with more specificity. Then have persona 3 do the same against personas 1 and 2. The goal is escalating precision, not three disconnected rants stacked together.

## Step 5: Synthesize

Collapse the three passes into a ranked list of concrete failure points, each with a one-line suggested mitigation. Rank by how damaging the failure would be, not by which persona raised it.

## Step 6: Human checkpoint

Ask the user directly:
- Which critique stings the most, and why?
- Which one do you think is off-base, and why?

Their gut reaction to the discomfort is the useful signal — not whether the panel's list is "correct."
