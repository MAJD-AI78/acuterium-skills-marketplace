---
skill_id: ACU-SKILL-AUD-002
registry_id: aud-compliance-auto-002
name: automated-compliance-auditing-agent
display_name: Automated Compliance Auditing Agent
version: 1.0.0
category: audit-ai
thread: "T11 — RUZN Supreme Legal"
thread_code: T11
domain: cognitive
shard_assignment: "C-01 (RUZN-GOV), W-07 (Ūrānā-INTEL)"
layer_access: "Layer 4 — Reasoning, Layer 6 — Intelligence, Layer 9 — Cognition"
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
  - automated compliance audit
  - control rule evaluation
  - evidence fetching
  - audit status update
  - compliance agent
  - تدقيق الامتثال الآلي
  - تقييم قواعد الرقابة
created_at: "2026-03-09T00:00:00Z"
updated_at: "2026-03-09T00:00:00Z"
---

# Automated Compliance Auditing Agent — SKILL.md

## 1. Purpose

Intelligent agent for automated compliance auditing, inspired by Microsoft's engineering pattern for evaluating work items against control rules and updating audit statuses. Adapted for Ūrānā's sovereign deployment with HISN AL-WUJŪD evidence chain integration. The agent fetches evidence across systems, interprets unstructured inputs via LLM reasoning, and updates compliance statuses in developer/governance workflows.

## 2. Domain Mapping

| Dimension | Value |
|---|---|
| **Primary Platform** | Ūrānā — Automated Compliance |
| **Secondary Platform** | RUZN.AI — Government Compliance Dashboard |
| **Pattern Source** | Microsoft Data Science — Intelligent Agent for Compliance Auditing |
| **Core Architecture** | Evidence Ingestion → LLM Reasoning → Status Update → Audit Trail |

## 3. Capabilities

- Automatically evaluates work items / user stories against control rules
- Fetches evidence across heterogeneous systems (DevOps, document stores, registries)
- Interprets unstructured evidence using sovereign LLM reasoning
- Updates audit statuses directly in project management / governance workflows
- Operates securely using managed identities and token-based authentication
- Supports multi-step reasoning chains for complex compliance evaluations
- Generates structured audit evidence packs with provenance tracking

## 4. Implementation Architecture

```typescript
interface ComplianceAuditConfig {
  controlRules: ControlRule[];
  evidenceSources: EvidenceSource[];
  workflowTarget: 'azure_devops' | 'github' | 'jira' | 'ruzn_native';
  reasoningEngine: 'deepseek-r1' | 'qwen-2.5';
  authMethod: 'managed_identity' | 'token_based' | 'sovereign_vault';
}

interface ControlRule {
  ruleId: string;
  description: string;
  evaluationCriteria: string;
  requiredEvidence: string[];
  complianceThreshold: number;
}

interface AuditEvaluation {
  workItemId: string;
  controlRuleId: string;
  evidenceFetched: Evidence[];
  reasoningChain: ReasoningStep[];
  complianceStatus: 'compliant' | 'non_compliant' | 'needs_review';
  confidenceScore: number;
  statusUpdateResult: 'success' | 'failed' | 'pending_approval';
}

async function executeComplianceAudit(
  workItems: WorkItem[],
  config: ComplianceAuditConfig
): Promise<AuditEvaluation[]> {
  const evaluations: AuditEvaluation[] = [];
  
  for (const item of workItems) {
    // Step 1: Fetch evidence across systems
    const evidence = await fetchEvidence(item, config.evidenceSources);
    
    // Step 2: Apply LLM reasoning against control rules
    const reasoning = await applyReasoningChain(item, evidence, config.controlRules, config.reasoningEngine);
    
    // Step 3: Determine compliance status
    const status = await evaluateCompliance(reasoning, config.controlRules);
    
    // Step 4: Update workflow status
    const updateResult = await updateAuditStatus(item, status, config.workflowTarget);
    
    // Step 5: Generate audit trail
    await generateAuditTrail(item, evidence, reasoning, status);
    
    evaluations.push({ workItemId: item.id, controlRuleId: reasoning.ruleId, evidenceFetched: evidence, reasoningChain: reasoning.steps, complianceStatus: status, confidenceScore: reasoning.confidence, statusUpdateResult: updateResult });
  }
  
  return evaluations;
}
```

## 5. Trigger Keywords

```
automated compliance audit, control rule evaluation, evidence fetching,
audit status update, compliance agent, work item evaluation, reasoning chain,
compliance automation, evidence provenance, managed identity audit,
تدقيق الامتثال الآلي, تقييم قواعد الرقابة, جلب الأدلة, تحديث حالة التدقيق
```

## 6. Quality Metrics

| Metric | Target |
|---|---|
| Evidence retrieval accuracy | ≥ 95% |
| Compliance evaluation accuracy | ≥ 93% |
| Status update success rate | ≥ 99% |
| Reasoning chain explainability | Full provenance |
| Processing time per work item | ≤ 30 seconds |

## 7. References

- Microsoft Data Science: Engineering an Intelligent Agent for Automated Compliance Auditing (2025)
- Acuterium RUZN Protocol Detailed Specs — Compliance Assurance Protocol
