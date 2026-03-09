---
name: azure-diagnostics
display_name: Azure Diagnostics
skill_id: ACU-SKILL-2151
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

# Azure Diagnostics

## Description
Debug and troubleshoot production issues on Azure. Covers Container Apps diagnostics, log analysis with KQL, health checks, and common issue resolution for image pulls, cold starts, and health probes.
USE FOR: debug production issues, troubleshoot container apps, analyze logs with KQL, fix image pull failures, resolve cold start issues, investigate health probe failures, check resource health, view application logs, find root cause of errors
DO NOT USE FOR: deploying applications (use azure-deploy), creating new resources (use azure-prepare), setting up monitoring (use azure-observability), cost optimization (use azure-cost-optimization)

## Acuterium Integration
- **Thread:** T13 — ACAI V2
- **Shard:** Marel
- **Layers:** L5, L6, L7
- **Governance:** restricted
- **Sovereignty Score:** 8/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** microsoft/skills
- **File:** .github/plugins/azure-skills/skills/azure-diagnostics/SKILL.md
- **Author:** Microsoft
