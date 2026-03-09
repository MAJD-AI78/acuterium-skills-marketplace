---
name: profiling-threat-actor-groups
display_name: Profiling Threat Actor Groups
skill_id: ACU-SKILL-1763
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

# Profiling Threat Actor Groups

## Description
Develops comprehensive threat actor profiles for APT groups, criminal organizations, and hacktivist collectives by aggregating TTP documentation, historical campaign data, tooling fingerprints, and attribution indicators from multiple intelligence sources. Use when briefing executives on sector-specific threats, updating threat model assumptions, or prioritizing defensive controls against specific adversaries. Activates for requests involving MITRE ATT&CK Groups, Mandiant APT profiles, CrowdStrike adversary naming, or sector-specific threat briefings.


## Acuterium Integration
- **Thread:** T06 — EDNA
- **Shard:** Edna-SIGINT
- **Layers:** L7, L8, L9
- **Governance:** restricted
- **Sovereignty Score:** 9/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/profiling-threat-actor-groups/SKILL.md
- **Author:** cybersecurity-community
