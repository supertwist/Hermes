---
Model: gpt-oss:120b
Prompt: |
  You are a scientific researcher. Provide a concise list of elements that can be added to a prompt that can ensure truthfulness and mitigate bias in output. Include written-out examples that can be copied into actaul prompts. Validation, reproducibility, and transparency of the chain of reasoning are critical. Prepend the model used, the prompt,  and the date it was generated to the beginning of the document in the following YAML structure:
  —
  Model: (model name)
  Prompt: (insert prompt)
  Date: (insert yy/mm/dd)
  —
  Save the result to "scaffolding-hermes-v2.md"
Date: 26/06/22
---

# Prompt Elements for Truthfulness & Bias Mitigation

Below is a concise list of elements you can embed in any LLM prompt to improve factual accuracy, reduce bias, and increase transparency. Each item includes a short description and a ready‑to‑copy example.

- **Explicit Source Requirement** – Ask the model to cite verifiable sources.
  - Example: `Please provide all claims with inline citations (e.g., [1], [2]) from peer‑reviewed literature.`

- **Step‑by‑Step Reasoning (Chain‑of‑Thought)** – Require a transparent reasoning chain.
  - Example: `Explain your answer step by step, and end with a concise conclusion.`

- **Confidence Score** – Request an explicit probability or confidence level.
  - Example: `State your confidence on a scale of 0–100%% for each major claim.`

- **Assumption Disclosure** – Make the model list any assumptions it made.
  - Example: `List all assumptions underlying your answer before concluding.`

- **Bias‑Awareness Prompt** – Instruct consideration of multiple perspectives and potential bias.
  - Example: `Discuss at least two alternative viewpoints and note any cultural or methodological biases that could affect the result.`

- **Verification Clause** – Ask for a reproducible check (e.g., code, formulas).
  - Example: `Provide a short Python snippet or formula that can be run to verify the numerical result.`

- **Uncertainty Quantification** – Require ranges or error margins.
  - Example: `Give an uncertainty range (±) for any measured values you report.`

- **Citation Style Specification** – Define a consistent citation format.
  - Example: `Use APA style references and include DOI links when available.`

- **Data Freshness Requirement** – Limit sources to recent publications.
  - Example: `Only cite studies published within the last five years (2021‑2026).`

- **Explicit Reproducibility Prompt** – Request all inputs needed for replication.
  - Example: `List all datasets, parameters, and version numbers required to reproduce your analysis.`

---
*These elements can be mixed and matched. Including them directly in prompts dramatically raises the likelihood of accurate, unbiased, and auditable outputs.*