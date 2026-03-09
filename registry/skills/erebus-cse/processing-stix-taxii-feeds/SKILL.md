---
name: processing-stix-taxii-feeds
display_name: Processing Stix Taxii Feeds
skill_id: ACU-SKILL-1762
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

# Processing Stix Taxii Feeds

## Description
Processes STIX 2.1 threat intelligence bundles delivered via TAXII 2.1 servers, normalizing objects into platform-native schemas and routing them to appropriate consuming systems. Use when onboarding new TAXII collection endpoints, automating bi-directional intelligence sharing with ISACs, or building pipeline validation for malformed STIX bundles. Activates for requests involving OASIS STIX, TAXII server configuration, MISP TAXII, or Cortex XSOAR feed integrations.


## Acuterium Integration
- **Thread:** T06 — EDNA
- **Shard:** Edna-SIGINT
- **Layers:** L7, L8, L9
- **Governance:** restricted
- **Sovereignty Score:** 9/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/processing-stix-taxii-feeds/SKILL.md
- **Author:** cybersecurity-community
