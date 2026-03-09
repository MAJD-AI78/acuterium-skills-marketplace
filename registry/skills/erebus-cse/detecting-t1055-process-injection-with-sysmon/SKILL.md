---
name: detecting-t1055-process-injection-with-sysmon
display_name: Detecting T1055 Process Injection With Sysmon
skill_id: ACU-SKILL-1435
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

# Detecting T1055 Process Injection With Sysmon

## Description
Detect process injection techniques (T1055) including classic DLL injection, process hollowing, and APC injection by analyzing Sysmon events for cross-process memory operations, remote thread creation, and anomalous DLL loading patterns.

## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/detecting-t1055-process-injection-with-sysmon/SKILL.md
- **Author:** cybersecurity-community
