---
name: performing-lateral-movement-detection
display_name: Performing Lateral Movement Detection
skill_id: ACU-SKILL-1692
version: 1.0.0
category: threat-intelligence
thread: T06
domain: security
shard_affinity:
  - Edna-SIGINT
layer_access:
  - L7
  - L8
  - L9
sovereignty_score: 9
governance_level: restricted
source_repo: mukul975/Anthropic-Cybersecurity-Skills
triggers:

---

# Performing Lateral Movement Detection

## Description
Detects lateral movement techniques including Pass-the-Hash, PsExec, WMI execution, RDP pivoting, and SMB-based spreading using SIEM correlation of Windows event logs, network flow data, and endpoint telemetry mapped to MITRE ATT&CK Lateral Movement (TA0008) techniques.


## Acuterium Integration
- **Thread:** T06 — EDNA
- **Shard:** Edna-SIGINT
- **Layers:** L7, L8, L9
- **Governance:** restricted
- **Sovereignty Score:** 9/10
- **PSI Minimum:** 10.0

## Source
- **Repository:** mukul975/Anthropic-Cybersecurity-Skills
- **File:** skills/performing-lateral-movement-detection/SKILL.md
- **Author:** cybersecurity-community
