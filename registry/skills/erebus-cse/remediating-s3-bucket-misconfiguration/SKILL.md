---
name: remediating-s3-bucket-misconfiguration
display_name: Remediating S3 Bucket Misconfiguration
skill_id: ACU-SKILL-1766
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

# Remediating S3 Bucket Misconfiguration

## Description
This skill provides step-by-step procedures for identifying and remediating Amazon S3 bucket misconfigurations that expose sensitive data to unauthorized access. It covers enabling S3 Block Public Access at account and bucket levels, auditing bucket policies and ACLs, enforcing encryption, configuring access logging, and deploying automated remediation using AWS Config and Lambda.


## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/remediating-s3-bucket-misconfiguration/SKILL.md
- **Author:** cybersecurity-community
