---
name: secure-code-review
display_name: Secure Code Review
skill_id: ACU-SKILL-2134
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

# Secure Code Review

## Description
Perform security-focused code review using taint analysis, data flow analysis, control flow analysis, and framework-specific insecure patterns. Covers Java/Spring Boot, Python/Django/Flask, and Node.js/Express. Identifies vulnerabilities at the code level with exact file/line references, PoC scenarios, and remediation code. Trigger when user mentions "code review", "security review", "secure code review", "find vulnerabilities in this code", "audit this code", "is this code secure", "taint analysis", or uploads source code files, pull requests, or git diffs. Also trigger when user asks about insecure coding patterns, dangerous functions, or framework-specific security issues.


## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** Poatan222/Skills-security
- **File:** secure-code-review/SKILL.md
- **Author:** Poatan222/Skills-security
