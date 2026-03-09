---
name: azure-postgres
display_name: Azure Postgres
skill_id: ACU-SKILL-2154
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

# Azure Postgres

## Description
Create new Azure Database for PostgreSQL Flexible Server instances and configure passwordless authentication with Microsoft Entra ID. Set up developer access, managed identities for apps, group-based permissions, and migrate from password-based to Entra ID authentication. Trigger phrases include "passwordless for postgres", "entra id postgres", "azure ad postgres authentication", "postgres managed identity", "migrate postgres to passwordless".

## Acuterium Integration
- **Thread:** T09 — Q-Suite
- **Shard:** Q-ENC
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** microsoft/skills
- **File:** .github/plugins/azure-skills/skills/azure-postgres/SKILL.md
- **Author:** Microsoft
