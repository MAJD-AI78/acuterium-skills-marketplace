# Marketplace Architecture

## System Design

The Agent Skills Marketplace follows a microservices architecture with three core services coordinated by BARANURION governance.

### Service Topology

```
                    ┌──────────────┐
                    │  BARANURION   │
                    │  Governance   │
                    └──────┬───────┘
                           │ Policy API
           ┌───────────────┼───────────────┐
           │               │               │
    ┌──────┴──────┐ ┌──────┴──────┐ ┌──────┴──────┐
    │  Registry   │ │  Discovery  │ │  Infusion   │
    │  Service    │ │  Service    │ │  Service    │
    │  (FastAPI)  │ │  (FastAPI)  │ │  (AcuTect)  │
    └──────┬──────┘ └──────┬──────┘ └──────┬──────┘
           │               │               │
    ┌──────┴───────────────┴───────────────┴──────┐
    │              APMS Database                   │
    │    (Protocols, Skills, Shards, Layers)       │
    └──────────────────────────────────────────────┘
```

### Registry Service
- **Technology**: FastAPI + PostgreSQL
- **Purpose**: Skill CRUD, versioning, metadata management
- **Endpoints**: `/api/v1/skills/*`
- **Auth**: TokenBridge (ACT/INT/CON tokens)

### Discovery Service
- **Technology**: FastAPI + FAISS/Pinecone
- **Purpose**: Semantic skill search, recommendations, compatibility checking
- **Endpoints**: `/api/v1/discover/*`
- **Features**: Domain filtering, shard affinity matching, ψ-score requirements

### Infusion Service
- **Technology**: Python + AcuTect-CODEX + ASIP Protocol
- **Purpose**: Deploy skills to target agents with soul infusion
- **Endpoints**: `/api/v1/infuse/*`
- **Process**: Validate → Governance check → ASIP ceremony → Deploy → Audit

## Data Model

### Skill Entity
```json
{
  "skill_id": "uuid",
  "name": "erebus-cyber-sovereignty",
  "version": "1.0.0",
  "domain": "cyber-defense",
  "author": "Acuterium Technologies",
  "manifest": "SKILL.md content",
  "shard_affinity": ["EREBUS_CSE"],
  "layer_access": [1, 2, 3, 4, 8],
  "protocols_required": ["Q-ENC", "ADOCP"],
  "governance_level": "sovereign",
  "psi_minimum": 12.0,
  "status": "published",
  "created_at": "2026-01-01T00:00:00Z",
  "updated_at": "2026-03-09T00:00:00Z"
}
```

### Infusion Record
```json
{
  "infusion_id": "uuid",
  "skill_id": "uuid",
  "target_agent": "agent-oman",
  "initiated_by": "acutect-codex",
  "governance_check": "passed",
  "asip_ceremony": "completed",
  "audit_entry_id": "AUD-00001234",
  "status": "active",
  "infused_at": "2026-03-09T00:00:00Z"
}
```

## Security
- All API calls authenticated via TokenBridge (ACT/INT/CON)
- Data encrypted in transit via Q-ENC
- Governance approval required for sovereign-level skills
- Complete audit trail in BARANURION
