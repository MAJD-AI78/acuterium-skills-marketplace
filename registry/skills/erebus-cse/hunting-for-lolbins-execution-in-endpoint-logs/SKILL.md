---
name: hunting-for-lolbins-execution-in-endpoint-logs
display_name: Hunting For Lolbins Execution In Endpoint Logs
skill_id: ACU-SKILL-1491
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

# Hunting For Lolbins Execution In Endpoint Logs

## Description
Hunt for adversary abuse of Living Off the Land Binaries (LOLBins) by analyzing endpoint process creation logs for suspicious execution patterns of legitimate Windows system binaries used for malicious purposes.

## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/hunting-for-lolbins-execution-in-endpoint-logs/SKILL.md
- **Author:** cybersecurity-community
