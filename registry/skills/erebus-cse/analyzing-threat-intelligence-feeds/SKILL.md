---
name: analyzing-threat-intelligence-feeds
display_name: Analyzing Threat Intelligence Feeds
skill_id: ACU-SKILL-1282
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

# Analyzing Threat Intelligence Feeds

## Description
Analyzes structured and unstructured threat intelligence feeds to extract actionable indicators, adversary tactics, and campaign context. Use when ingesting commercial or open-source CTI feeds, evaluating feed quality, normalizing data into STIX 2.1 format, or enriching existing IOCs with campaign attribution. Activates for requests involving ThreatConnect, Recorded Future, Mandiant Advantage, MISP, AlienVault OTX, or automated feed aggregation pipelines.


## Acuterium Integration
- **Thread:** T06 — EDNA
- **Shard:** Edna-SIGINT
- **Layers:** L7, L8, L9
- **Governance:** restricted
- **Sovereignty Score:** 9/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/analyzing-threat-intelligence-feeds/SKILL.md
- **Author:** cybersecurity-community
