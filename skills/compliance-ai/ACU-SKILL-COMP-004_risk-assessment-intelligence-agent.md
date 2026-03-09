---
skill_id: ACU-SKILL-COMP-004
registry_id: comp-risk-assess-004
name: risk-assessment-intelligence-agent
display_name: Risk Assessment Intelligence Agent
version: 1.0.0
category: compliance-ai
thread: "T11 — RUZN Supreme Legal"
thread_code: T11
domain: cognitive
shard_assignment: "W-07 (Ūrānā-INTEL)"
sovereignty_score: 10
governance_level: sovereign
status: draft
author: Acuterium Technologies
acuterium_product: "Ūrānā"
secondary_product: "RUZN.AI"
priority: P1-Critical
localization_flag: ar-en
compatible_with: "DeepSeek-R1, Qwen-2.5"
license: Acuterium Sovereign License
trigger_keywords:
  - risk assessment
  - compliance risk
  - predictive risk
  - risk scoring
  - risk matrix
  - sanctions screening
  - تقييم المخاطر
  - مخاطر الامتثال
  - فحص العقوبات
created_at: "2026-03-09T00:00:00Z"
updated_at: "2026-03-09T00:00:00Z"
---

# Risk Assessment Intelligence Agent — SKILL.md

## 1. Purpose

Sovereign AI agent for comprehensive compliance risk assessment. Analyzes historical data, entity profiles, transactions, and regulatory context to identify compliance risks proactively. Detects structured transactions designed to evade reporting thresholds, flags sanctioned entities, and predicts emerging risk trends using AI-powered modeling.

## 2. Capabilities

- Analyzes historical data, customer/entity profiles, and transactions for compliance risks
- Detects structured transactions designed to evade reporting thresholds (AML/CFT)
- Flags individuals and entities on sanctions lists across 247 jurisdictions
- Predictive modeling for early detection of emerging risk trends
- Risk matrix generation with severity/likelihood scoring
- Entity risk scoring with consciousness-weighted Compliance Assurance formula
- Integrates with Ūrānā's Legal Entity Intelligence Protocol (LEIP)

## 3. Implementation Architecture

```typescript
interface RiskAssessmentConfig {
  scope: 'entity' | 'transaction' | 'regulatory' | 'operational' | 'comprehensive';
  dataInputs: DataSource[];
  sanctionsLists: string[];
  jurisdictions: string[];
  riskModel: 'statistical' | 'ml_predictive' | 'hybrid';
  thresholds: RiskThresholds;
}

interface EntityRiskProfile {
  entityId: string;
  riskScore: number;             // 0-100
  riskCategory: 'critical' | 'high' | 'medium' | 'low';
  riskFactors: RiskFactor[];
  sanctionsHits: SanctionsMatch[];
  adverseMedia: AdverseMediaHit[];
  pepsScreening: PEPResult[];
  recommendations: string[];
}

async function assessRisk(config: RiskAssessmentConfig): Promise<RiskAssessmentReport> {
  const entityProfiles = await buildEntityProfiles(config.dataInputs);
  const sanctionsScreened = await screenAgainstSanctions(entityProfiles, config.sanctionsLists);
  const transactionPatterns = await analyzeTransactionPatterns(config.dataInputs);
  const predictiveRisks = await runPredictiveModeling(transactionPatterns, config.riskModel);
  const riskMatrix = await generateRiskMatrix(sanctionsScreened, predictiveRisks);
  return { entityProfiles: sanctionsScreened, transactionPatterns, predictiveRisks, riskMatrix };
}
```

## 4. Quality Metrics

| Metric | Target |
|---|---|
| Sanctions screening accuracy | ≥ 99.5% |
| Risk scoring precision | ≥ 93% |
| False positive rate | ≤ 3% |
| Predictive risk detection lead time | ≥ 30 days ahead |
