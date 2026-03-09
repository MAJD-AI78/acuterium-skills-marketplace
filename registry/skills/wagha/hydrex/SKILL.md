---
name: hydrex
display_name: Hydrex
skill_id: ACU-SKILL-2181
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

# Hydrex

## Description
Interact with Hydrex liquidity pools on Base. Use when the user wants to lock HYDX for voting power, check voting power for gauge voting, vote on liquidity pool strategies, view pool information, check voting weights, participate in Hydrex governance, deposit single-sided liquidity into auto-managed vaults to earn Hydrex yields, claim oHYDX rewards from incentive campaigns, or exercise oHYDX into veHYDX. Uses Bankr for transaction execution.

## Acuterium Integration
- **Thread:** T13 — ACAI V2
- **Shard:** Marel
- **Layers:** L5, L6, L7
- **Governance:** restricted
- **Sovereignty Score:** 8/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** BankrBot/skills
- **File:** hydrex/SKILL.md
- **Author:** BankrBot
