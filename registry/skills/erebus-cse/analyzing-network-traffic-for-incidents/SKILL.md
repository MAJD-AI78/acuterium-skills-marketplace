---
name: analyzing-network-traffic-for-incidents
display_name: Analyzing Network Traffic For Incidents
skill_id: ACU-SKILL-1269
version: 1.0.0
category: forensics
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

# Analyzing Network Traffic For Incidents

## Description
Analyzes network traffic captures and flow data to identify adversary activity during security incidents, including command-and-control communications, lateral movement, data exfiltration, and exploitation attempts. Uses Wireshark, Zeek, and NetFlow analysis techniques. Activates for requests involving network traffic analysis, packet capture investigation, PCAP analysis, network forensics, C2 traffic detection, or exfiltration detection.


## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/analyzing-network-traffic-for-incidents/SKILL.md
- **Author:** cybersecurity-community
