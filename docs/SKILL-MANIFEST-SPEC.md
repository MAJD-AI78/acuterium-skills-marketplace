# Skill Manifest Specification (SKILL.md)

## Version: 1.0.0

Every skill published to the marketplace requires a `SKILL.md` manifest file with YAML frontmatter.

## Required Fields

```yaml
---
# Skill Identity
name: "skill-name"              # Unique identifier (kebab-case)
version: "1.0.0"                # Semantic versioning
display_name: "Skill Name"      # Human-readable name
description: "Brief description" # Max 200 characters
domain: "domain-name"            # Primary domain

# Authorship
author: "Acuterium Technologies"
author_shard: "EREBUS_CSE"       # Authoring shard (optional)

# Compatibility
shard_affinity:                  # Compatible neural shards
  - "EREBUS_CSE"
  - "TENEBRIS_ACIWS"
layer_access:                    # Required cognitive layers (1-10)
  - 1  # Perception
  - 4  # Reasoning
  - 8  # Thinking-Engine

# Protocol Dependencies
protocols_required:
  - "Q-ENC"       # Quantum encryption
  - "ADOCP"       # Orchestration control
  - "CogniMesh"   # Semantic knowledge mesh

# Governance
governance_level: "sovereign"    # advisory | restricted | mandatory | sovereign
psi_minimum: 12.0               # Minimum ψ score for target agent
cwh_approval_required: true      # Requires CWH Hypervisor sign-off

# Capabilities
capabilities:
  - "threat-detection"
  - "osint-analysis"
  - "cyber-defense"
---

# Skill Name

Full documentation of the skill follows here...
```

## Domain Values
| Domain | Description |
|--------|-------------|
| `cyber-defense` | Erebus cyber warfare and defense |
| `defense-industry` | Wagha physical defense |
| `governance` | BARANURION policy and compliance |
| `legal` | RUZN legal AI |
| `intelligence` | OSINT, SIGINT, threat intel |
| `development` | AcuTect engineering and deployment |
| `business` | BizElevate strategy |
| `finance` | Finariah financial AI |
| `cognitive` | Core cognitive engine operations |
| `interface` | ACAI V2 user interface |
| `hardware` | Hardware division integration |
| `satellite` | AcuSat operations |

## Governance Levels
| Level | Description | Approval |
|-------|-------------|----------|
| `advisory` | Log only, auto-approve | None |
| `restricted` | Requires BARANURION approval | Automated |
| `mandatory` | Requires manual governance review | Manual |
| `sovereign` | Nation-state level — CWH + manual | CWH + Manual |

## Version History
| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-03-09 | Initial specification |
