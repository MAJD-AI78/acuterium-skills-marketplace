---
name: agents-sdk
display_name: Agents Sdk
skill_id: ACU-SKILL-2051
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
source_repo: cloudflare/skills
triggers:

---

# Agents Sdk

## Description
Build AI agents on Cloudflare Workers using the Agents SDK. Load when creating stateful agents, durable workflows, real-time WebSocket apps, scheduled tasks, MCP servers, or chat applications. Covers Agent class, state management, callable RPC, Workflows integration, and React hooks. Biases towards retrieval from Cloudflare docs over pre-trained knowledge.

## Acuterium Integration
- **Thread:** T13 — ACAI V2
- **Shard:** Marel
- **Layers:** L5, L6, L7
- **Governance:** restricted
- **Sovereignty Score:** 8/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** cloudflare/skills
- **File:** skills/agents-sdk/SKILL.md
- **Author:** cloudflare/skills
