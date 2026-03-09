---
name: building-mcp-server-on-cloudflare
display_name: Building Mcp Server On Cloudflare
skill_id: ACU-SKILL-2053
version: 1.0.0
category: auth
thread: T09
domain: security
shard_affinity:
  - Q-ENC
layer_access:
  - L8
  - L9
  - L10
sovereignty_score: 10
governance_level: sovereign
source_repo: cloudflare/skills
triggers:

---

# Building Mcp Server On Cloudflare

## Description
Builds remote MCP (Model Context Protocol) servers on Cloudflare Workers
with tools, OAuth authentication, and production deployment. Generates
server code, configures auth providers, and deploys to Workers.

Use when: user wants to "build MCP server", "create MCP tools", "remote
MCP", "deploy MCP", add "OAuth to MCP", or mentions Model Context Protocol
on Cloudflare. Also triggers on "MCP authentication" or "MCP deployment".
Biases towards retrieval from Cloudflare docs over pre-trained knowledge.


## Acuterium Integration
- **Thread:** T09 — Q-Suite
- **Shard:** Q-ENC
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** cloudflare/skills
- **File:** skills/building-mcp-server-on-cloudflare/SKILL.md
- **Author:** cloudflare/skills
