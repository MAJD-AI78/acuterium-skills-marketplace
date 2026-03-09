---
name: executing-diamond-model-analysis
display_name: Executing Diamond Model Analysis
skill_id: ACU-SKILL-1440
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

# Executing Diamond Model Analysis

## Description
Applies the Diamond Model of Intrusion Analysis to structure adversary activity into its four core vertices (adversary, capability, infrastructure, victim) and identifies relationships between them to pivot investigations and attribute campaigns. Use when analyzing a completed intrusion, linking disparate incidents to a common threat actor, or building structured analytic products for threat intelligence dissemination. Activates for requests involving Diamond Model, intrusion analysis, campaign clustering, or adversary attribution methodology.


## Acuterium Integration
- **Thread:** T06 — EDNA
- **Shard:** Edna-SIGINT
- **Layers:** L7, L8, L9
- **Governance:** restricted
- **Sovereignty Score:** 9/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/executing-diamond-model-analysis/SKILL.md
- **Author:** cybersecurity-community
