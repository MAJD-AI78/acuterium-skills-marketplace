---
name: detecting-t1548-abuse-elevation-control-mechanism
display_name: Detecting T1548 Abuse Elevation Control Mechanism
skill_id: ACU-SKILL-1436
version: 1.0.0
category: red-team
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

# Detecting T1548 Abuse Elevation Control Mechanism

## Description
Detect abuse of elevation control mechanisms including UAC bypass, sudo exploitation, and setuid/setgid manipulation by monitoring registry modifications, process elevation flags, and unusual parent-child process relationships.

## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/detecting-t1548-abuse-elevation-control-mechanism/SKILL.md
- **Author:** cybersecurity-community
