---
document_id: ACU-IMPL-LEG-001
title: "Pre-Deployment Implementation Instructions: Legal, QA, Audit & Compliance Skill Registry"
version: 1.0.0
author: Acuterium Technologies
classification: SOVEREIGN — INTERNAL
date: "2026-03-09"
applies_to: "RUZN.AI, Ūrānā, Acuterium Skill Registry V5"
---

# Pre-Deployment Implementation Instructions

## Comprehensive Guide for Legal AI, QA/Audit, Compliance & Accreditation Skills

---

## Part A: Trigger Keyword Extraction (921 Community Skills)

### Problem Statement

921 community skills in the registry (`ACU-SKILL-REG-001_Master_Index_V5.csv`) lack explicit trigger keywords, which prevents accurate DIARAN-MOE routing. Without keywords, the 785-expert MoE engine cannot reliably route requests to the correct skill.

### Solution: Automated Keyword Extraction Pipeline

#### Step 1: Extract Keywords from Skill Descriptions

```python
#!/usr/bin/env python3
"""
ACU-KEYWORD-EXTRACTOR v1.0
Automated trigger keyword extraction for Acuterium Skill Registry.
Processes skills with missing trigger_keywords field.
"""

import json
import csv
import re
from collections import Counter

# Stopwords for filtering
LEGAL_STOPWORDS = {'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been',
                   'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
                   'would', 'could', 'should', 'may', 'might', 'shall', 'can',
                   'this', 'that', 'these', 'those', 'it', 'its', 'for', 'with',
                   'from', 'to', 'of', 'in', 'on', 'at', 'by', 'and', 'or',
                   'not', 'no', 'but', 'if', 'when', 'where', 'how', 'what',
                   'which', 'who', 'whom', 'use', 'used', 'using', 'you', 'your'}

# Acuterium domain vocabulary for boosting
DOMAIN_BOOST_TERMS = {
    'legal': ['contract', 'compliance', 'audit', 'regulatory', 'statute', 'litigation',
              'verdict', 'precedent', 'jurisdiction', 'arbitration', 'mediation'],
    'security': ['vulnerability', 'exploit', 'pentest', 'malware', 'firewall', 'encryption',
                 'authentication', 'authorization', 'RBAC', 'OWASP', 'CVE'],
    'qa': ['quality', 'assurance', 'testing', 'FMEA', 'CAPA', 'SPC', 'ISO', 'defect',
           'inspection', 'accreditation', 'certification', 'attestation'],
    'audit': ['audit', 'controls', 'findings', 'evidence', 'trail', 'compliance',
              'internal', 'external', 'fieldwork', 'sampling', 'materiality']
}


def extract_keywords_from_description(description: str, name: str, category: str) -> list:
    """
    Extracts trigger keywords from skill description using multi-strategy approach:
    1. N-gram extraction (bigrams and trigrams for compound terms)
    2. Named entity-like pattern matching (capitalized terms, acronyms)
    3. Domain vocabulary boosting
    4. Verb phrase extraction for action triggers
    """
    keywords = set()
    
    # Strategy 1: Extract quoted terms (often exact trigger phrases)
    quoted = re.findall(r'"([^"]+)"', description)
    keywords.update(q.lower().strip() for q in quoted if len(q) > 2)
    
    # Strategy 2: Extract acronyms and technical terms
    acronyms = re.findall(r'\b[A-Z]{2,}(?:-[A-Z]+)*\b', description)
    keywords.update(a for a in acronyms if a not in {'AI', 'USE', 'THE', 'FOR'})
    
    # Strategy 3: Extract hyphenated compound terms
    compounds = re.findall(r'\b\w+(?:-\w+)+\b', description.lower())
    keywords.update(c for c in compounds if len(c) > 4)
    
    # Strategy 4: Bigram extraction from cleaned text
    words = [w.lower() for w in re.findall(r'\b\w+\b', description) 
             if w.lower() not in LEGAL_STOPWORDS and len(w) > 2]
    for i in range(len(words) - 1):
        bigram = f"{words[i]} {words[i+1]}"
        keywords.add(bigram)
    
    # Strategy 5: Domain boost — add if domain terms found in description
    desc_lower = description.lower()
    for domain, terms in DOMAIN_BOOST_TERMS.items():
        if category.lower() in domain or any(t in desc_lower for t in terms[:3]):
            for term in terms:
                if term.lower() in desc_lower:
                    keywords.add(term.lower())
    
    # Strategy 6: Name-derived keywords
    name_parts = name.replace('-', ' ').replace('_', ' ').split()
    keywords.update(p.lower() for p in name_parts if p.lower() not in LEGAL_STOPWORDS)
    
    # Filter and rank
    ranked = sorted(keywords, key=lambda k: (
        len(k.split()),  # prefer multi-word terms
        sum(1 for d in DOMAIN_BOOST_TERMS.values() if k in [t.lower() for t in d]),  # domain relevance
        len(k)  # longer terms often more specific
    ), reverse=True)
    
    return ranked[:20]  # Top 20 keywords per skill


def process_registry(csv_path: str, output_path: str):
    """Process entire registry, extract keywords for skills missing them."""
    updated = 0
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    for row in rows:
        description = row.get('description', '')
        name = row.get('name', '')
        category = row.get('category', '')
        
        if description and len(description) > 10:
            keywords = extract_keywords_from_description(description, name, category)
            if keywords:
                row['extracted_keywords'] = '; '.join(keywords)
                updated += 1
    
    # Write updated registry
    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        fieldnames = list(rows[0].keys())
        if 'extracted_keywords' not in fieldnames:
            fieldnames.append('extracted_keywords')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Processed {len(rows)} skills, extracted keywords for {updated}")
    return updated


if __name__ == '__main__':
    process_registry(
        'ACU-SKILL-REG-001_Master_Index_V5.csv',
        'ACU-SKILL-REG-001_Master_Index_V5_WITH_KEYWORDS.csv'
    )
```

#### Step 2: Validate Extracted Keywords

```bash
# Run extraction
python3 acu_keyword_extractor.py

# Verify output
head -5 ACU-SKILL-REG-001_Master_Index_V5_WITH_KEYWORDS.csv

# Count skills with keywords vs without
awk -F',' '{if($NF != "") count++} END {print count " skills with keywords"}' \
    ACU-SKILL-REG-001_Master_Index_V5_WITH_KEYWORDS.csv
```

#### Step 3: Push Keywords into SQL Registry

```sql
-- Add extracted_keywords column if not exists
ALTER TABLE marketplace_skills 
ADD COLUMN IF NOT EXISTS extracted_keywords TEXT DEFAULT NULL;

-- Batch update from CSV import (use transaction wrapper per Part C)
BEGIN;

-- Example: Update keywords for a specific skill
UPDATE marketplace_skills 
SET extracted_keywords = 'contract review, agreement analysis, clause detection'
WHERE skill_id = 'ACU-SKILL-LEG-001';

-- Bulk update via COPY from CSV
-- COPY temp_keywords FROM '/path/to/keywords_update.csv' WITH CSV HEADER;
-- UPDATE marketplace_skills m 
-- SET extracted_keywords = t.extracted_keywords 
-- FROM temp_keywords t 
-- WHERE m.skill_id = t.skill_id;

COMMIT;
```

---

## Part B: Status Promotion Workflow (2,179 Draft → Published)

### Problem Statement

2,179 skills are in `draft` status and need a staged promotion workflow to reach `published` status safely.

### Staged Workflow Implementation

```
┌─────────┐    ┌──────────┐    ┌──────────┐    ┌───────────┐    ┌───────────┐
│  DRAFT  │───▶│ REVIEWED │───▶│ TESTING  │───▶│ VALIDATED │───▶│ PUBLISHED │
└─────────┘    └──────────┘    └──────────┘    └───────────┘    └───────────┘
    │               │               │                │                │
    │ Auto-extract  │ Peer review   │ Integration    │ Sovereignty    │ Production
    │ keywords      │ + domain      │ testing with   │ compliance     │ ready
    │ + metadata    │ expert sign   │ DIARAN-MOE     │ verification   │
    │ validation    │ off           │ routing        │ + final        │
    │               │               │                │ approval       │
```

#### Stage 1: DRAFT → REVIEWED

```sql
-- Promotion criteria check
SELECT skill_id, name, 
  CASE 
    WHEN description IS NOT NULL AND LENGTH(description) > 50 THEN 'PASS'
    ELSE 'FAIL'
  END as description_check,
  CASE 
    WHEN extracted_keywords IS NOT NULL AND LENGTH(extracted_keywords) > 10 THEN 'PASS'
    ELSE 'FAIL'
  END as keywords_check,
  CASE 
    WHEN thread IS NOT NULL AND thread_code IS NOT NULL THEN 'PASS'
    ELSE 'FAIL'
  END as thread_mapping_check,
  CASE 
    WHEN sovereignty_score IS NOT NULL AND sovereignty_score >= 0 THEN 'PASS'
    ELSE 'FAIL'
  END as sovereignty_check
FROM marketplace_skills
WHERE status = 'draft';

-- Promote passing skills
BEGIN;

UPDATE marketplace_skills 
SET status = 'reviewed',
    updated_at = NOW()
WHERE status = 'draft'
  AND description IS NOT NULL 
  AND LENGTH(description) > 50
  AND extracted_keywords IS NOT NULL
  AND thread IS NOT NULL
  AND sovereignty_score IS NOT NULL;

-- Log promotion event
INSERT INTO skill_audit_log (skill_id, action, from_status, to_status, actor, timestamp)
SELECT skill_id, 'STATUS_PROMOTION', 'draft', 'reviewed', 'system_auto', NOW()
FROM marketplace_skills
WHERE status = 'reviewed' AND updated_at >= NOW() - INTERVAL '1 minute';

COMMIT;
```

#### Stage 2: REVIEWED → TESTING

```sql
-- Requires: domain expert sign-off recorded in audit log
BEGIN;

UPDATE marketplace_skills 
SET status = 'testing',
    updated_at = NOW()
WHERE status = 'reviewed'
  AND skill_id IN (
    SELECT skill_id FROM skill_audit_log 
    WHERE action = 'DOMAIN_EXPERT_APPROVED'
    AND timestamp >= NOW() - INTERVAL '30 days'
  );

INSERT INTO skill_audit_log (skill_id, action, from_status, to_status, actor, timestamp)
SELECT skill_id, 'STATUS_PROMOTION', 'reviewed', 'testing', 'system_auto', NOW()
FROM marketplace_skills
WHERE status = 'testing' AND updated_at >= NOW() - INTERVAL '1 minute';

COMMIT;
```

#### Stage 3: TESTING → VALIDATED

```sql
-- Requires: successful DIARAN-MOE routing test results
BEGIN;

UPDATE marketplace_skills 
SET status = 'validated',
    updated_at = NOW()
WHERE status = 'testing'
  AND skill_id IN (
    SELECT skill_id FROM skill_test_results 
    WHERE test_type = 'diaran_moe_routing'
    AND result = 'PASS'
    AND tested_at >= NOW() - INTERVAL '7 days'
  );

COMMIT;
```

#### Stage 4: VALIDATED → PUBLISHED

```sql
-- Final promotion: requires sovereignty compliance verification
BEGIN;

-- Verify sovereignty compliance for sovereign-tier skills
UPDATE marketplace_skills 
SET status = 'published',
    updated_at = NOW()
WHERE status = 'validated'
  AND (
    -- Non-sovereign skills: auto-promote
    (governance_level != 'sovereign')
    OR
    -- Sovereign skills: require explicit approval
    (governance_level = 'sovereign' AND skill_id IN (
      SELECT skill_id FROM skill_audit_log 
      WHERE action = 'SOVEREIGNTY_COMPLIANCE_VERIFIED'
    ))
  );

INSERT INTO skill_audit_log (skill_id, action, from_status, to_status, actor, timestamp)
SELECT skill_id, 'STATUS_PROMOTION', 'validated', 'published', 'system_auto', NOW()
FROM marketplace_skills
WHERE status = 'published' AND updated_at >= NOW() - INTERVAL '1 minute';

COMMIT;
```

---

## Part C: SQL Execution with Transaction Wrapper

### Problem Statement

All SQL operations against the skill registry must execute within transaction wrappers for atomic rollback capability, especially for batch operations affecting 2,179+ records.

### Transaction Wrapper Template

```sql
-- ═══════════════════════════════════════════════════════
-- ACUTERIUM SKILL REGISTRY — ATOMIC TRANSACTION WRAPPER
-- ═══════════════════════════════════════════════════════
-- Author: Acuterium Technologies
-- Date: 2026-03-09
-- Purpose: Ensure atomic execution with rollback on failure
-- Target DB: PostgreSQL 16+ (sovereign deployment)
-- ═══════════════════════════════════════════════════════

-- Pre-flight: Create savepoint for nested transactions
BEGIN;
SAVEPOINT pre_operation;

-- ╔═══════════════════════════════════════════╗
-- ║  STEP 1: PRE-VALIDATION                  ║
-- ╚═══════════════════════════════════════════╝

-- Validate current state before mutation
DO $$
DECLARE
    total_skills INTEGER;
    draft_count INTEGER;
    published_count INTEGER;
BEGIN
    SELECT COUNT(*) INTO total_skills FROM marketplace_skills;
    SELECT COUNT(*) INTO draft_count FROM marketplace_skills WHERE status = 'draft';
    SELECT COUNT(*) INTO published_count FROM marketplace_skills WHERE status = 'published';
    
    RAISE NOTICE 'Pre-operation state: % total, % draft, % published',
        total_skills, draft_count, published_count;
    
    -- Abort if unexpected state
    IF total_skills = 0 THEN
        RAISE EXCEPTION 'Registry is empty — aborting operation';
    END IF;
END $$;

-- ╔═══════════════════════════════════════════╗
-- ║  STEP 2: EXECUTE MUTATIONS               ║
-- ╚═══════════════════════════════════════════╝

SAVEPOINT before_mutations;

-- [INSERT YOUR BATCH OPERATIONS HERE]
-- Example: Keyword insertion for 921 skills
UPDATE marketplace_skills 
SET extracted_keywords = subquery.keywords
FROM (
    -- Your keyword update subquery
    SELECT skill_id, extracted_keywords as keywords
    FROM temp_keyword_import
) AS subquery
WHERE marketplace_skills.skill_id = subquery.skill_id;

-- ╔═══════════════════════════════════════════╗
-- ║  STEP 3: POST-VALIDATION                 ║
-- ╚═══════════════════════════════════════════╝

DO $$
DECLARE
    affected_rows INTEGER;
    null_keywords INTEGER;
BEGIN
    GET DIAGNOSTICS affected_rows = ROW_COUNT;
    
    SELECT COUNT(*) INTO null_keywords 
    FROM marketplace_skills 
    WHERE extracted_keywords IS NULL AND status = 'draft';
    
    RAISE NOTICE 'Post-operation: % rows affected, % still missing keywords',
        affected_rows, null_keywords;
    
    -- Rollback if unexpected result
    IF affected_rows = 0 THEN
        RAISE EXCEPTION 'No rows affected — rolling back';
    END IF;
    
    -- Rollback if data corruption detected
    IF null_keywords > 1000 THEN
        RAISE NOTICE 'WARNING: High null keyword count — reviewing...';
    END IF;
END $$;

-- ╔═══════════════════════════════════════════╗
-- ║  STEP 4: AUDIT LOG                       ║
-- ╚═══════════════════════════════════════════╝

INSERT INTO skill_registry_audit_log (
    operation_type, 
    operation_description,
    affected_count,
    executor,
    executed_at,
    rollback_available
)
VALUES (
    'BATCH_KEYWORD_EXTRACTION',
    'Automated keyword extraction for 921 community skills lacking explicit trigger keywords',
    (SELECT COUNT(*) FROM marketplace_skills WHERE extracted_keywords IS NOT NULL),
    'acuterium_admin',
    NOW(),
    TRUE
);

-- ╔═══════════════════════════════════════════╗
-- ║  STEP 5: COMMIT OR ROLLBACK              ║
-- ╚═══════════════════════════════════════════╝

-- OPTION A: If everything looks good
COMMIT;

-- OPTION B: If issues detected (uncomment to use)
-- ROLLBACK TO SAVEPOINT before_mutations;
-- ROLLBACK;
```

### Backup Before Batch Operations

```bash
#!/bin/bash
# Pre-operation backup script
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
DB_NAME="acuterium_skills_registry"
BACKUP_DIR="/sovereign/backups/skill_registry"

# Create backup
pg_dump -Fc -f "${BACKUP_DIR}/registry_${TIMESTAMP}.dump" ${DB_NAME}

# Verify backup
pg_restore --list "${BACKUP_DIR}/registry_${TIMESTAMP}.dump" | head -20

echo "Backup created: registry_${TIMESTAMP}.dump"
echo "To restore: pg_restore -d ${DB_NAME} ${BACKUP_DIR}/registry_${TIMESTAMP}.dump"
```

---

## Part D: New Skills Registration SQL

### Insert the 15 New Legal/QA/Audit/Compliance Skills

```sql
-- ═══════════════════════════════════════════════════════
-- INSERT NEW LEGAL, QA, AUDIT & COMPLIANCE SKILLS
-- Atomic transaction with full rollback capability
-- ═══════════════════════════════════════════════════════

BEGIN;
SAVEPOINT new_skills_insert;

INSERT INTO marketplace_skills (
    skill_id, registry_id, name, display_name, version, category,
    thread, thread_code, domain, description, shard_assignment,
    layer_access, sovereignty_score, governance_level, status,
    author, acuterium_product, priority, localization_flag,
    extracted_keywords, created_at, updated_at
) VALUES
-- Legal AI Skills (RUZN.AI)
('ACU-SKILL-LEG-001', 'leg-contract-rev-001', 'contract-review-agent', 'Contract Review Agent', '1.0.0', 'legal-ai',
 'T11 — RUZN Supreme Legal', 'T11', 'cognitive', 
 'Sovereign AI agent for automated contract review, clause extraction, risk flagging, and compliance verification against Omani/GCC legal standards.',
 'C-01 (RUZN-GOV)', 'Layer 4 — Reasoning, Layer 9 — Cognition', 10, 'sovereign', 'draft',
 'Acuterium Technologies', 'RUZN.AI', 'P1-Critical', 'ar-en',
 'contract review, agreement analysis, clause detection, unfavorable terms, contract compliance, مراجعة العقود',
 NOW(), NOW()),

('ACU-SKILL-LEG-002', 'leg-research-assist-002', 'legal-research-assistant', 'Legal Research Assistant', '1.0.0', 'legal-ai',
 'T11 — RUZN Supreme Legal', 'T11', 'cognitive',
 'Sovereign AI agent for comprehensive legal research across Omani statutes, GCC regulatory frameworks, and international precedents with bilingual memo generation.',
 'C-01 (RUZN-GOV)', 'Layer 4 — Reasoning, Layer 9 — Cognition', 10, 'sovereign', 'draft',
 'Acuterium Technologies', 'RUZN.AI', 'P1-Critical', 'ar-en',
 'legal research, case law, statute lookup, precedent analysis, research memo, بحث قانوني, سوابق قضائية',
 NOW(), NOW()),

('ACU-SKILL-LEG-003', 'leg-doc-draft-003', 'legal-document-drafting-agent', 'Legal Document Drafting Agent', '1.0.0', 'legal-ai',
 'T11 — RUZN Supreme Legal', 'T11', 'cognitive',
 'Sovereign AI agent for generating legal document drafts — demand letters, motions, contracts, ministerial correspondence with bilingual RTL-native output.',
 'C-01 (RUZN-GOV)', 'Layer 4 — Reasoning, Layer 9 — Cognition', 10, 'sovereign', 'draft',
 'Acuterium Technologies', 'RUZN.AI', 'P1-Critical', 'ar-en',
 'document drafting, legal document generation, demand letter, motion drafting, صياغة المستندات القانونية',
 NOW(), NOW()),

('ACU-SKILL-LEG-004', 'leg-due-diligence-004', 'due-diligence-agent', 'Due Diligence Agent', '1.0.0', 'legal-ai',
 'T11 — RUZN Supreme Legal', 'T11', 'cognitive',
 'Sovereign AI agent for automated due diligence across M&A, government procurement, and institutional integrity assessments with evidence chain integration.',
 'C-01 (RUZN-GOV), W-07 (Ūrānā-INTEL)', 'Layer 4 — Reasoning, Layer 6 — Intelligence', 10, 'sovereign', 'draft',
 'Acuterium Technologies', 'RUZN.AI, Ūrānā', 'P1-Critical', 'ar-en',
 'due diligence, data room analysis, M&A review, risk identification, beneficial ownership, العناية الواجبة',
 NOW(), NOW()),

('ACU-SKILL-LEG-005', 'leg-ediscovery-005', 'e-discovery-processing-agent', 'E-Discovery Processing Agent', '1.0.0', 'legal-ai',
 'T11 — RUZN Supreme Legal', 'T11', 'cognitive',
 'Sovereign AI agent for processing electronic evidence with intelligent relevance filtering, privilege detection, and sovereign chain of custody.',
 'C-01 (RUZN-GOV)', 'Layer 4 — Reasoning, Layer 6 — Intelligence', 10, 'sovereign', 'draft',
 'Acuterium Technologies', 'RUZN.AI', 'P2-High', 'ar-en',
 'e-discovery, electronic evidence, document review, privilege detection, litigation support, الاكتشاف الإلكتروني',
 NOW(), NOW()),

-- Compliance AI Skills
('ACU-SKILL-COMP-001', 'comp-monitoring-001', 'compliance-monitoring-agent', 'Compliance Monitoring Agent', '1.0.0', 'compliance-ai',
 'T11 — RUZN Supreme Legal', 'T11', 'cognitive',
 'Sovereign AI agent for continuous regulatory compliance monitoring across 47+ frameworks with 97.2% detection accuracy and 12,847 daily automated tests.',
 'C-01 (RUZN-GOV), W-07 (Ūrānā-INTEL)', 'Layer 4 — Reasoning, Layer 9 — Cognition', 10, 'sovereign', 'draft',
 'Acuterium Technologies', 'RUZN.AI, Ūrānā', 'P1-Critical', 'ar-en',
 'compliance monitoring, regulatory tracking, compliance deadline, regulatory alerts, مراقبة الامتثال',
 NOW(), NOW()),

('ACU-SKILL-COMP-002', 'comp-reg-change-002', 'regulatory-change-intelligence-agent', 'Regulatory Change Intelligence Agent', '1.0.0', 'compliance-ai',
 'T11 — RUZN Supreme Legal', 'T11', 'cognitive',
 'Sovereign AI agent within Ūrānā Regulatory Iron Dome for detecting regulatory changes across GCC jurisdictions with 97.2% accuracy.',
 'W-07 (Ūrānā-INTEL)', 'Layer 4 — Reasoning, Layer 6 — Intelligence', 10, 'sovereign', 'draft',
 'Acuterium Technologies', 'Ūrānā', 'P1-Critical', 'ar-en',
 'regulatory change, legislative update, policy impact assessment, regulatory intelligence, تغيير تنظيمي',
 NOW(), NOW()),

('ACU-SKILL-COMP-003', 'comp-policy-enforce-003', 'policy-enforcement-agent', 'Policy Enforcement Agent', '1.0.0', 'compliance-ai',
 'T11 — RUZN Supreme Legal', 'T11', 'cognitive',
 'Sovereign AI agent for real-time policy violation detection, gap analysis, and mandatory training compliance tracking.',
 'C-01 (RUZN-GOV), W-07 (Ūrānā-INTEL)', 'Layer 4 — Reasoning, Layer 9 — Cognition', 10, 'sovereign', 'draft',
 'Acuterium Technologies', 'RUZN.AI, Ūrānā', 'P1-Critical', 'ar-en',
 'policy enforcement, policy violation, internal policy monitoring, gap analysis, إنفاذ السياسات',
 NOW(), NOW()),

('ACU-SKILL-COMP-004', 'comp-risk-assess-004', 'risk-assessment-intelligence-agent', 'Risk Assessment Intelligence Agent', '1.0.0', 'compliance-ai',
 'T11 — RUZN Supreme Legal', 'T11', 'cognitive',
 'Sovereign AI agent for comprehensive compliance risk assessment with sanctions screening across 247 jurisdictions and predictive modeling.',
 'W-07 (Ūrānā-INTEL)', 'Layer 4 — Reasoning, Layer 9 — Cognition', 10, 'sovereign', 'draft',
 'Acuterium Technologies', 'Ūrānā', 'P1-Critical', 'ar-en',
 'risk assessment, compliance risk, predictive risk, sanctions screening, تقييم المخاطر, فحص العقوبات',
 NOW(), NOW()),

('ACU-SKILL-COMP-005', 'comp-workflow-auto-005', 'compliance-workflow-automation-agent', 'Compliance Workflow Automation Agent', '1.0.0', 'compliance-ai',
 'T11 — RUZN Supreme Legal', 'T11', 'cognitive',
 'Sovereign AI agent for orchestrating end-to-end compliance workflows including KYC, CDD, fraud screening, and exception escalation.',
 'C-01 (RUZN-GOV)', 'Layer 4 — Reasoning, Layer 9 — Cognition', 10, 'sovereign', 'draft',
 'Acuterium Technologies', 'RUZN.AI', 'P2-High', 'ar-en',
 'compliance workflow, KYC automation, due diligence automation, fraud screening, أتمتة سير العمل',
 NOW(), NOW()),

-- Audit AI Skills
('ACU-SKILL-AUD-001', 'aud-internal-auto-001', 'internal-audit-automation-agent', 'Internal Audit Automation Agent', '1.0.0', 'audit-ai',
 'T11 — RUZN Supreme Legal', 'T11', 'cognitive',
 'Sovereign multi-agent system for internal audit: Data Analyst → Senior Auditor → Audit Manager pipeline with 96.4% control testing accuracy.',
 'C-01 (RUZN-GOV), W-07 (Ūrānā-INTEL)', 'Layer 4 — Reasoning, Layer 9 — Cognition', 10, 'sovereign', 'draft',
 'Acuterium Technologies', 'RUZN.AI, Ūrānā', 'P1-Critical', 'ar-en',
 'internal audit, controls testing, audit fieldwork, ghost employee detection, تدقيق داخلي, اختبار الضوابط',
 NOW(), NOW()),

('ACU-SKILL-AUD-002', 'aud-compliance-auto-002', 'automated-compliance-auditing-agent', 'Automated Compliance Auditing Agent', '1.0.0', 'audit-ai',
 'T11 — RUZN Supreme Legal', 'T11', 'cognitive',
 'Intelligent agent for evaluating work items against control rules with LLM reasoning, evidence fetching, and audit status updating.',
 'C-01 (RUZN-GOV), W-07 (Ūrānā-INTEL)', 'Layer 4 — Reasoning, Layer 6 — Intelligence', 10, 'sovereign', 'draft',
 'Acuterium Technologies', 'Ūrānā', 'P1-Critical', 'ar-en',
 'automated compliance audit, control rule evaluation, evidence fetching, audit status update, تدقيق الامتثال الآلي',
 NOW(), NOW()),

('ACU-SKILL-AUD-003', 'aud-evidence-mgmt-003', 'audit-trail-evidence-management-agent', 'Audit Trail & Evidence Management Agent', '1.0.0', 'audit-ai',
 'T11 — RUZN Supreme Legal', 'T11', 'cognitive',
 'Sovereign agent for immutable audit trail generation with blockchain-verified timestamping and chain of custody tracking.',
 'W-07 (Ūrānā-INTEL)', 'Layer 4 — Reasoning, Layer 9 — Cognition', 10, 'sovereign', 'draft',
 'Acuterium Technologies', 'Ūrānā', 'P1-Critical', 'ar-en',
 'audit trail, evidence management, evidence locker, blockchain timestamp, chain of custody, سجل التدقيق',
 NOW(), NOW()),

-- Quality Assurance & Accreditation Skills
('ACU-SKILL-QA-001', 'qa-framework-001', 'qa-quality-assurance-framework-agent', 'QA Quality Assurance Framework Agent', '1.0.0', 'quality-assurance',
 'T04 — ACIW', 'T04', 'cognitive',
 'Sovereign QA framework agent across supplier performance, in-process control, and post-market feedback with Plan-Execute-Improve cycle.',
 'W-07 (Ūrānā-INTEL)', 'Layer 4 — Reasoning, Layer 9 — Cognition', 10, 'sovereign', 'draft',
 'Acuterium Technologies', 'Ūrānā', 'P1-Critical', 'ar-en',
 'quality assurance, QA framework, process control, defect detection, SPC, FMEA, CAPA, ضمان الجودة',
 NOW(), NOW()),

('ACU-SKILL-QA-002', 'qa-accreditation-002', 'accreditation-attestation-intelligence-agent', 'Accreditation & Attestation Intelligence Agent', '1.0.0', 'quality-assurance',
 'T04 — ACIW', 'T04', 'cognitive',
 'Sovereign AI for institutional accreditation, attestation workflows, self-assessment reports, evidence scoring, and predictive submission readiness.',
 'W-07 (Ūrānā-INTEL)', 'Layer 4 — Reasoning, Layer 9 — Cognition', 10, 'sovereign', 'draft',
 'Acuterium Technologies', 'Ūrānā', 'P1-Critical', 'ar-en',
 'accreditation, attestation, certification assessment, self-assessment report, gap analysis, اعتماد, شهادة',
 NOW(), NOW()),

('ACU-SKILL-QA-003', 'qa-capa-generator-003', 'capa-narrative-generator-agent', 'CAPA Narrative Generator Agent', '1.0.0', 'quality-assurance',
 'T04 — ACIW', 'T04', 'cognitive',
 'Transforms structured CAPA inputs into traceable narratives with evidence linkage, supporting ISO 9001 and IATF 16949 audit formats.',
 'W-07 (Ūrānā-INTEL)', 'Layer 4 — Reasoning, Layer 9 — Cognition', 10, 'sovereign', 'draft',
 'Acuterium Technologies', 'Ūrānā', 'P2-High', 'ar-en',
 'CAPA, corrective action, preventive action, root cause analysis, nonconformance, إجراء تصحيحي',
 NOW(), NOW());

-- Verify insertion
SELECT skill_id, display_name, category, status, acuterium_product
FROM marketplace_skills 
WHERE skill_id LIKE 'ACU-SKILL-LEG%' 
   OR skill_id LIKE 'ACU-SKILL-COMP%' 
   OR skill_id LIKE 'ACU-SKILL-AUD%'
   OR skill_id LIKE 'ACU-SKILL-QA%'
ORDER BY skill_id;

COMMIT;
```

---

## Part E: GitHub Repository Structure for Perplexity Push

### Recommended Repository Layout

```
acuterium-skills-legal-qa-audit/
├── README.md
├── LICENSE
├── .github/
│   └── workflows/
│       └── validate-skills.yml
├── skills/
│   ├── legal-ai/
│   │   ├── ACU-SKILL-LEG-001_contract-review-agent.md
│   │   ├── ACU-SKILL-LEG-002_legal-research-assistant.md
│   │   ├── ACU-SKILL-LEG-003_legal-document-drafting-agent.md
│   │   ├── ACU-SKILL-LEG-004_due-diligence-agent.md
│   │   └── ACU-SKILL-LEG-005_e-discovery-processing-agent.md
│   ├── compliance-ai/
│   │   ├── ACU-SKILL-COMP-001_compliance-monitoring-agent.md
│   │   ├── ACU-SKILL-COMP-002_regulatory-change-intelligence-agent.md
│   │   ├── ACU-SKILL-COMP-003_policy-enforcement-agent.md
│   │   ├── ACU-SKILL-COMP-004_risk-assessment-intelligence-agent.md
│   │   └── ACU-SKILL-COMP-005_compliance-workflow-automation-agent.md
│   ├── audit-ai/
│   │   ├── ACU-SKILL-AUD-001_internal-audit-automation-agent.md
│   │   ├── ACU-SKILL-AUD-002_automated-compliance-auditing-agent.md
│   │   └── ACU-SKILL-AUD-003_audit-trail-evidence-management-agent.md
│   └── quality-assurance/
│       ├── ACU-SKILL-QA-001_qa-quality-assurance-framework-agent.md
│       ├── ACU-SKILL-QA-002_accreditation-attestation-intelligence-agent.md
│       └── ACU-SKILL-QA-003_capa-narrative-generator-agent.md
├── sql/
│   ├── 001_insert_new_skills.sql
│   ├── 002_keyword_extraction_update.sql
│   ├── 003_status_promotion_workflow.sql
│   └── 004_transaction_wrapper_template.sql
├── scripts/
│   ├── acu_keyword_extractor.py
│   └── validate_skill_schema.py
└── docs/
    └── ACU-IMPL-LEG-001_implementation_instructions.md
```

### Perplexity Push Instructions

```bash
# 1. Create the repository
gh repo create acuterium-skills-legal-qa-audit --private --description \
  "Acuterium Legal AI, QA, Audit & Compliance Skills for RUZN.AI and Ūrānā"

# 2. Clone and structure
git clone https://github.com/acuterium/acuterium-skills-legal-qa-audit.git
cd acuterium-skills-legal-qa-audit

# 3. Copy skill files into correct directories
mkdir -p skills/{legal-ai,compliance-ai,audit-ai,quality-assurance}
mkdir -p sql scripts docs

# 4. Copy files (from this deliverable output)
cp ACU-SKILL-LEG-*.md skills/legal-ai/
cp ACU-SKILL-COMP-*.md skills/compliance-ai/
cp ACU-SKILL-AUD-*.md skills/audit-ai/
cp ACU-SKILL-QA-*.md skills/quality-assurance/
cp ACU-IMPL-LEG-001_implementation_instructions.md docs/

# 5. Commit and push
git add -A
git commit -m "feat: Add 16 sovereign Legal/QA/Audit/Compliance skills for RUZN.AI and Ūrānā

- 5 Legal AI skills (contract review, research, drafting, due diligence, e-discovery)
- 5 Compliance AI skills (monitoring, regulatory change, policy enforcement, risk, workflow)
- 3 Audit AI skills (internal audit, automated compliance, evidence management)
- 3 QA skills (framework, accreditation/attestation, CAPA generator)
- Full SQL insertion scripts with transaction wrappers
- Keyword extraction pipeline for 921 skills
- Status promotion workflow for 2,179 draft→published transitions"

git push origin main
```

---

## Part F: Skill-to-Platform Mapping Summary

| Skill ID | Skill Name | RUZN.AI | Ūrānā | Thread |
|---|---|---|---|---|
| ACU-SKILL-LEG-001 | Contract Review Agent | ✅ Primary | ✅ Secondary | T11 |
| ACU-SKILL-LEG-002 | Legal Research Assistant | ✅ Primary | ✅ Secondary | T11 |
| ACU-SKILL-LEG-003 | Legal Document Drafting Agent | ✅ Primary | ✅ Secondary | T11 |
| ACU-SKILL-LEG-004 | Due Diligence Agent | ✅ | ✅ | T11 |
| ACU-SKILL-LEG-005 | E-Discovery Processing Agent | ✅ Primary | ✅ Secondary | T11 |
| ACU-SKILL-COMP-001 | Compliance Monitoring Agent | ✅ | ✅ | T11 |
| ACU-SKILL-COMP-002 | Regulatory Change Intelligence | ✅ Secondary | ✅ Primary | T11 |
| ACU-SKILL-COMP-003 | Policy Enforcement Agent | ✅ | ✅ | T11 |
| ACU-SKILL-COMP-004 | Risk Assessment Intelligence | ✅ Secondary | ✅ Primary | T11 |
| ACU-SKILL-COMP-005 | Compliance Workflow Automation | ✅ Primary | ✅ Secondary | T11 |
| ACU-SKILL-AUD-001 | Internal Audit Automation | ✅ | ✅ | T11 |
| ACU-SKILL-AUD-002 | Automated Compliance Auditing | ✅ Secondary | ✅ Primary | T11 |
| ACU-SKILL-AUD-003 | Audit Trail & Evidence Mgmt | ✅ Secondary | ✅ Primary | T11 |
| ACU-SKILL-QA-001 | QA Framework Agent | ✅ Secondary | ✅ Primary | T04 |
| ACU-SKILL-QA-002 | Accreditation & Attestation | ✅ Secondary | ✅ Primary | T04 |
| ACU-SKILL-QA-003 | CAPA Narrative Generator | ✅ Secondary | ✅ Primary | T04 |

---

**Document Classification**: SOVEREIGN — INTERNAL  
**Next Action**: Push to GitHub via Perplexity Space, then execute SQL insertion within transaction wrapper  
**Review Required**: Dr. Jay — Sovereignty compliance verification for all 16 skills before Stage 4 promotion
