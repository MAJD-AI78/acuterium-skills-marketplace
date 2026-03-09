---
name: visual-audit
display_name: Visual Audit
skill_id: ACU-SKILL-2105
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
source_repo: andersoncollab/design-agent
triggers:

---

# Visual Audit

## Description
A visual audit systematically evaluates design quality across seven critical dimensions: typography, color, spacing, layout, components, motion, and accessibility. The audit uses a scoring framework (Design Feasibility & Impact Index — DFII from Anthropic's frontend-design skill) to quantify improvements and prioritize fixes. Output: scored report with specific issues, impact levels, and quick wins.

## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** andersoncollab/design-agent
- **File:** skills/visual-audit/SKILL.md
- **Author:** andersoncollab
