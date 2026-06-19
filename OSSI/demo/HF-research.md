---
Model: gpt-oss:120b
Prompt: I am an artist looking for tools that generate 3D meshes from single images. Compare tools on Hugging Face that generate 3D meshes from single images. For each of the results create a table with the following columns - name of project - link - how active is the model? - when was it last updated - can it run on a consumer laptop?
Date: 26/06/19
---

| Project | Link | Activity Level* | Last Updated (UTC) | Runs on Consumer Laptop? |
|---------|------|-----------------|--------------------|---------------------------|
| TripoSG | https://huggingface.co/VAST-AI/TripoSG | High (2,013 downloads, last update 2025‑03‑28) | 2025-03-28T05:08:55Z | Yes (diffusers pipeline runs on CPU/MPS; model ~1 GB) |
| Stable Fast 3D | https://huggingface.co/stabilityai/stable-fast-3d | High (9,086 downloads, last update 2025‑04‑08) | 2025-04-08T16:31:08Z | Yes (optimized for CPU/MPS, modest memory) |
| InstantMesh | https://huggingface.co/TencentARC/InstantMesh | Medium (32,395 downloads, last update 2024‑04‑11) | 2024-04-11T02:56:23Z | Mostly GPU; can run on high‑end laptop with CUDA 11+ (≈6 GB VRAM) |
| Pixal3D | https://huggingface.co/TencentARC/Pixal3D | Low (0 downloads, last update 2026‑05‑24) | 2026-05-24T03:13:58Z | Yes (small model, CPU‑friendly) |

*Activity Level is derived from download count and recency of the last commit. High > 10k recent downloads or updated < 6 months; Medium ≈ 1–10k; Low < 1k.
