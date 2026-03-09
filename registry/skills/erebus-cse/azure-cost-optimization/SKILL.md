---
name: azure-cost-optimization
display_name: Azure Cost Optimization
skill_id: ACU-SKILL-2149
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

# Azure Cost Optimization

## Description
Identify and quantify cost savings across Azure subscriptions by analyzing actual costs,
utilization metrics, and generating actionable optimization recommendations. USE FOR:
optimize Azure costs, reduce Azure spending, reduce Azure expenses, analyze Azure costs,
find cost savings, generate cost optimization report, find orphaned resources, rightsize VMs,
cost analysis, reduce waste, Azure spending analysis, find unused resources, optimize Redis
costs. DO NOT USE FOR: deploying resources (use azure-deploy), general Azure diagnostics
(use azure-diagnostics), security issues (use azure-security)

## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** microsoft/skills
- **File:** .github/plugins/azure-skills/skills/azure-cost-optimization/SKILL.md
- **Author:** Microsoft
