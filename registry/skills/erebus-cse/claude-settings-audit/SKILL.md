---
name: claude-settings-audit
display_name: Claude Settings Audit
skill_id: ACU-SKILL-0323
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
source_repo: sickn33/antigravity-awesome-skills
triggers:
  - uncategorized
---

# Claude Settings Audit

## Description
Analyze a repository to generate recommended Claude Code settings.json permissions. Use when setting up a new project, auditing existing settings, or determining which read-only bash commands to allow. Detects tech stack, build tools, and monorepo structure.

## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** sickn33/antigravity-awesome-skills
- **File:** skills/claude-settings-audit
- **Author:** antigravity-community
