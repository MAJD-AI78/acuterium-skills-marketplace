---
name: analyzing-windows-event-logs-in-splunk
display_name: Analyzing Windows Event Logs In Splunk
skill_id: ACU-SKILL-1285
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

# Analyzing Windows Event Logs In Splunk

## Description
Analyzes Windows Security, System, and Sysmon event logs in Splunk to detect authentication attacks, privilege escalation, persistence mechanisms, and lateral movement using SPL queries mapped to MITRE ATT&CK techniques. Use when SOC analysts need to investigate Windows-based threats, build detection queries, or perform forensic timeline analysis of Windows endpoints and domain controllers.


## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/analyzing-windows-event-logs-in-splunk/SKILL.md
- **Author:** cybersecurity-community
