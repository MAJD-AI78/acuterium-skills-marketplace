---
name: detecting-dcsync-attack-in-active-directory
display_name: Detecting Dcsync Attack In Active Directory
skill_id: ACU-SKILL-1399
version: 1.0.0
category: security
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

# Detecting Dcsync Attack In Active Directory

## Description
Detect DCSync attacks where adversaries abuse Active Directory replication privileges to extract password hashes by monitoring for non-domain-controller accounts requesting directory replication via DsGetNCChanges.

## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/detecting-dcsync-attack-in-active-directory/SKILL.md
- **Author:** cybersecurity-community
