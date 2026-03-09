---
name: detecting-golden-ticket-attacks-in-kerberos-logs
display_name: Detecting Golden Ticket Attacks In Kerberos Logs
skill_id: ACU-SKILL-1407
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

# Detecting Golden Ticket Attacks In Kerberos Logs

## Description
Detect Golden Ticket attacks in Active Directory by analyzing Kerberos TGT anomalies including mismatched encryption types, impossible ticket lifetimes, non-existent accounts, and forged PAC signatures in domain controller event logs.

## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/detecting-golden-ticket-attacks-in-kerberos-logs/SKILL.md
- **Author:** cybersecurity-community
