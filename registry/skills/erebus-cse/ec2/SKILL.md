---
name: ec2
display_name: Ec2
skill_id: ACU-SKILL-2038
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
source_repo: itsmostafa/aws-agent-skills
triggers:

---

# Ec2

## Description
AWS EC2 virtual machine management for instances, AMIs, and networking. Use when launching instances, configuring security groups, managing key pairs, troubleshooting connectivity, or automating instance lifecycle.

## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** itsmostafa/aws-agent-skills
- **File:** skills/ec2/SKILL.md
- **Author:** itsmostafa/aws-agent-skills
