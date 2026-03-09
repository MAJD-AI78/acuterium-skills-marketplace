---
name: hunting-advanced-persistent-threats
display_name: Hunting Advanced Persistent Threats
skill_id: ACU-SKILL-1484
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

# Hunting Advanced Persistent Threats

## Description
Proactively hunts for Advanced Persistent Threat (APT) activity within enterprise environments using hypothesis-driven searches across endpoint telemetry, network logs, and memory artifacts. Use when conducting scheduled threat hunting cycles, investigating anomalous behavior flagged by UEBA, or validating that known APT TTPs are not present in the environment. Activates for requests involving MITRE ATT&CK, Velociraptor, osquery, Zeek, or threat hunting playbooks.


## Acuterium Integration
- **Thread:** T06 — EDNA
- **Shard:** Edna-SIGINT
- **Layers:** L7, L8, L9
- **Governance:** restricted
- **Sovereignty Score:** 9/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/hunting-advanced-persistent-threats/SKILL.md
- **Author:** cybersecurity-community
