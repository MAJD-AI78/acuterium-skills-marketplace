---
name: clanker
display_name: Clanker
skill_id: ACU-SKILL-2177
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

# Clanker

## Description
Deploy ERC20 tokens on Base, Ethereum, Arbitrum, and other EVM chains using the Clanker SDK. Use when the user wants to deploy a new token, create a memecoin, set up token vesting, configure airdrops, manage token rewards, claim LP fees, or update token metadata. Supports V4 deployment with vaults, airdrops, dev buys, custom market caps, vanity addresses, and multi-chain deployment.

## Acuterium Integration
- **Thread:** T13 — ACAI V2
- **Shard:** Marel
- **Layers:** L5, L6, L7
- **Governance:** restricted
- **Sovereignty Score:** 8/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** BankrBot/skills
- **File:** clanker/SKILL.md
- **Author:** BankrBot
