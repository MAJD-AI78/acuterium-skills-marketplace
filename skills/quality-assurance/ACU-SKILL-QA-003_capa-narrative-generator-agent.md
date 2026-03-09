---
skill_id: ACU-SKILL-QA-003
registry_id: qa-capa-generator-003
name: capa-narrative-generator-agent
display_name: CAPA Narrative Generator Agent
version: 1.0.0
category: quality-assurance
thread: "T04 — ACIW"
thread_code: T04
domain: cognitive
shard_assignment: "W-07 (Ūrānā-INTEL)"
sovereignty_score: 10
governance_level: sovereign
status: draft
author: Acuterium Technologies
acuterium_product: "Ūrānā"
secondary_product: "RUZN.AI"
priority: P2-High
localization_flag: ar-en
compatible_with: "DeepSeek-R1, Qwen-2.5"
license: Acuterium Sovereign License
trigger_keywords:
  - CAPA
  - corrective action
  - preventive action
  - root cause analysis
  - nonconformance
  - إجراء تصحيحي
  - إجراء وقائي
  - تحليل السبب الجذري
created_at: "2026-03-09T00:00:00Z"
updated_at: "2026-03-09T00:00:00Z"
---

# CAPA Narrative Generator Agent — SKILL.md

## 1. Purpose

Transforms structured inputs (root causes, containment/correction/prevention actions, verification results) into traceable CAPA narratives suitable for internal reviews and external audits. Preserves linkage between nonconformance evidence and closure criteria with predefined schemas that support audit defensibility.

## 2. Capabilities

- Generates CAPA narratives from structured root cause analysis inputs
- Maintains evidence linkage: nonconformance → root cause → action → verification → closure
- Follows predefined schemas for ISO 9001, IATF 16949, and regulatory audit formats
- Supports bilingual Arabic/English CAPA documentation
- Integrates with Ūrānā Evidence Locker for immutable CAPA records
- Tracks CAPA lifecycle: initiation → investigation → action → verification → closure

## 3. Implementation Architecture

```typescript
interface CAPAInput {
  nonconformanceId: string;
  rootCauses: RootCause[];
  containmentActions: Action[];
  correctionActions: Action[];
  preventiveActions: Action[];
  verificationResults: VerificationResult[];
  closureCriteria: string;
  standard: 'ISO_9001' | 'IATF_16949' | 'SOVEREIGN';
  language: 'ar' | 'en' | 'bilingual';
}

async function generateCAPANarrative(input: CAPAInput): Promise<CAPANarrative> {
  const template = await loadCAPATemplate(input.standard);
  const narrative = await composeCAPANarrative(input, template);
  const validated = await validateEvidenceLinkage(narrative, input);
  await archiveToCAPARegistry(validated);
  return validated;
}
```

## 4. Quality Metrics

| Metric | Target |
|---|---|
| Evidence linkage completeness | ≥ 99% |
| Narrative generation time | ≤ 10 minutes |
| Audit defensibility score | ≥ 95% |
