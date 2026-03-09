---
name: recovering-from-ransomware-attack
display_name: Recovering From Ransomware Attack
skill_id: ACU-SKILL-1765
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

# Recovering From Ransomware Attack

## Description
Executes structured recovery from a ransomware incident following NIST and CISA frameworks, including environment isolation, forensic evidence preservation, clean infrastructure rebuild, prioritized system restoration from verified backups, credential reset, and validation against re-infection. Covers Active Directory recovery, database restoration, and application stack rebuild in dependency order. Activates for requests involving ransomware recovery, post-encryption restoration, or disaster recovery from ransomware.


## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/recovering-from-ransomware-attack/SKILL.md
- **Author:** cybersecurity-community
