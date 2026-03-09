---
name: testing-websocket-api-security
display_name: Testing Websocket Api Security
skill_id: ACU-SKILL-1808
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

# Testing Websocket Api Security

## Description
Tests WebSocket API implementations for security vulnerabilities including missing authentication on WebSocket upgrade, Cross-Site WebSocket Hijacking (CSWSH), injection attacks through WebSocket messages, insufficient input validation, denial-of-service via message flooding, and information leakage through WebSocket frames. The tester intercepts WebSocket handshakes and messages using Burp Suite, crafts malicious payloads, and tests for authorization bypass on WebSocket channels. Activates for requests involving WebSocket security testing, WS penetration testing, CSWSH attack, or real-time API security assessment.


## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/testing-websocket-api-security/SKILL.md
- **Author:** cybersecurity-community
