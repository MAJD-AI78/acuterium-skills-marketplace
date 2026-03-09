---
name: shodan-reconnaissance
display_name: Shodan Reconnaissance
skill_id: ACU-SKILL-1026
version: 1.0.0
category: search
thread: T02
domain: cognitive
shard_affinity:
  - APMS
layer_access:
  - L4
  - L5
  - L6
sovereignty_score: 9
governance_level: restricted
source_repo: sickn33/antigravity-awesome-skills
triggers:
  - uncategorized
---

# Shodan Reconnaissance

## Description
This skill should be used when the user asks to "search for exposed devices on the internet," "perform Shodan reconnaissance," "find vulnerable services using Shodan," "scan IP ranges...

## Acuterium Integration
- **Thread:** T02 — DIAR
- **Shard:** APMS
- **Layers:** L4, L5, L6
- **Governance:** restricted
- **Sovereignty Score:** 9/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** sickn33/antigravity-awesome-skills
- **File:** skills/shodan-reconnaissance
- **Author:** antigravity-community
