---
name: client-deliverables
display_name: Client Deliverables
skill_id: ACU-SKILL-2069
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
source_repo: andersoncollab/design-agent
triggers:

---

# Client Deliverables

## Description
You are the output layer for design systems and client work. This workflow orchestrates all other design-agent skills to produce professional, branded deliverables that tell a story: Problem → Analysis → Recommendation → Next Steps. Instead of dumping raw design data, you package design work into three key formats: **structured markdown** (for hosting as web pages), **PDF exports** (for email/archival), and **XLSX reports** (for metrics-driven clients). Each deliverable follows Anderson Collabor

## Acuterium Integration
- **Thread:** T01 — COSM
- **Shard:** Diaran-MOE
- **Layers:** L5, L6, L7, L8
- **Governance:** mandatory
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** andersoncollab/design-agent
- **File:** skills/client-deliverables/SKILL.md
- **Author:** andersoncollab
