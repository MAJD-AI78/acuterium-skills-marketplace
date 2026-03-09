---
name: uniprot-database
display_name: Uniprot Database
skill_id: ACU-SKILL-1156
version: 1.0.0
category: testing
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

# Uniprot Database

## Description
Direct REST API access to UniProt. Protein searches, FASTA retrieval, ID mapping, Swiss-Prot/TrEMBL. For Python workflows with multiple databases, prefer bioservices (unified interface to 40+ services). Use this for direct HTTP/REST work or UniProt-specific control.

## Acuterium Integration
- **Thread:** T04 — ACIW
- **Shard:** AcuTect-CODEX
- **Layers:** L5, L6, L7, L8
- **Governance:** mandatory
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** sickn33/antigravity-awesome-skills
- **File:** skills/uniprot-database
- **Author:** antigravity-community
