---
name: sns
display_name: Sns
skill_id: ACU-SKILL-2047
version: 1.0.0
category: cloud-aws
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
source_repo: itsmostafa/aws-agent-skills
triggers:

---

# Sns

## Description
AWS SNS notification service for pub/sub messaging. Use when creating topics, managing subscriptions, configuring message filtering, sending notifications, or setting up mobile push.

## Acuterium Integration
- **Thread:** T13 — ACAI V2
- **Shard:** Marel
- **Layers:** L5, L6, L7
- **Governance:** restricted
- **Sovereignty Score:** 8/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** itsmostafa/aws-agent-skills
- **File:** skills/sns/SKILL.md
- **Author:** itsmostafa/aws-agent-skills
