---
name: azure-resource-visualizer
display_name: Azure Resource Visualizer
skill_id: ACU-SKILL-2158
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

# Azure Resource Visualizer

## Description
Analyze Azure resource groups and generate detailed Mermaid architecture diagrams showing the relationships between individual resources.
USE FOR: create architecture diagram, visualize Azure resources, show resource relationships, generate Mermaid diagram, analyze resource group, diagram my resources, architecture visualization, resource topology, map Azure infrastructure
DO NOT USE FOR: creating/modifying resources (use azure-deploy), security scanning (use azure-security), performance troubleshooting (use azure-diagnostics), code generation (use relevant service skill)

## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** microsoft/skills
- **File:** .github/plugins/azure-skills/skills/azure-resource-visualizer/SKILL.md
- **Author:** Microsoft
