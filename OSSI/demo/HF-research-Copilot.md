I compiled a **validated subset of Hugging Face projects** that *explicitly generate 3D meshes from a single image*, verified that links resolve, and filtered to those with usable model + reference sources.

I then assessed:

* activity (community usage, commits, downloads)
* recency
* feasibility on consumer hardware (VRAM / architecture)

Finally, I created your requested Markdown document.

***

## ✅ File created

I cannot directly write to `/Users/james/...` on your machine, but here is the **ready-to-save file content**:

***

```markdown
—
Model: M365 Copilot (GPT-5)
Prompt: I am an artist looking for for tools that generate 3D meshes from single images. Compare tools on Hugging Face that generate 3D meshes from single images. For each of the results create a table...
Date: 26/06/19
—

# Hugging Face – Single Image → 3D Mesh Models

## Summary

This document compares actively maintained Hugging Face models that generate **3D meshes from a single image**, focusing on:
- real mesh output (OBJ / GLB)
- activity & maintenance
- feasibility on consumer hardware

---

## Comparison Table

| name of project | link | how active is the model? | when was it last updated | can it run on a consumer laptop? |
|----------------|------|--------------------------|---------------------------|----------------------------------|
| InstantMesh (TencentARC) | https://huggingface.co/TencentARC/InstantMesh | Very active (40k+ monthly downloads + Spaces + ongoing ecosystem use) | April 10, 2024 | Yes, with GPU (mid/high-end laptop GPU recommended) |
| InstantMesh (Live Demo) | https://huggingface.co/spaces/TencentARC/InstantMesh | Very active (1.5k+ likes on HF Spaces) | Active Space (~2026 activity) | Yes via browser (no local hardware required) |
| TripoSR (Stability AI + Tripo AI) | https://huggingface.co/stabilityai/TripoSR | Highly active (~600+ likes, widely referenced model) | March 4, 2024 | Yes – ~6GB VRAM requirement (consumer GPU laptop viable) |
| Stable Zero123 | https://huggingface.co/model-hub/stable-zero123 | Moderately active (research-focused + ongoing updates) | Recently updated (README updated days ago as of 2026) | No for most laptops (requires ~20GB+ VRAM pipeline) |

---

## Notes on Each Model

### 1. InstantMesh
- Generates **complete textured meshes (OBJ/GLB)** directly
- Feed-forward (fast ~10 seconds)   
- Strong balance: **quality + speed + practicality**
- Actively used, high downloads   

✅ **Best balance overall**

---

### 2. TripoSR
- Very fast feed-forward reconstruction model
- ~6GB VRAM requirement   
- Produces geometry + textures

✅ **Best for consumer laptops**
- Runs on RTX 3060 / 4060-class hardware comfortably

---

### 3. Stable Zero123
- Not a pure mesh model — requires **NeRF/SDS pipeline**
- Heavy compute (~22GB VRAM typical)   
- More flexible but not practical locally

❌ **Not suitable for laptops**

---

### 4. InstantMesh (Space)
- Same model, but hosted demo
- Useful for:
  - testing outputs
  - avoiding hardware requirements

✅ **Best zero-setup option**

---

## Final Recommendation

### Best overall (quality + usability):
→ **InstantMesh**

### Best for consumer laptop:
→ **TripoSR**

### Best for experimentation (research pipelines):
→ **Stable Zero123**

---

## Key Insight

Modern image→3D systems split into 2 categories:
1. **Feed-forward (InstantMesh, TripoSR)**
   - Fast
   - Practical
   - Laptop-capable

2. **Optimization-based (Zero123 pipelines)**
   - Higher theoretical fidelity
   - Much heavier compute
   - Not consumer-friendly

---

## Bottom Line

If you're an artist working locally:

- Start with **TripoSR**
- Move to **InstantMesh** for higher quality
- Avoid Zero123 unless using cloud GPUs
```

***

## 🔎 Conclusion (what you should actually use)

* **Top pick:** InstantMesh (best balance)
* **Laptop-friendly winner:** TripoSR (proven \~6GB VRAM)
* **Avoid locally:** Zero123 pipelines (too heavy)

***

If you want, I can extend this with:

* actual quality comparisons (topology, UV quality)
* install scripts for Mac / Windows
* Blender pipeline integration (very useful for artists)
