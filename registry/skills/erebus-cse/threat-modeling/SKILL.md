---
name: threat-modeling
display_name: Threat Modeling
skill_id: ACU-SKILL-2135
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
source_repo: Poatan222/Skills-security
triggers:

---

# Threat Modeling

## Description
Generate STRIDE-based threat models from architecture descriptions, diagrams, or design documents. Produces a structured threat register with risk ratings, mitigations, and data flow analysis. Trigger when user mentions "threat model", "STRIDE", "attack surface", "security review", "design review", "architecture review", "threat assessment", or uploads architecture diagrams, system design docs, or data flow diagrams. Also trigger when user describes a new feature or system and asks about security implications.


## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** Poatan222/Skills-security
- **File:** threat-modeling/SKILL.md
- **Author:** Poatan222/Skills-security
