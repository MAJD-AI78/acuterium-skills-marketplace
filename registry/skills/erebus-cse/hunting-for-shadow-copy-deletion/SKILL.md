---
name: hunting-for-shadow-copy-deletion
display_name: Hunting For Shadow Copy Deletion
skill_id: ACU-SKILL-1496
version: 1.0.0
category: forensics
thread: T08
domain: security
shard_affinity:
  - Tenebris-ACIWS
layer_access:
  - L8
  - L9
  - L10
sovereignty_score: 10
governance_level: sovereign
source_repo: mukul975/Anthropic-Cybersecurity-Skills
triggers:

---

# Hunting For Shadow Copy Deletion

## Description
Hunt for Volume Shadow Copy deletion activity that indicates ransomware preparation or anti-forensics by monitoring vssadmin, wmic, and PowerShell shadow copy commands.

## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/hunting-for-shadow-copy-deletion/SKILL.md
- **Author:** cybersecurity-community
