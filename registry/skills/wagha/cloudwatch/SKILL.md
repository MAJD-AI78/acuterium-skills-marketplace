---
name: cloudwatch
display_name: Cloudwatch
skill_id: ACU-SKILL-2035
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

# Cloudwatch

## Description
AWS CloudWatch monitoring for logs, metrics, alarms, and dashboards. Use when setting up monitoring, creating alarms, querying logs with Insights, configuring metric filters, building dashboards, or troubleshooting application issues.

## Acuterium Integration
- **Thread:** T13 — ACAI V2
- **Shard:** Marel
- **Layers:** L5, L6, L7
- **Governance:** restricted
- **Sovereignty Score:** 8/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** itsmostafa/aws-agent-skills
- **File:** skills/cloudwatch/SKILL.md
- **Author:** itsmostafa/aws-agent-skills
