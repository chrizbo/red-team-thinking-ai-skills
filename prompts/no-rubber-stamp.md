Marks up AI-generated text inline to flag spots where the human should question the machine rather than accept it — using a fixed taxonomy of seven failure modes AI systems are prone to (pattern-over-exception, confidence-vs-evidence gap, sycophancy, softened critique, encoded bias, trade-off/accountability gap, flattened nuance). Use when a user pastes output from an LLM (ChatGPT, Claude, or any AI) and wants it marked up for where to push back, wants to avoid rubber-stamping AI output, or explicitly asks to find where AI output needs human scrutiny.

---

# No Rubber Stamp

Machines and humans are good at different things. Machines are good at finding patterns across large amounts of data, working tirelessly, scaling with compute, generating from examples, and producing low-friction critique. Humans are good at being accountable for outcomes, using emotion and intuition, making exceptions, balancing trade-offs, and reading social and political context. This skill marks up AI output at the seams — the places where it's drifted into territory that plays to a machine's weaknesses rather than its strengths — so the human reading it knows exactly where to slow down.

This is a markup pass, not a rewrite. Don't fix the flagged content or suggest replacement text — the point is to hand the human a map of where to apply their own judgment, not to do that judgment for them.

## Step 1: Get the content

If the user hasn't pasted the AI output yet, ask for it. Keep it verbatim. Ask which model or system produced it if it's not obvious — not required, but useful context for calibrating expectations (e.g. a known-sycophantic model deserves extra scrutiny on that axis).

## Step 2: Scan against the fixed taxonomy

Read through the content and check every claim, recommendation, or judgment call against these seven flags. Use all seven every time — don't invent new categories or skip ones that don't seem to apply on a first pass. Most real content will only trigger 2-4 of them; that's expected.

If the content has labeled speakers or sources and some are clearly human and some clearly AI (e.g. a multi-agent decision log), flag any line that trips the taxonomy regardless of who said it — bad reasoning is bad reasoning either way. Note the source of each flagged line in the summary, since it changes who owes the answer to the question.

1. **Pattern-over-exception** — the content smooths to the typical or majority case, or leans on a memorized template, in a way that may not fit this specific situation. Ask: is there a reason THIS case might be the exception?
2. **Confidence vs. evidence gap** — a claim is stated with more certainty than what's actually backing it. This includes correlation dressed up as causation — a pattern stated as "X leads to Y" when the actual basis is just "X and Y showed up together." Ask: what's the actual evidence here, and does the tone match it?
3. **Sycophancy** — the content is shaped to agree with what the user already said or clearly wants to hear, rather than to independently assess it. Ask: would the answer change if the user's framing were removed?
4. **Softened critique** — a critique or risk is named, but pulled toward generic or safe phrasing instead of the sharpest real objection. Ask: what's the version of this critique that would actually sting?
5. **Encoded bias** — a claim reflects a pattern baked into training data or examples rather than reasoning proper to this specific case. It reads as neutral or objective specifically because the humans behind it — whoever labeled, curated, or designed the examples it learned from — are invisible, not because the bias is absent. Ask: whose default is this, and does it fit here?
6. **Trade-off/accountability gap** — a judgment call is presented as clean or obvious, with no visible owner for the consequence if it's wrong. Ask: what competing value got traded away, and who answers for that choice?
7. **Flattened nuance** — emotional, social, or political texture has been compressed into something clean-sounding. Ask: what's the messier, truer version of this moment?

## Step 3: Mark up inline

Insert a bracketed tag immediately after the flagged span, in plain text so it survives any rendering context:

`[⚠ CATEGORY: one-line reason]`

Use the category names from Step 2 (e.g. `PATTERN-OVER-EXCEPTION`, `CONFIDENCE-GAP`, `SYCOPHANCY`, `SOFTENED-CRITIQUE`, `ENCODED-BIAS`, `ACCOUNTABILITY-GAP`, `FLATTENED-NUANCE`). Reproduce the original content in full with tags inserted — don't excerpt or summarize it away.

## Step 4: Chat summary

After the marked-up text, add a short table ranked by how consequential the miss is (most consequential first), not by order of appearance:

| Flag | Where | Question to ask |
|---|---|---|
| Category | Short quote or pointer | The one-line question from Step 2, made specific to this instance |

Add a Source column (human / AI) only if the content has mixed labeled speakers per Step 2 — omit it for single-author content.

Close with a one-line count by category if more than one flag shares a category (e.g. "3 pattern-over-exception, 2 sycophancy") — this surfaces whether the content has one systemic blind spot or several scattered ones.

Do not end on the table alone. A study on the Wisconsin-mandated COMPAS warning found that giving people a disclaimer about an algorithm's limitations had "no significant effect" on their decisions — people skim past generic warnings and rubber-stamp the output anyway. To avoid that, close by putting the single most consequential flag back to the user as a direct question they have to answer before acting on the content — not "let me know if you have concerns," but the specific question from the table's top row, addressed to them by name of the decision at hand (e.g. "Before you send this: who owns it if the 60% throttle figure is wrong?").
