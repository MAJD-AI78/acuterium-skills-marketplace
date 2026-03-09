# Changelog — acuterium-skills-marketplace

## [5.0.0] — 2026-03-09

### Added
- **44 new agent skills** (42 Legal AI from lawvable/awesome-legal-skills + 2 MCP Market)
- Legal AI — Commercial Law: 6 skills (Contract Review, Debt Recovery, NDA Review/Triage, NIL Contracts, Tech Negotiation)
- Legal AI — Privacy Law: 6 skills (Cookie Policy, DPIA, GDPR Breach Sentinel, Privacy Compliance, Notice/Policy Drafting)
- Legal AI — Compliance: 2 skills (Vendor Due Diligence, Whistleblower Policy Auditor)
- Legal AI — Employment Law: 2 skills (Dismissal Challenge/Notification Drafters)
- Legal AI — Corporate Law: 1 skill (Shareholder Disclosure Enforcer)
- Legal AI — Legal Methodology: 6 skills (Legal Simulation, Mediation, Red Team Verifier, Risk Assessment x2, Statutory Interpretation)
- Legal AI — Legal Tooling: 3 skills (Canned Responses, Meeting Briefing, Tabular Review)
- Legal AI — MS Office: 9 skills (Excel x3, Outlook, PowerPoint, Word x4)
- Legal AI — Adobe: 2 skills (PDF Processing x2)
- Legal AI — Vibe-Coding: 2 skills (Security Review, VS Code Extension Builder)
- Legal AI — Meta-Skills: 3 skills (Skill Self-Creation x2, Skill Optimizer)
- MCP Market — Web Intelligence: 1 skill (Google Search & Web Access)
- MCP Market — Research Intelligence: 1 skill (Ark Research)
- Shard mappings: W-02 Ajraam (25), W-08 ZURD (7), EREBUS-CSE (4), Diaran-MOE (3), others
- URANA protocol mappings: URANA-RISK-001, URANA-AUDT-001, URANA-COMP-001, URANA-QMS-001
- 6 French-law skills flagged for Oman/GCC localization
- Updated skills.json (3,972 total), CSV master index, SQL seeds, Excel registry V5
- 2 duplicates excluded: Agent Team Task Coordination, Team Communication Protocols (already in v4)

### Changed
- Skills registry total: 3,928 → 3,972
- skills.json schema: added ruzn_module, urana_module, erebus_integration, priority, localization_flag fields

## [4.0.0] — 2026-03-09

### Added
- 1,740 new agent skills from MCP Market, dmgrok catalog, awesome-agent-skills, anthropic cookbooks/courses, obra/superpowers
- Registry total: 2,188 → 3,928

## [3.0.0] — 2026-03-09

### Added
- 2,179 new agent skills from 21 GitHub repositories
- Registry total: 9 → 2,188

## [0.1.0] — 2026-03-09

### Added
- Initial marketplace architecture (Registry, Discovery, Infusion services)
- Skill manifest specification (SKILL.md format)
- Registry of 9 existing agent skills
- Database schema extending APMS
- Docker Compose deployment configuration
- CLI tool stub
- API reference documentation
- BARANURION governance integration points
- ASIP infusion ceremony workflow
