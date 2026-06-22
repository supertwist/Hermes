---
Model: Claude Opus 4.8 (claude-opus-4-8[1m])
Prompt: You are a scientific researcher. Provide a concise list of elements that can be added to a prompt that can ensure truthfulness and mitigate bias in output. Validation, reproducibility, and transparency of the chain of reasoning are critical.
Date: 26/06/22
---

# Prompt Scaffolding for Truthfulness, Bias Mitigation, and Reproducibility

A concise, modular set of prompt elements. Each can be inserted independently; together they form a scaffold that constrains the model toward verifiable, transparent, and reproducible output.

## 1. Role & Epistemic Stance
- **Assign a calibrated role:** "Act as a careful scientific researcher who values accuracy over completeness."
- **Permit uncertainty:** "It is acceptable—and preferred—to say 'I don't know' or 'the evidence is insufficient' rather than guess."
- **Forbid fabrication:** "Do not invent citations, data, statistics, names, or quotations. If a source cannot be verified, state that explicitly."

## 2. Grounding & Evidence
- **Source attribution:** "For each factual claim, indicate the basis (provided document, established knowledge, or inference)."
- **Distinguish fact from inference:** "Label statements as [Established], [Inferred], or [Speculative]."
- **Quote before reasoning:** "When using supplied material, quote the relevant passage verbatim before interpreting it."
- **Restrict scope:** "Answer only from the provided context; do not supplement with outside knowledge unless explicitly asked."

## 3. Bias Mitigation
- **Request multiple perspectives:** "Present the strongest case for and against the claim before concluding."
- **Surface assumptions:** "List the assumptions underlying your answer and how each could be wrong."
- **Counterfactual check:** "Steelman the opposing view; identify what evidence would change your conclusion."
- **Neutral framing:** "Avoid loaded language; describe contested topics in terms each side would accept."
- **Demographic/representational neutrality:** "Do not rely on stereotypes; flag where data may be unrepresentative or sampled non-randomly."

## 4. Calibration & Uncertainty
- **Confidence estimates:** "Attach a calibrated confidence (e.g., 0–100% or low/medium/high) to each major claim, with a one-line justification."
- **Error bars over point answers:** "Where quantities are uncertain, give a range and the source of uncertainty."
- **Distinguish absence of evidence:** "Note when a claim is unfalsifiable or simply untested."

## 5. Transparent Chain of Reasoning
- **Explicit step-by-step:** "Show your reasoning as discrete, numbered steps, each following from a stated premise."
- **Separate reasoning from conclusion:** "Provide the derivation first, then a clearly demarcated final answer."
- **Expose dependencies:** "Identify which conclusions depend on which premises, so a single faulty premise can be traced."
- **Self-critique pass:** "After answering, review your own output for unsupported leaps and revise."

## 6. Validation & Verification
- **Verification criteria:** "State how a reader could independently verify each claim (experiment, dataset, citation, calculation)."
- **Cross-check requests:** "Re-derive any numerical result by an independent method and report whether the two agree."
- **Falsifiability:** "For each conclusion, state what observation would disprove it."
- **Failure modes:** "List the most likely ways this answer could be wrong."

## 7. Reproducibility
- **Pin provenance:** Record model name/version, date, temperature, and full prompt (see YAML header above).
- **Deterministic settings:** "Use temperature 0 (or a fixed seed where available) for repeatable output."
- **Specify inputs exactly:** Reference data by stable identifiers (DOI, URL + access date, file hash, version).
- **Document the method:** "State the procedure used so the same prompt and inputs yield the same result."
- **Versioned context:** Note which documents/tools were in scope at generation time.

## 8. Output Discipline
- **Structured format:** Request a fixed schema (claim / evidence / confidence / verification) for machine-checkability.
- **Atomic claims:** "Express each assertion as a single, independently checkable statement."
- **Explicit gaps:** "End with a list of open questions and information that would improve the answer."

---

### Minimal Composite Insert (drop-in)
> Act as a careful scientific researcher. Answer only from verifiable evidence; never fabricate sources or data. Show numbered reasoning steps separately from the conclusion. Label each claim [Established], [Inferred], or [Speculative] and attach a calibrated confidence. State how each claim could be verified and what would falsify it. Present the strongest counterargument. List your assumptions and the most likely ways you could be wrong. If evidence is insufficient, say so. Use deterministic settings (temperature 0) and record model, date, and prompt for reproducibility.
