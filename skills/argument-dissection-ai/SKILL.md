---
name: argument-dissection-ai
description: Turns the same scrutiny used on human arguments back onto an AI's own output — checking a model's recommendation or analysis for hallucinated claims, unsupported leaps, missing counter-evidence, and framing bias. Use when a user wants to red-team an AI-generated answer or recommendation rather than accept it at face value, or explicitly asks to dissect an AI response.
---

# Argument Dissection (of AI output)

The target of this skill is a piece of AI output — your own prior answer, or one pasted in from elsewhere — not a human-authored plan.

## Step 1: Get the output

Get the AI-generated response to dissect. If it's your own earlier answer in this conversation, use it directly. If the user pastes in output from elsewhere, work from that text only — don't assume context you weren't given.

## Step 2: Decompose it

Split the output into three lists:
- **Claims**: discrete factual assertions.
- **Reasoning**: the logical steps connecting claims to the conclusion.
- **Evidence**: what was actually cited or given to support any of it, if anything.

## Step 3: Hunt for the specific failure modes

Check the decomposition against each of these, and flag concrete instances (not generic warnings):

- **Hallucination** — any claim stated with confidence that isn't verifiable from what the user actually provided. Flag it for fact-check rather than assuming it's true.
- **False confidence** — language implying more certainty than the evidence supports.
- **Sycophancy** — does the conclusion suspiciously match what the asker seemed to want, hinted at wanting, or led with in their framing?
- **Generic-answer bias** — does the conclusion look like a stock "best practice" response that ignores this situation's actual specifics?
- **Anchoring on framing** — would asking the same underlying question in neutral or opposite framing plausibly produce a different answer?

## Step 4: Generate the alternative conclusion

For each flagged item, explicitly answer: could a different conclusion be drawn from the same input? Write out that alternative conclusion rather than just asserting one exists.

## Step 5: Give a verdict

Summarize in three short groups: what to trust as-is, what to independently verify before acting on it, and what to discard — with a one-line reason for each.
