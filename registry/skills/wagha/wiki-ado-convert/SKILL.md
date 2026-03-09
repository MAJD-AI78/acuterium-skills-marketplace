---
name: wiki-ado-convert
display_name: Wiki Ado Convert
skill_id: ACU-SKILL-2168
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

# Wiki Ado Convert

## Description
Converts VitePress/GFM wiki markdown to Azure DevOps Wiki-compatible format. Generates a Node.js build script that transforms Mermaid syntax, strips front matter, fixes links, and outputs ADO-compatible copies to dist/ado-wiki/.

## Acuterium Integration
- **Thread:** T13 — ACAI V2
- **Shard:** Marel
- **Layers:** L5, L6, L7
- **Governance:** restricted
- **Sovereignty Score:** 8/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** microsoft/skills
- **File:** .github/plugins/deep-wiki/skills/wiki-ado-convert/SKILL.md
- **Author:** Microsoft
