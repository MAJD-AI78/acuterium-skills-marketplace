---
name: dashboard-patterns
display_name: Dashboard Patterns
skill_id: ACU-SKILL-2074
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
source_repo: andersoncollab/design-agent
triggers:

---

# Dashboard Patterns

## Description
This skill provides production-ready layouts and component patterns for dashboards, admin panels, analytics interfaces, and data-heavy applications. Dashboards require special handling: progressive data loading (skeleton states), empty states (no data yet), error states (API failed), and chart selection (pick the right visualization). The skill covers information architecture (hierarchy), chart selection guide (which visualization for which data), component patterns (KPI cards, data tables, filt

## Acuterium Integration
- **Thread:** T13 — ACAI V2
- **Shard:** Marel
- **Layers:** L5, L6, L7
- **Governance:** restricted
- **Sovereignty Score:** 8/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** andersoncollab/design-agent
- **File:** skills/dashboard-patterns/SKILL.md
- **Author:** andersoncollab
