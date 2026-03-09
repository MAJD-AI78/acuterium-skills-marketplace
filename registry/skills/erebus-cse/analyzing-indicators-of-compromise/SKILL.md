---
name: analyzing-indicators-of-compromise
display_name: Analyzing Indicators Of Compromise
skill_id: ACU-SKILL-1256
version: 1.0.0
category: malware
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

# Analyzing Indicators Of Compromise

## Description
Analyzes indicators of compromise (IOCs) including IP addresses, domains, file hashes, URLs, and email artifacts to determine maliciousness confidence, campaign attribution, and blocking priority. Use when triaging IOCs from phishing emails, security alerts, or external threat feeds; enriching raw IOCs with multi-source intelligence; or making block/monitor/whitelist decisions. Activates for requests involving VirusTotal, AbuseIPDB, MalwareBazaar, MISP, or IOC enrichment pipelines.


## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/analyzing-indicators-of-compromise/SKILL.md
- **Author:** cybersecurity-community
