# Acuterium Agent Skills Marketplace

<p align="center">
  <strong>Central Registry, Distribution & Infusion Hub</strong><br/>
  <em>Powered by AcuTect-CODEX — "The Architect"</em>
</p>

---

## Overview

The **Acuterium Agent Skills Marketplace** is the centralized platform for registering, distributing, discovering, and infusing agent skills across the entire Acuterium ecosystem. Every skill — from neural shard orchestration to sovereign governance — flows through this marketplace.

Skills are **ASIP-infused** (Soul Infusion Protocol) units of specialized intelligence that can be deployed to any compatible agent within the ecosystem, governed by BARANURION and orchestrated by Diaran-MOE-Heavy.

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    BARANURION                            │
│              (Governance & Compliance)                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌──────────────┐   │
│  │   REGISTRY   │  │  DISCOVERY  │  │   INFUSION    │   │
│  │   Service    │  │   Service   │  │   Service     │   │
│  │             │  │             │  │  (AcuTect)    │   │
│  └──────┬──────┘  └──────┬──────┘  └──────┬───────┘   │
│         │                │                │             │
│  ┌──────┴──────────────────┴────────────────┴───────┐   │
│  │              SKILL CATALOG (APMS)                │   │
│  │  254 Protocols · 9 Skills · 12 Neural Shards    │   │
│  └──────────────────────────────────────────────────┘   │
│                                                         │
│  ┌──────────────────────────────────────────────────┐   │
│  │           DISTRIBUTION LAYER                     │   │
│  │  TokenBridge (ACT/INT/CON) · Q-ENC · CogniMesh  │   │
│  └──────────────────────────────────────────────────┘   │
│                                                         │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────────┐  │
│  │Diaran-  │ │ Agent-  │ │  RUZN   │ │ BizElevate  │  │
│  │MOE-Heavy│ │ Oman    │ │  Legal  │ │ Strategy    │  │
│  │(785 exp)│ │         │ │         │ │             │  │
│  └─────────┘ └─────────┘ └─────────┘ └─────────────┘  │
│                   Target Agents                        │
└─────────────────────────────────────────────────────────┘
```

## Installed Skills (9 Active)

| # | Skill | ID | Domain |
|---|-------|----|--------|
| 1 | **Acuterium Master Orchestrator** | `fc1079c6` | Ecosystem orchestration & routing |
| 2 | **ACAI V2 Interface** | `7580c640` | Unified AI interface |
| 3 | **Cognitive Engines** | `79cac7d4` | 10-layer cognitive architecture |
| 4 | **Fullstack Platform** | `467915b0` | Full-stack development |
| 5 | **Erebus Cyber Sovereignty** | `905bb3ce` | Cyber warfare & defense |
| 6 | **Baranurion Core Orchestration** | `5302abe5` | Governance & compliance |
| 7 | **RUZN Government Platform** | `c18427cb` | Legal AI & government |
| 8 | **Commercial Products** | `33f596f5` | Product management |
| 9 | **AcuTect DevOps Deployment** | `5c4bf71a` | CI/CD & infrastructure |

## Core Services

### 1. Registry Service
Central catalog of all available skills with metadata, versioning, and dependency tracking.

### 2. Discovery Service
Search, filter, and recommend skills based on agent capabilities, domain requirements, and compatibility.

### 3. Infusion Service (AcuTect-CODEX)
ASIP-powered skill deployment — infuses skills into target agents with soul, purpose, and governance compliance.

### 4. Governance Layer (BARANURION)
Policy enforcement, audit trails, and ethical compliance for all marketplace operations.

## Skill Lifecycle

```
1. DEVELOP    → Author skill with SKILL.md manifest
2. REGISTER   → Submit to registry with metadata
3. REVIEW     → BARANURION governance check + URANA QA audit
4. PUBLISH    → Available in marketplace catalog
5. DISCOVER   → Agents find skills via search/recommendation
6. INFUSE     → AcuTect-CODEX deploys skill to agent via ASIP
7. MONITOR    → Execution tracked by BARANURION audit system
8. UPDATE     → Version management with backward compatibility
```

## Skill Manifest Format (SKILL.md)

Every skill requires a manifest:

```yaml
---
name: "skill-name"
version: "1.0.0"
domain: "cyber-defense"
author: "Acuterium Technologies"
shard_affinity: ["EREBUS_CSE", "TENEBRIS_ACIWS"]
layer_access: [1, 2, 3, 4, 8]  # L1-Perception through L8-Thinking
protocols_required: ["Q-ENC", "ADOCP", "CogniMesh"]
governance_level: "sovereign"
psi_minimum: 12.0
---
```

## Dependencies

- `AcuTect_CODEX` — Skill authoring and infusion engine
- `baranurion` — Governance enforcement
- `diaran-ai` — Skill routing to target agents
- `acuterium-contracts` — Skill interface schemas
- `APMS` — Protocol management backing store

## Quick Start

```bash
# List available skills
acuterium skills list

# Search skills by domain
acuterium skills search --domain cyber-defense

# Install a skill to an agent
acuterium skills infuse --skill erebus-cyber-sovereignty --target agent-oman

# Publish a new skill
acuterium skills publish --manifest SKILL.md --source ./src
```

---

*SECURE · SOVEREIGN · SCALABLE*  
*Genesis Through Intelligence*
