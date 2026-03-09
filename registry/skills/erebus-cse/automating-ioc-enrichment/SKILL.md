---
name: automating-ioc-enrichment
display_name: Automating Ioc Enrichment
skill_id: ACU-SKILL-1295
version: 1.0.0
category: threat-intelligence
thread: T06
domain: security
shard_affinity:
  - Edna-SIGINT
layer_access:
  - L7
  - L8
  - L9
sovereignty_score: 9
governance_level: restricted
source_repo: mukul975/Anthropic-Cybersecurity-Skills
triggers:

---

# Automating Ioc Enrichment

## Description
Automates the enrichment of raw indicators of compromise with multi-source threat intelligence context using SOAR platforms, Python pipelines, or TIP playbooks to reduce analyst triage time and standardize enrichment outputs. Use when building automated enrichment workflows integrated with SIEM alerts, email submission pipelines, or bulk IOC processing from threat feeds. Activates for requests involving SOAR enrichment, Cortex XSOAR, Splunk SOAR, TheHive, Python enrichment pipelines, or automated IOC processing.


## Acuterium Integration
- **Thread:** T06 — EDNA
- **Shard:** Edna-SIGINT
- **Layers:** L7, L8, L9
- **Governance:** restricted
- **Sovereignty Score:** 9/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/automating-ioc-enrichment/SKILL.md
- **Author:** cybersecurity-community
