---
name: find-skills
display_name: Find Skills
skill_id: ACU-SKILL-2050
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
source_repo: vercel-labs/skills
triggers:

---

# Find Skills

## Description
Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extending capabilities. This skill should be used when the user is looking for functionality that might exist as an installable skill.

## Acuterium Integration
- **Thread:** T01 — COSM
- **Shard:** Diaran-MOE
- **Layers:** L5, L6, L7, L8
- **Governance:** mandatory
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** vercel-labs/skills
- **File:** skills/find-skills/SKILL.md
- **Author:** vercel-labs/skills
