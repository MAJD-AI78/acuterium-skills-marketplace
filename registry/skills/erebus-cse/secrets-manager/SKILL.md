---
name: secrets-manager
display_name: Secrets Manager
skill_id: ACU-SKILL-2046
version: 1.0.0
category: auth
thread: T09
domain: security
shard_affinity:
  - Q-ENC
layer_access:
  - L8
  - L9
  - L10
sovereignty_score: 10
governance_level: sovereign
source_repo: itsmostafa/aws-agent-skills
triggers:

---

# Secrets Manager

## Description
AWS Secrets Manager for secure secret storage and rotation. Use when storing credentials, configuring automatic rotation, managing secret versions, retrieving secrets in applications, or integrating with RDS.

## Acuterium Integration
- **Thread:** T09 — Q-Suite
- **Shard:** Q-ENC
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** itsmostafa/aws-agent-skills
- **File:** skills/secrets-manager/SKILL.md
- **Author:** itsmostafa/aws-agent-skills
