---
name: azure-rbac
display_name: Azure Rbac
skill_id: ACU-SKILL-2156
version: 1.0.0
category: security
thread: T08
domain: security
shard_affinity:
  - Tenebris-ACIWS
layer_access:
  - L8
  - L9
  - L10
sovereignty_score: 10
governance_level: sovereign
source_repo: microsoft/skills
triggers:

---

# Azure Rbac

## Description
Helps users find the right Azure RBAC role for an identity with least privilege access, then generate CLI commands and Bicep code to assign it.
USE FOR: "what role should I assign", "least privilege role", "RBAC role for", "role to read blobs", "role for managed identity", "custom role definition", "assign role to identity".
DO NOT USE FOR: creating or configuring managed identities, or general Azure security hardening; those are out of scope for this role-selection skill.

## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** microsoft/skills
- **File:** .github/plugins/azure-skills/skills/azure-rbac/SKILL.md
- **Author:** Microsoft
