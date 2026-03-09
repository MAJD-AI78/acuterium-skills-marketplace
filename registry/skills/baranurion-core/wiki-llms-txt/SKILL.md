---
name: wiki-llms-txt
display_name: Wiki Llms Txt
skill_id: ACU-SKILL-2170
version: 1.0.0
category: documentation
thread: T02
domain: cognitive
shard_affinity:
  - APMS
layer_access:
  - L4
  - L5
  - L6
sovereignty_score: 9
governance_level: restricted
source_repo: microsoft/skills
triggers:

---

# Wiki Llms Txt

## Description
Generates llms.txt and llms-full.txt files for LLM-friendly project documentation following the llms.txt specification. Use when the user wants to create LLM-readable summaries, llms.txt files, or make their wiki accessible to language models.

## Acuterium Integration
- **Thread:** T02 — DIAR
- **Shard:** APMS
- **Layers:** L4, L5, L6
- **Governance:** restricted
- **Sovereignty Score:** 9/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** microsoft/skills
- **File:** .github/plugins/deep-wiki/skills/wiki-llms-txt/SKILL.md
- **Author:** Microsoft
