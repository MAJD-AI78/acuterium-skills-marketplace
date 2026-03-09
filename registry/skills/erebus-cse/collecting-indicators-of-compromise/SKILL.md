---
name: collecting-indicators-of-compromise
display_name: Collecting Indicators Of Compromise
skill_id: ACU-SKILL-1329
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

# Collecting Indicators Of Compromise

## Description
Systematically collects, categorizes, and distributes indicators of compromise (IOCs) during and after security incidents to enable detection, blocking, and threat intelligence sharing. Covers network, host, email, and behavioral indicators using STIX/TAXII formats and threat intelligence platforms. Activates for requests involving IOC collection, indicator extraction, threat indicator sharing, compromise indicators, STIX export, or IOC enrichment.


## Acuterium Integration
- **Thread:** T06 — EDNA
- **Shard:** Edna-SIGINT
- **Layers:** L7, L8, L9
- **Governance:** restricted
- **Sovereignty Score:** 9/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/collecting-indicators-of-compromise/SKILL.md
- **Author:** cybersecurity-community
