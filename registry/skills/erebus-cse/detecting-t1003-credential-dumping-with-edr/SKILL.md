---
name: detecting-t1003-credential-dumping-with-edr
display_name: Detecting T1003 Credential Dumping With Edr
skill_id: ACU-SKILL-1434
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

# Detecting T1003 Credential Dumping With Edr

## Description
Detect OS credential dumping techniques targeting LSASS memory, SAM database, NTDS.dit, and cached credentials using EDR telemetry, Sysmon process access monitoring, and Windows security event correlation.

## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/detecting-t1003-credential-dumping-with-edr/SKILL.md
- **Author:** cybersecurity-community
