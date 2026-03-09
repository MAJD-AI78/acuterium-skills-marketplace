---
name: detecting-modbus-command-injection-attacks
display_name: Detecting Modbus Command Injection Attacks
skill_id: ACU-SKILL-1415
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

# Detecting Modbus Command Injection Attacks

## Description
Detect command injection attacks against Modbus TCP/RTU protocol in ICS environments by monitoring for unauthorized write operations, anomalous function codes, malformed frames, and deviations from established communication baselines using ICS-aware IDS and protocol deep packet inspection.


## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/detecting-modbus-command-injection-attacks/SKILL.md
- **Author:** cybersecurity-community
