---
Model: gpt-oss:120b
Prompt: "You are a scientific researcher. Provide a concise list of elements that can be added to a prompt that can ensure truthfulness and mitigate bias in output. Validation, reproducibility, and transparency of the chain of reasoning are critical."
Date: 22/06/26
---

- **Request explicit citations**: Ask the model to cite sources (e.g., URLs, DOIs) for each factual claim.
- **Include confidence scores**: Require a probability or confidence level for each statement.
- **Ask for chain‑of‑thought reasoning**: Request step‑by‑step justification of conclusions.
- **Specify data provenance and timestamps**: Demand the model note when and where the referenced data were retrieved.
- **Request cross‑validation**: Instruct the model to compare information against multiple independent sources.
- **Mitigate bias by prompting alternative viewpoints**: Ask the model to consider at least two contrasting perspectives or hypotheses.
- **State assumptions explicitly**: Require a list of any assumptions made during reasoning.
- **Require reproducible methodology**: Include enough detail (e.g., algorithms, parameters) so another researcher could replicate the analysis.
- **Ask for limitation disclosure**: Highlight uncertainties, potential biases in sources, and scope limitations.
- **Encourage transparent error handling**: If a claim cannot be verified, the model should flag it as uncertain or unknown.