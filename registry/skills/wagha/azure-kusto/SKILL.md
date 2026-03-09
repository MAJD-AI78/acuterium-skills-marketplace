---
name: azure-kusto
display_name: Azure Kusto
skill_id: ACU-SKILL-2152
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

# Azure Kusto

## Description
Query and analyze data in Azure Data Explorer (Kusto/ADX) using KQL for log analytics, telemetry, and time series analysis.
USE FOR: KQL queries, Kusto database queries, Azure Data Explorer, ADX clusters, log analytics, time series data, IoT telemetry, anomaly detection
DO NOT USE FOR: SQL databases (use azure-postgres), NoSQL queries (use azure-storage), Elasticsearch, AWS analytics tools

## Acuterium Integration
- **Thread:** T13 — ACAI V2
- **Shard:** Marel
- **Layers:** L5, L6, L7
- **Governance:** restricted
- **Sovereignty Score:** 8/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** microsoft/skills
- **File:** .github/plugins/azure-skills/skills/azure-kusto/SKILL.md
- **Author:** Microsoft
