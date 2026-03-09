---
name: pubmed-database
display_name: Pubmed Database
skill_id: ACU-SKILL-0920
version: 1.0.0
category: coding
thread: T04
domain: cognitive
shard_affinity:
  - AcuTect-CODEX
layer_access:
  - L5
  - L6
  - L7
  - L8
sovereignty_score: 10
governance_level: mandatory
source_repo: sickn33/antigravity-awesome-skills
triggers:
  - uncategorized
---

# Pubmed Database

## Description
Direct REST API access to PubMed. Advanced Boolean/MeSH queries, E-utilities API, batch processing, citation management. For Python workflows, prefer biopython (Bio.Entrez). Use this for direct HTTP/REST work or custom API implementations.

## Acuterium Integration
- **Thread:** T04 — ACIW
- **Shard:** AcuTect-CODEX
- **Layers:** L5, L6, L7, L8
- **Governance:** mandatory
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** sickn33/antigravity-awesome-skills
- **File:** skills/pubmed-database
- **Author:** antigravity-community
