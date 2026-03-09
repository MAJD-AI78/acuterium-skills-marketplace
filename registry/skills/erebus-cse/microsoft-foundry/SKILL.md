---
name: microsoft-foundry
display_name: Microsoft Foundry
skill_id: ACU-SKILL-2162
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
source_repo: microsoft/skills
triggers:

---

# Microsoft Foundry

## Description
Use this skill to work with Microsoft Foundry (Azure AI Foundry): deploy AI models from catalog, build RAG applications with knowledge indexes, create and evaluate AI agents, manage RBAC permissions and role assignments, manage quotas and capacity, create Foundry resources.
USE FOR: Microsoft Foundry, AI Foundry, deploy model, model catalog, RAG, knowledge index, create agent, evaluate agent, agent monitoring, create Foundry project, new Foundry project, set up Foundry, onboard to Foundry, provision Foundry infrastructure, create Foundry resource, create AI Services, multi-service resource, AIServices kind, register resource provider, enable Cognitive Services, setup AI Services account, create resource group for Foundry, RBAC, role assignment, managed identity, service principal, permissions, quota, capacity, TPM, deployment failure, QuotaExceeded.
DO NOT USE FOR: Azure Functions (use azure-functions), App Service (use azure-create-app), generic Azure resource creation (use azure-create-app).

## Acuterium Integration
- **Thread:** T09 — Q-Suite
- **Shard:** Q-ENC
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** microsoft/skills
- **File:** .github/plugins/azure-skills/skills/microsoft-foundry/SKILL.md
- **Author:** Microsoft
