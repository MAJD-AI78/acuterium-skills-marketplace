---
name: bankr-signals
display_name: Bankr Signals
skill_id: ACU-SKILL-2174
version: 1.0.0
category: cloud-aws
thread: T13
domain: infrastructure
shard_affinity:
  - Marel
layer_access:
  - L5
  - L6
  - L7
sovereignty_score: 8
governance_level: restricted
source_repo: BankrBot/skills
triggers:

---

# Bankr Signals

## Description
Transaction-verified trading signals on Base. Register agent as signal provider, publish trades with TX hash proof, consume signals from top performers via REST API. All track records verified against blockchain data. No fake performance claims. Triggers on: "publish signal", "post trade signal", "register provider", "subscribe to signals", "copy trade", "bankr signals", "signal feed", "trading leaderboard", "read signals", "get top traders".

## Acuterium Integration
- **Thread:** T13 — ACAI V2
- **Shard:** Marel
- **Layers:** L5, L6, L7
- **Governance:** restricted
- **Sovereignty Score:** 8/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** BankrBot/skills
- **File:** bankr-signals/SKILL.md
- **Author:** BankrBot
