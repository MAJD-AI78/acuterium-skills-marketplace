# Marketplace API Reference

## Base URL
`https://api.acuterium.tech/marketplace/v1`

## Authentication
All endpoints require TokenBridge authentication:
```
Authorization: Bearer <ACT_TOKEN>
X-Shard-ID: <requesting_shard_code>
X-Governance-Level: <operation_level>
```

---

## Registry API

### List Skills
```
GET /skills
```
Query params: `domain`, `shard`, `governance_level`, `page`, `limit`

### Get Skill
```
GET /skills/{skill_id}
```

### Register Skill
```
POST /skills
Content-Type: multipart/form-data

manifest: SKILL.md file
source: ZIP archive of skill source
```

### Update Skill
```
PUT /skills/{skill_id}
```

### Deprecate Skill
```
DELETE /skills/{skill_id}
```

---

## Discovery API

### Search Skills
```
GET /discover/search?q=cyber+defense&domain=cyber-defense
```

### Get Recommendations
```
GET /discover/recommend?agent={agent_id}&context={task_description}
```

### Check Compatibility
```
POST /discover/compatibility
{
  "skill_id": "uuid",
  "target_agent": "agent-oman",
  "target_shard": "STRATEDGE_ASI"
}
```

---

## Infusion API

### Infuse Skill
```
POST /infuse
{
  "skill_id": "uuid",
  "target_agent": "agent-oman",
  "infusion_params": {
    "asip_ceremony": true,
    "governance_override": false
  }
}
```

### Get Infusion Status
```
GET /infuse/{infusion_id}/status
```

### Revoke Infusion
```
DELETE /infuse/{infusion_id}
```

---

## Governance API

### Get Governance Report
```
GET /governance/report?skill_id={skill_id}
```

### Audit Trail
```
GET /governance/audit?skill_id={skill_id}&from={date}&to={date}
```
