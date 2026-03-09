---
name: implementing-usb-device-control-policy
display_name: Implementing Usb Device Control Policy
skill_id: ACU-SKILL-1606
version: 1.0.0
category: malware
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

# Implementing Usb Device Control Policy

## Description
Implements USB device control policies to restrict unauthorized removable media access on endpoints, preventing data exfiltration and malware introduction via USB devices. Use when deploying device control via Group Policy, Intune, or EDR platforms to enforce USB restrictions. Activates for requests involving USB control, removable media policy, device control, or data loss prevention via USB.


## Acuterium Integration
- **Thread:** T08 — ZURD
- **Shard:** Tenebris-ACIWS
- **Layers:** L8, L9, L10
- **Governance:** sovereign
- **Sovereignty Score:** 10/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/implementing-usb-device-control-policy/SKILL.md
- **Author:** cybersecurity-community
