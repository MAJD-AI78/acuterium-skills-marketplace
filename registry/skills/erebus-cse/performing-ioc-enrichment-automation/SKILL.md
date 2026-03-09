---
name: performing-ioc-enrichment-automation
display_name: Performing Ioc Enrichment Automation
skill_id: ACU-SKILL-1685
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

# Performing Ioc Enrichment Automation

## Description
Automates Indicator of Compromise (IOC) enrichment by orchestrating lookups across VirusTotal, AbuseIPDB, Shodan, MISP, and other intelligence sources to provide contextual scoring and disposition recommendations. Use when SOC analysts need rapid multi-source enrichment of IPs, domains, URLs, and file hashes during alert triage or incident investigation.


## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/performing-ioc-enrichment-automation/SKILL.md
- **Author:** cybersecurity-community
