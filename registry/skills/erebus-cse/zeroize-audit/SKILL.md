---
name: zeroize-audit
display_name: Zeroize Audit
skill_id: ACU-SKILL-1237
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

# Zeroize Audit

## Description
Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow verification. Use for auditing C/C++/Rust code handling secrets, keys, passwords, or other sensitive data.

## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** sickn33/antigravity-awesome-skills
- **File:** skills/zeroize-audit
- **Author:** antigravity-community
