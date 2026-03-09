---
name: detecting-evasion-techniques-in-endpoint-logs
display_name: Detecting Evasion Techniques In Endpoint Logs
skill_id: ACU-SKILL-1404
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

# Detecting Evasion Techniques In Endpoint Logs

## Description
Detects defense evasion techniques used by adversaries in endpoint logs including log tampering, timestomping, process injection, and security tool disabling. Use when investigating suspicious endpoint behavior, building detection rules for evasion tactics, or conducting threat hunting for stealthy adversary activity. Activates for requests involving evasion detection, defense evasion analysis, log tampering detection, or MITRE ATT&CK TA0005.


## Acuterium Integration
- **Thread:** T06 — EDNA
- **Shard:** Edna-SIGINT
- **Layers:** L7, L8, L9
- **Governance:** restricted
- **Sovereignty Score:** 9/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/detecting-evasion-techniques-in-endpoint-logs/SKILL.md
- **Author:** cybersecurity-community
