---
name: azure-validate
display_name: Azure Validate
skill_id: ACU-SKILL-2160
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

# Azure Validate

## Description
Pre-deployment validation checkpoint. Run deep checks to ensure your application is ready for Azure deployment. Validates configuration, infrastructure, permissions, and prerequisites.
USE FOR: validate my app, check deployment readiness, run preflight checks, verify configuration, check if ready to deploy, validate azure.yaml, validate Bicep, test before deploying, troubleshoot deployment errors.
DO NOT USE FOR: creating or building apps (use azure-prepare), executing deployments (use azure-deploy).

## Acuterium Integration
- **Thread:** T13 — ACAI V2
- **Shard:** Marel
- **Layers:** L5, L6, L7
- **Governance:** restricted
- **Sovereignty Score:** 8/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** microsoft/skills
- **File:** .github/plugins/azure-skills/skills/azure-validate/SKILL.md
- **Author:** Microsoft
