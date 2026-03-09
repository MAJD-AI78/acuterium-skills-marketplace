---
name: pdf
display_name: Pdf
skill_id: ACU-SKILL-2025
version: 1.0.0
category: multimodal
thread: T03
domain: cognitive
shard_affinity:
  - Baranurion-L1
layer_access:
  - L1
  - L2
  - L3
sovereignty_score: 9
governance_level: restricted
source_repo: anthropics/skills
triggers:

---

# Pdf

## Description
Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.

## Acuterium Integration
- **Thread:** T03 — HISN
- **Shard:** Baranurion-L1
- **Layers:** L1, L2, L3
- **Governance:** restricted
- **Sovereignty Score:** 9/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** anthropics/skills
- **File:** skills/pdf/SKILL.md
- **Author:** anthropics/skills
