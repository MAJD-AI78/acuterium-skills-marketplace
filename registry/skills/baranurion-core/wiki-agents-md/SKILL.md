---
name: wiki-agents-md
display_name: Wiki Agents Md
skill_id: ACU-SKILL-2169
version: 1.0.0
category: agent-patterns
thread: T01
domain: cognitive
shard_affinity:
  - Diaran-MOE
layer_access:
  - L5
  - L6
  - L7
  - L8
sovereignty_score: 10
governance_level: mandatory
source_repo: microsoft/skills
triggers:

---

# Wiki Agents Md

## Description
Generates AGENTS.md files for repository folders — coding agent context files with build commands, testing instructions, code style, project structure, and boundaries. Only generates where AGENTS.md is missing.

## Acuterium Integration
- **Thread:** T01 — COSM
- **Shard:** Diaran-MOE
- **Layers:** L5, L6, L7, L8
- **Governance:** mandatory
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** microsoft/skills
- **File:** .github/plugins/deep-wiki/skills/wiki-agents-md/SKILL.md
- **Author:** Microsoft
