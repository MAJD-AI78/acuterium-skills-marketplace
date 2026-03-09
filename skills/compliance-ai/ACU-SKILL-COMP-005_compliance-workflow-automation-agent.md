---
skill_id: ACU-SKILL-COMP-005
registry_id: comp-workflow-auto-005
name: compliance-workflow-automation-agent
display_name: Compliance Workflow Automation Agent
version: 1.0.0
category: compliance-ai
thread: "T11 — RUZN Supreme Legal"
thread_code: T11
domain: cognitive
shard_assignment: "C-01 (RUZN-GOV)"
sovereignty_score: 10
governance_level: sovereign
status: draft
author: Acuterium Technologies
acuterium_product: "RUZN.AI"
secondary_product: "Ūrānā"
priority: P2-High
localization_flag: ar-en
compatible_with: "Qwen-2.5, DeepSeek-R1"
license: Acuterium Sovereign License
trigger_keywords:
  - compliance workflow
  - due diligence automation
  - KYC automation
  - fraud screening
  - workflow orchestration
  - أتمتة سير العمل
  - العناية الواجبة للعملاء
  - فحص الاحتيال
created_at: "2026-03-09T00:00:00Z"
updated_at: "2026-03-09T00:00:00Z"
---

# Compliance Workflow Automation Agent — SKILL.md

## 1. Purpose

Sovereign AI agent for orchestrating end-to-end compliance workflows including customer due diligence (CDD), KYC verification, fraud screening, document generation, case routing, and exception escalation. Sequences and prioritizes activities automatically while maintaining human-in-the-loop checkpoints for critical decisions.

## 2. Capabilities

- Automates customer due diligence and KYC workflows end-to-end
- Fraud screening against transaction patterns and behavioral analytics
- Document generation for compliance filings and regulatory submissions
- Intelligent case routing and priority queuing based on risk scores
- Exception escalation with automatic context packaging
- Multi-agent coordination: screening agent → review agent → approval agent
- Supports Omani AML/CFT requirements and CBO regulatory mandates

## 3. Implementation Architecture

```typescript
interface ComplianceWorkflow {
  workflowType: 'KYC' | 'CDD' | 'EDD' | 'SAR' | 'STR' | 'fraud_screening';
  subject: EntitySubject;
  dataInputs: DataSource[];
  riskLevel: 'standard' | 'enhanced' | 'simplified';
  approvalChain: Approver[];
  slaMinutes: number;
}

async function executeComplianceWorkflow(workflow: ComplianceWorkflow): Promise<WorkflowResult> {
  const screened = await runScreeningAgent(workflow.subject, workflow.dataInputs);
  const reviewed = await runReviewAgent(screened, workflow.riskLevel);
  if (reviewed.requiresEscalation) {
    await escalateToHuman(reviewed, workflow.approvalChain);
  }
  const decision = await obtainDecision(reviewed);
  const documentation = await generateComplianceDocumentation(decision, workflow.workflowType);
  await archiveWorkflow(documentation);
  return { decision, documentation, processingTime: calculateSLA(workflow) };
}
```

## 4. Quality Metrics

| Metric | Target |
|---|---|
| Workflow completion rate | ≥ 98% |
| SLA adherence | ≥ 95% |
| Screening accuracy | ≥ 96% |
| Exception routing accuracy | ≥ 99% |
