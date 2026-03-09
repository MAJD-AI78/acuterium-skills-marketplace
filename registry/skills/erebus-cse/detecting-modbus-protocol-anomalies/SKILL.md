---
name: detecting-modbus-protocol-anomalies
display_name: Detecting Modbus Protocol Anomalies
skill_id: ACU-SKILL-1416
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

# Detecting Modbus Protocol Anomalies

## Description
This skill covers detecting anomalies in Modbus/TCP and Modbus RTU communications in industrial control systems. It addresses function code monitoring, register range validation, timing analysis, unauthorized client detection, and deep packet inspection for malformed Modbus frames. The skill leverages Zeek with Modbus protocol analyzers, Suricata IDS with OT rules, and custom Python-based detection using Markov chain models for normal Modbus transaction sequences.


## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/detecting-modbus-protocol-anomalies/SKILL.md
- **Author:** cybersecurity-community
