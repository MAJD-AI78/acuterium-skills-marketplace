---
name: azure-deploy
display_name: Azure Deploy
skill_id: ACU-SKILL-2150
version: 1.0.0
category: cloud-azure
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
source_repo: microsoft/skills
triggers:

---

# Azure Deploy

## Description
Execute deployment to Azure. Final step after preparation and validation. Runs azd up, azd deploy, or infrastructure provisioning commands.
USE FOR: run azd up, run azd deploy, execute deployment, provision infrastructure, push to production, go live, ship it, deploy web app, deploy container app, deploy static site, deploy Azure Functions, bicep deploy, terraform apply.
DO NOT USE FOR: creating or building apps (use azure-prepare), validating before deploy (use azure-validate).

## Acuterium Integration
- **Thread:** T13 — ACAI V2
- **Shard:** Marel
- **Layers:** L5, L6, L7
- **Governance:** restricted
- **Sovereignty Score:** 8/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** microsoft/skills
- **File:** .github/plugins/azure-skills/skills/azure-deploy/SKILL.md
- **Author:** Microsoft
