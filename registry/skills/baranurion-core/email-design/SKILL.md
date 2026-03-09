---
name: email-design
display_name: Email Design
skill_id: ACU-SKILL-2082
version: 1.0.0
category: multimodal
thread: T03
domain: cognitive
shard_affinity:
  - Baranurion-L1
layer_access:
  - L1
  - L2
  - L3
sovereignty_score: 9
governance_level: restricted
source_repo: andersoncollab/design-agent
triggers:

---

# Email Design

## Description
This skill provides production-ready email templates and HTML best practices for rendering reliably across the 4 major email clients (Gmail, Outlook, Apple Mail, Yahoo). Email is fundamentally different from web design: Outlook uses Word's HTML renderer (not a browser), most clients strip CSS stylesheets, dark mode requires special handling, and images may be blocked. This skill teaches the constraints, patterns, and templates to ship emails that look consistent across 95%+ of inboxes.

## Acuterium Integration
- **Thread:** T03 — HISN
- **Shard:** Baranurion-L1
- **Layers:** L1, L2, L3
- **Governance:** restricted
- **Sovereignty Score:** 9/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** andersoncollab/design-agent
- **File:** skills/email-design/SKILL.md
- **Author:** andersoncollab
