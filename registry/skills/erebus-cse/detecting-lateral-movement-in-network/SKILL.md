---
name: detecting-lateral-movement-in-network
display_name: Detecting Lateral Movement In Network
skill_id: ACU-SKILL-1410
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

# Detecting Lateral Movement In Network

## Description
Identifies lateral movement techniques in enterprise networks by analyzing authentication logs, network flows, SMB traffic, and RDP sessions using Zeek, Velociraptor, and SIEM correlation rules to detect attackers moving between systems.


## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/detecting-lateral-movement-in-network/SKILL.md
- **Author:** cybersecurity-community
