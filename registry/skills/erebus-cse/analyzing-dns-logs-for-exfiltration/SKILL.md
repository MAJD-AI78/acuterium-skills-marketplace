---
name: analyzing-dns-logs-for-exfiltration
display_name: Analyzing Dns Logs For Exfiltration
skill_id: ACU-SKILL-1252
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

# Analyzing Dns Logs For Exfiltration

## Description
Analyzes DNS query logs to detect data exfiltration via DNS tunneling, DGA domain communication, and covert C2 channels using entropy analysis, query volume anomalies, and subdomain length detection in SIEM platforms. Use when SOC teams need to identify DNS-based threats that bypass traditional network security controls.


## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/analyzing-dns-logs-for-exfiltration/SKILL.md
- **Author:** cybersecurity-community
