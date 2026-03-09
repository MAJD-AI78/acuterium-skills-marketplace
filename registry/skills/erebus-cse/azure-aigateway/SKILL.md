---
name: azure-aigateway
display_name: Azure Aigateway
skill_id: ACU-SKILL-2147
version: 1.0.0
category: content-safety
thread: T08
domain: security
shard_affinity:
  - EREBUS-CSE
layer_access:
  - L8
  - L9
  - L10
sovereignty_score: 10
governance_level: mandatory
source_repo: microsoft/skills
triggers:

---

# Azure Aigateway

## Description
Configure Azure API Management (APIM) as AI Gateway to secure, observe, control AI models, MCP servers, agents. Helps with rate limiting, semantic caching, content safety, load balancing.
USE FOR: AI Gateway, APIM, setup gateway, configure gateway, add gateway, model gateway, MCP server, rate limit, token limit, semantic cache, content safety, load balance, OpenAPI import, convert API to MCP.
DO NOT USE FOR: deploy models (use microsoft-foundry), Azure Functions (use azure-functions), databases (use azure-postgres).

## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** EREBUS-CSE
- **Layers:** L8, L9, L10
- **Governance:** mandatory
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** microsoft/skills
- **File:** .github/plugins/azure-skills/skills/azure-aigateway/SKILL.md
- **Author:** Microsoft
