---
name: hunting-for-persistence-via-wmi-subscriptions
display_name: Hunting For Persistence Via Wmi Subscriptions
skill_id: ACU-SKILL-1493
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

# Hunting For Persistence Via Wmi Subscriptions

## Description
Hunt for adversary persistence through Windows Management Instrumentation event subscriptions by monitoring WMI consumer, filter, and binding creation events that execute malicious code triggered by system events.

## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/hunting-for-persistence-via-wmi-subscriptions/SKILL.md
- **Author:** cybersecurity-community
