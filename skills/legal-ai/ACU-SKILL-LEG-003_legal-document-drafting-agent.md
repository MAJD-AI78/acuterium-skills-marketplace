---
skill_id: ACU-SKILL-LEG-003
registry_id: leg-doc-draft-003
name: legal-document-drafting-agent
display_name: Legal Document Drafting Agent
version: 1.0.0
category: legal-ai
thread: "T11 — RUZN Supreme Legal"
thread_code: T11
domain: cognitive
shard_assignment: "C-01 (RUZN-GOV)"
layer_access: "Layer 4 — Reasoning, Layer 9 — Cognition"
sovereignty_score: 10
governance_level: sovereign
status: draft
author: Acuterium Technologies
acuterium_product: "RUZN.AI"
secondary_product: "Ūrānā"
priority: P1-Critical
localization_flag: ar-en
compatible_with: "Qwen-2.5, DeepSeek-R1, Claude Enterprise"
license: Acuterium Sovereign License
trigger_keywords:
  - document drafting
  - legal document generation
  - demand letter
  - motion drafting
  - legal correspondence
  - صياغة المستندات القانونية
  - إعداد المذكرات
  - خطاب المطالبة
created_at: "2026-03-09T00:00:00Z"
updated_at: "2026-03-09T00:00:00Z"
---

# Legal Document Drafting Agent — SKILL.md

## 1. Purpose

Sovereign AI agent for generating first drafts of legal documents — demand letters, motions, contracts, ministerial correspondence, and government memoranda. Adapts to organizational style guides, incorporates case-specific facts, and maintains bilingual Arabic/English formatting with RTL-native output.

## 2. Domain Mapping

| Dimension | Value |
|---|---|
| **Primary Platform** | RUZN.AI — Sovereign Legal Intelligence |
| **Secondary Platform** | Ūrānā — Regulatory Document Generation |
| **HISN AL-WUJŪD Shard** | C-01 (RUZN-GOV) |
| **Sovereignty Tier** | 10/10 |
| **Arabic NLP Engine** | Qwen-2.5 |

## 3. Capabilities

- Generates first drafts from templates, precedent documents, and structured inputs
- Adapts language, tone, and formality to match organizational style guides
- Incorporates case-specific facts, party details, and jurisdictional requirements
- Maintains consistent formatting per Omani government document standards
- Suggests alternative phrasing for diplomatic, assertive, or neutral tones
- Supports UDS-standard DOCX output with proper Arabic typographic conventions
- Tracks document versions with immutable audit trails

## 4. Implementation Architecture

```typescript
interface DraftingRequest {
  documentType: 'demand_letter' | 'motion' | 'contract' | 'memorandum' | 'ministerial_correspondence' | 'legal_opinion';
  facts: CaseFactSet;
  parties: Party[];
  jurisdiction: 'OM' | 'GCC';
  templateId?: string;
  styleGuideId: string;
  tone: 'diplomatic' | 'assertive' | 'neutral' | 'formal_government';
  language: 'ar' | 'en' | 'bilingual';
  outputFormat: 'docx' | 'pdf' | 'ruzn_native';
}

async function generateDraft(request: DraftingRequest): Promise<DraftOutput> {
  const template = await loadTemplate(request.templateId, request.documentType);
  const styleGuide = await loadStyleGuide(request.styleGuideId);
  const draft = await composeDraft(template, request.facts, request.parties, styleGuide);
  const formatted = await applyFormatting(draft, request.language, request.outputFormat);
  const alternatives = await generateAlternativePhrasing(draft, request.tone);
  await createAuditTrail(formatted, 'document-drafting');
  return { document: formatted, alternatives, metadata: extractMetadata(formatted) };
}
```

## 5. Trigger Keywords

```
document drafting, legal document generation, demand letter, motion drafting,
legal correspondence, ministerial memo, government memorandum, contract template,
legal opinion, formal letter, UDS document,
صياغة المستندات القانونية, إعداد المذكرات, خطاب المطالبة, مذكرة وزارية,
رأي قانوني, مراسلات حكومية
```

## 6. Quality Metrics

| Metric | Target |
|---|---|
| Draft generation time | ≤ 5 minutes |
| Template adherence | ≥ 98% |
| Drafting time reduction | ≥ 75% vs manual |
| Arabic typographic accuracy | ≥ 99% |
