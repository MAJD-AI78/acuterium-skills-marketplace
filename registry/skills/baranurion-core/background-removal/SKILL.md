---
name: background-removal
display_name: Background Removal
skill_id: ACU-SKILL-2065
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
source_repo: andersoncollab/design-agent
triggers:

---

# Background Removal

## Description
This skill provides production integration with the remove.bg API to automatically remove backgrounds from images. Use it to process product photos, headshots, social media assets, and creative materials into transparent PNGs. The API uses AI to detect subjects (person, product, car, animal) and cleanly removes backgrounds.

## Acuterium Integration
- **Thread:** T03 — HISN
- **Shard:** Baranurion-L1
- **Layers:** L1, L2, L3
- **Governance:** restricted
- **Sovereignty Score:** 9/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** andersoncollab/design-agent
- **File:** skills/background-removal/SKILL.md
- **Author:** andersoncollab
