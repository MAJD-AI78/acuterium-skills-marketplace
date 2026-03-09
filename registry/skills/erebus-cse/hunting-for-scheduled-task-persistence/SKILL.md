---
name: hunting-for-scheduled-task-persistence
display_name: Hunting For Scheduled Task Persistence
skill_id: ACU-SKILL-1495
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
source_repo: mukul975/Anthropic-Cybersecurity-Skills
triggers:

---

# Hunting For Scheduled Task Persistence

## Description
Hunt for adversary persistence via Windows Scheduled Tasks by analyzing task creation events, suspicious task actions, and unusual scheduling patterns.

## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/hunting-for-scheduled-task-persistence/SKILL.md
- **Author:** cybersecurity-community
