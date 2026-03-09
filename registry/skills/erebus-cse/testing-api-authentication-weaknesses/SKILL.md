---
name: testing-api-authentication-weaknesses
display_name: Testing Api Authentication Weaknesses
skill_id: ACU-SKILL-1789
version: 1.0.0
category: red-team
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

# Testing Api Authentication Weaknesses

## Description
Tests API authentication mechanisms for weaknesses including broken token validation, missing authentication on endpoints, weak password policies, credential stuffing susceptibility, token leakage in URLs or logs, and session management flaws. The tester evaluates JWT implementation, API key handling, OAuth flows, and session token entropy to identify authentication bypasses. Maps to OWASP API2:2023 Broken Authentication. Activates for requests involving API authentication testing, token validation assessment, credential security testing, or API auth bypass.


## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/testing-api-authentication-weaknesses/SKILL.md
- **Author:** cybersecurity-community
