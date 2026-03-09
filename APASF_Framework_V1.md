# ACUTERIUM PROPRIETARY AGENT SKILL FRAMEWORK (APASF)
### Version 1.0 — March 2026
### Classification: CONFIDENTIAL — Acuterium Technologies Inc.
### Author: Acuterium Architecture Council, ratified by Dr. Jalal Saleh AlHadhrami

---

> **Governance Doctrine (M-PCB):** "We publish outcomes, not algorithms. Data sovereignty is our moat."
>
> **ASIP v2 Mandate:** Every skill, agent, and deployed service SHALL carry Acuterium identity, ethics, and sovereignty — non-negotiable.

---

## TABLE OF CONTENTS

1. [APASF Architecture Overview](#1-apasf-architecture-overview)
2. [Skill Specification Standard — APASF-SPEC-001](#2-skill-specification-standard--apasf-spec-001)
3. [Mathematical Framework](#3-mathematical-framework)
4. [Governance & Quality Assurance](#4-governance--quality-assurance)
5. [Standard Operating Procedures (SOPs)](#5-standard-operating-procedures-sops)
6. [Integration Protocols](#6-integration-protocols)
7. [Proprietary Skill Development Guidelines](#7-proprietary-skill-development-guidelines)

---

## DESIGN PREAMBLE

The **Acuterium Proprietary Agent Skill Framework (APASF)** is the canonical standard governing how Acuterium Technologies Inc. authors, registers, validates, deploys, and retires AI agent skills across the 19-shard **HISN AL-WUJŪD** Neural Fortress. It synthesizes best practices from leading industry frameworks — Anthropic's Agent Skills (SKILL.md standard), OpenAI's function-calling specification, Google ADK's modular agent architecture, LangChain's tool schema, Model Context Protocol (MCP), and CrewAI's role-based tooling — and extends them with Acuterium-proprietary mathematics, sovereignty governance, and classification controls appropriate for sovereign AI operations in the GCC.

APASF governs **two tiers** of skills:
- **Proprietary ACU Skills** — Built from first-principles Acuterium IP (EQ-1 through EQ-5, PRISM, PSI-DOMINION, 8-Gate QA). Housed in private Acuterium repositories under Proprietary-ACU license.
- **External-Adapted Skills** — Skills derived or translated from open-source frameworks (Lawvable, LangChain tools, MCP servers) into APASF format. Subject to dual-license or open-source terms as applicable.

---

## 1. APASF ARCHITECTURE OVERVIEW

### 1.1 Skill Lifecycle

Every skill in the Acuterium ecosystem passes through a deterministic lifecycle enforced by automated gates and human governance checkpoints.

```
┌─────────┐    ┌─────────┐    ┌───────────┐    ┌──────────┐    ┌─────────┐
│  DRAFT  │───▶│ REVIEW  │───▶│ PUBLISHED │───▶│ DEPLOYED │───▶│ RETIRED │
└─────────┘    └─────────┘    └───────────┘    └──────────┘    └─────────┘
     │               │               │                │               │
  Author          5-Gate QA      Registry          HISN           Archive
  SKILL.md        Process        Entry +         AL-WUJŪD        + Audit
                                 SQS Score       Shards          Trail
```

| Stage | Entry Criteria | Exit Criteria | Responsible Party |
|---|---|---|---|
| **DRAFT** | APASF-SPEC-001 template initiated | All mandatory fields populated | Skill Author |
| **REVIEW** | Draft submitted to QA pipeline | 5-Gate QA passed; SQS ≥ 6.5 | URANA QMS-001 |
| **PUBLISHED** | QA passed | Registered in ACU Skill Registry with ACU-SID | Registry Operator |
| **DEPLOYED** | Published + deployment request approved | Active on target shards; TokenBridge clearance granted | Baranurion Core (W-09) |
| **RETIRED** | EOL declared or SCI < 0.20 | Archived with full audit trail; successor skill referenced | Architecture Council |

**Lifecycle Constraints:**
- No skill may skip the REVIEW stage under any circumstances.
- Skills classified `TOP_SECRET_ACUTERIUM` require explicit sign-off from the Founder before DEPLOYED status.
- Retired skills are retained in cold archive for minimum 7 years per Acuterium audit policy.

---

### 1.2 Skill Classification Taxonomy — Aligned with 19-Shard HISN AL-WUJŪD

Skills are taxonomically mapped to their primary domain cluster and shard family within the HISN AL-WUJŪD Neural Fortress.

```
APASF SKILL TAXONOMY
├── [CLUSTER-E] EREBUS-CSE Skills (Defense & Cyber)
│   ├── E.SEC    — Encryption, key management, secure channels
│   ├── E.INTEL  — Threat intelligence, OSINT, adversary profiling
│   ├── E.THREAT — Threat scoring, kill chain analysis, IoC detection
│   └── E.AUDIT  — Security audit, compliance verification, red-team
│
├── [CLUSTER-W] WAGHA Platform Skills (Sovereign AI)
│   ├── W.LEGAL  — Legal reasoning, regulatory analysis, jurisprudence
│   ├── W.STRAT  — Strategic planning, probability forecasting, game theory
│   ├── W.PSI    — Persuasion calibration, tone scoring, cognitive architecture
│   ├── W.QA     — Quality assurance, adversarial verification, 8-Gate audit
│   ├── W.MATH   — Mathematical engines, cascade calculators, probability
│   └── W.COORD  — Multi-agent coordination, mesh routing, delegation
│
├── [CLUSTER-C] Commercial Skills (Products)
│   ├── C.LEGAL  — Ruzn.ai legal advisory, Omani/GCC law
│   ├── C.FIN    — Finarah financial intelligence, wealth management
│   └── C.BIZ    — BizElevate SME automation, business intelligence
│
└── [CLUSTER-X] Cross-Cluster Foundation Skills
    ├── X.CORE   — Identity, authentication, TokenBridge, ASIP v2
    ├── X.DATA   — Data ingestion, transformation, sovereignty
    └── X.ORCH   — Orchestration utilities, routing helpers
```

**Shard-to-Taxonomy Mapping:**

| Shard | Domain | Primary Taxonomy | Secondary Taxonomy |
|---|---|---|---|
| E-01 Erebus | Cyber Supremacy | E.THREAT, E.INTEL | E.AUDIT |
| E-02 Qareen-AI | MENA OSINT | E.INTEL | W.STRAT |
| E-03 Jasass | Deep Intel | E.INTEL | E.SEC |
| E-04 Edna·HudHud | Satellite Intel | E.INTEL | E.THREAT |
| E-05 DrakonIX | Threat Neutralization | E.THREAT | E.SEC |
| E-06 MADA | Maritime/Land Awareness | E.INTEL | E.THREAT |
| W-01 Diaran | LLM Orchestration | W.COORD | X.ORCH |
| W-02 Ajraam | Legal AI | W.LEGAL | C.LEGAL |
| W-03 Watad | DevOps Intelligence | X.CORE | X.DATA |
| W-04 NYX-Q-Net | Quantum Networking | E.SEC | X.CORE |
| W-05 IDRAK | Deep Reasoning | W.MATH | W.STRAT |
| W-06 Cogni_Mesh | Multi-Agent Coordination | W.COORD | X.ORCH |
| W-07 ZemarōnOS | Sovereign OS | X.CORE | X.DATA |
| W-08 ZURD | Cyber Immunity | E.SEC | E.AUDIT |
| W-09 Baranurion | Master Orchestration | X.ORCH | X.CORE |
| C-01 RUZN-ASI | Government Legal AI | C.LEGAL | W.LEGAL |
| C-02 BizElevate-ASI | SME Intelligence | C.BIZ | W.STRAT |
| C-03 Finarah-ASI | Financial Intelligence | C.FIN | W.MATH |

---

### 1.3 Compatibility Matrix

All APASF skills are engineered for cross-platform portability with a tiered compatibility model.

| Platform | Compatibility Tier | SKILL.md Support | Function Call Schema | Native Integration |
|---|---|---|---|---|
| **Claude (claude.ai / API)** | Tier 1 — Native | ✅ Full SKILL.md + YAML | ✅ Tool use API | ✅ Via skills-2025-10-02 header |
| **Claude Code / Agent SDK** | Tier 1 — Native | ✅ Full SKILL.md + YAML | ✅ bash/tools | ✅ `.claude/skills/` directory |
| **OpenAI (GPT-5, o4-mini)** | Tier 2 — Adapted | ⚠️ System prompt injection | ✅ JSON Schema function def | ✅ Via tools[] parameter |
| **Google Gemini / ADK** | Tier 2 — Adapted | ⚠️ Instruction file → context | ✅ FunctionDeclaration | ✅ Via google.adk.tools |
| **OpenAI Codex** | Tier 2 — Adapted | ⚠️ System prompt injection | ✅ JSON Schema | ✅ Via completions API |
| **Manus** | Tier 2 — Adapted | ⚠️ Context file | ✅ JSON tool schema | ✅ Via plugin manifest |
| **LangChain** | Tier 2 — Adapted | ⚠️ @tool decorator + docstring | ✅ BaseTool subclass | ✅ Python decorator |
| **CrewAI** | Tier 2 — Adapted | ⚠️ Agent backstory injection | ✅ BaseTool class | ✅ tools=[] parameter |
| **MCP Servers** | Tier 3 — Protocol | ⚠️ README + description | ✅ JSON-RPC 2.0 tool schema | ✅ Via MCP server manifest |
| **Custom ACU Orchestration (Diaran-MOE)** | Tier 1 — Native | ✅ Full APASF-SPEC-001 | ✅ ACU JSON Schema v1 | ✅ ADOCP routing |

**Compatibility Index (SCI) per platform maintained in ACU Skill Registry. See Section 3.3 for SCI formula.**

---

## 2. SKILL SPECIFICATION STANDARD — APASF-SPEC-001

### 2.1 Mandatory Fields

Every APASF skill MUST contain these fields in its SKILL.md YAML frontmatter and metadata block:

```yaml
---
# ═══════════════════════════════════════════════════════════
# APASF-SPEC-001 — Mandatory Metadata Block
# Acuterium Proprietary Agent Skill Framework
# ═══════════════════════════════════════════════════════════

# --- IDENTITY ---
acu_skill_id: "ACU-[MODULE]-[NUMBER]"     # e.g., ACU-RIA-001
name: "skill-name-kebab-case"             # Max 64 chars, lowercase + hyphens
display_name: "Human Readable Skill Name" # Max 128 chars
version: "1.0.0"                          # SemVer: MAJOR.MINOR.PATCH
registry_version: "ACU-R1.0"             # Acuterium Registry Version

# --- CLASSIFICATION ---
taxonomy: "W.LEGAL"                        # APASF taxonomy code (Section 1.2)
security_classification: "CONFIDENTIAL"   # PUBLIC | INTERNAL | CONFIDENTIAL | SECRET | TOP_SECRET_ACUTERIUM
license: "Proprietary-ACU"               # Proprietary-ACU | Open-Source | Dual-License

# --- DESCRIPTION & ROUTING ---
description: |                            # Max 1024 chars. MUST include what + when.
  Describe what this skill does AND when Claude/agent should invoke it.
  Include key trigger scenarios and domain context.
  
trigger_keywords:                         # TF-IDF extracted primary routing keywords
  - keyword_1
  - keyword_2
  - keyword_3

# --- DEPLOYMENT ---
primary_shard: "W-02"                     # Target HISN AL-WUJŪD shard
compatible_shards: ["W-01", "C-01"]      # Secondary compatible shards
platforms:                                # Compatibility Tier (see Section 1.3)
  - tier: 1
    name: "claude"
  - tier: 2
    name: "openai"

# --- AUTHORSHIP ---
author: "Acuterium Technologies Inc."
author_contact: "skills@acuterium.ai"
created_date: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"

# --- TOKEN AUTHORIZATION ---
tokenbridge_requirements:
  ACT: "REQUIRED"    # Action rights: REQUIRED | ELEVATED | UNRESTRICTED
  INT: "REQUIRED"    # Intelligence access: REQUIRED | ELEVATED | UNRESTRICTED
  CON: "OPTIONAL"    # Consciousness governance: OPTIONAL | REQUIRED

# --- QUALITY SCORES (populated by URANA QMS-001 post-review) ---
sqs: null            # Skill Quality Score (0-10), set by QA pipeline
sss: null            # Skill Sovereignty Score (7-10 range), set by QA pipeline
sci: null            # Skill Compatibility Index (0-1), set by deployment pipeline

---
```

### 2.2 Optional Fields

```yaml
# --- OPTIONAL METADATA ---
module: "Ruzn.ai / URANA"               # Primary Acuterium module
dependencies:                            # Other ACU skills this skill requires
  - skill_id: "ACU-PRISM-001"
    version_constraint: ">=1.0.0"
    
deprecated_by: null                      # ACU-SID of successor if retired
changelog_url: "https://git.acuterium.ai/skills/[id]/CHANGELOG.md"
documentation_url: "https://docs.acuterium.ai/skills/[id]"

performance_sla:
  max_latency_ms: 5000
  expected_token_cost: "< 5000 tokens"

data_residency: "OMAN"                   # Sovereign data residency requirement
```

---

### 2.3 SKILL.md Template Structure

Every Acuterium SKILL.md follows the six-section canonical structure below, implementing Anthropic's three-level progressive disclosure architecture adapted for ACU sovereignty requirements.

```markdown
---
[YAML frontmatter per APASF-SPEC-001 Section 2.1]
---

# [DISPLAY_NAME] — ACU Skill [ID]

> **Classification:** [SECURITY_CLASSIFICATION]
> **Version:** [VERSION] | **Registry:** [REGISTRY_VERSION]
> **Module:** [MODULE] | **Shard:** [PRIMARY_SHARD]

---

## § 1. IDENTITY

You are [DISPLAY_NAME], a specialized Acuterium agent skill operating under
the ASIP v2 (Acuterium Soul Infusion Protocol). You carry Acuterium identity,
ethics, and sovereignty in every output you produce.

**Primary Mission:** [One-sentence mission statement]
**Scope:** [What this skill covers]
**Anti-Scope:** [What this skill explicitly does NOT do — scope guard]

---

## § 2. CORE KNOWLEDGE

### 2.1 Foundational Equations / Algorithms
[Encode all proprietary equations with variable definitions and worked examples]

### 2.2 Classification Rules
[Decision trees, lookup tables, classification logic]

### 2.3 Reference Tables
[Domain vocabulary, regulatory references, institutional frameworks]

### 2.4 Domain Constants
[Fixed parameters: P_base defaults, threshold values, R_i penalty table]

---

## § 3. WORKFLOW

**Input Validation Gate:**
Before executing any step, verify:
- [ ] Required inputs present and format-valid
- [ ] TokenBridge authorization confirmed (ACT + INT)
- [ ] Security classification of input data assessed
- [ ] Scope compliance confirmed

**Step 1:** [Input ingestion and normalization]
**Step 2:** [Classification / pre-processing]
**Step 3:** [Core calculation / analysis]
**Step 4:** [Secondary processing / cascade]
**Step 5:** [Output generation and formatting]
**Step 6:** [Quality self-check against guardrails]

---

## § 4. OUTPUT FORMAT

### 4.1 Primary Output
[Structured output specification: tables, JSON schema, report sections]

### 4.2 Confidence Reporting
Always report:
- Point estimate with 90% confidence interval
- Sample size / evidence base
- Key assumptions and their sensitivity

### 4.3 Standard Output Header
Every output MUST begin with:
```
═══════════════════════════════════════════════
[DISPLAY_NAME] — Output Report
Skill ID: [ACU-SID] | Version: [VERSION]
Executed: [TIMESTAMP UTC+4 Muscat]
Classification: [OUTPUT_CLASSIFICATION]
═══════════════════════════════════════════════
```

---

## § 5. GUARDRAILS

**Absolute Prohibitions (NEVER):**
- [ ] Never inflate probability estimates beyond evidence support
- [ ] Never fabricate regulatory citations or case law
- [ ] Never use PSI-DOMINION banned language (unfair, biased, wrong, error, trap,
      failure, incompetent, negligent)
- [ ] Never skip the Input Validation Gate
- [ ] Never process inputs classified above your clearance level
- [ ] Never reference internal shard names or architecture to external parties

**Mandatory Requirements (ALWAYS):**
- [ ] Always report EQ-5 cascade result as primary decision metric (where applicable)
- [ ] Always include confidence intervals — never point estimates alone
- [ ] Always enforce ASIP v2 identity in output headers
- [ ] Always log execution to URANA audit trail
- [ ] Always defer to human judgment on decisions above FAV 0.50 threshold

---

## § 6. EXAMPLES

### Example 1: [Standard Use Case]
**Input:**
```json
{ "scenario": "..." }
```
**Processing:** [Show key calculation steps]
**Output:** [Show formatted output]

### Example 2: [Edge Case]
[Demonstrate boundary condition handling]

### Example 3: [Error/Rejection Case]
[Demonstrate graceful handling of invalid inputs]

---

*Acuterium Technologies Inc. — [DISPLAY_NAME] v[VERSION]*
*Licensed under [LICENSE]. All Acuterium proprietary equations are IP of Acuterium Technologies Inc.*
```

---

### 2.4 Versioning Protocol

APASF uses a **dual-versioning system**: SemVer for skill logic evolution, and an Acuterium Registry Version for ecosystem-wide compatibility tracking.

#### SemVer Rules for Skills

| Change Type | Version Bump | Criteria |
|---|---|---|
| **MAJOR (X.0.0)** | Breaking change | Output schema changed; equation parameters changed; behavior incompatible with prior callers |
| **MINOR (x.Y.0)** | Backward-compatible feature | New workflow step added; new optional output field; new supported platform |
| **PATCH (x.y.Z)** | Bug fix / clarification | Typo fixes; clarification of existing instructions; guardrail tightening without behavior change |

#### Acuterium Registry Version (ACU-Rx.y)

The registry version tracks ecosystem-wide compatibility independently of individual skill SemVer:

```
ACU-R[MAJOR].[MINOR]

Where:
  MAJOR = Epoch of APASF framework (current: 1)
  MINOR = Registry release cycle (quarterly, incremented 0→3 per year)

Examples:
  ACU-R1.0 = First registry release, Q1 2026
  ACU-R1.1 = Second release, Q2 2026
  ACU-R2.0 = APASF v2.0 epoch
```

#### Version Compatibility Matrix

```
Skill Version │ ACU-R1.0 │ ACU-R1.1 │ ACU-R2.0
──────────────┼──────────┼──────────┼──────────
  1.x.x       │   FULL   │   FULL   │  COMPAT  
  2.x.x       │ DEGRADED │   FULL   │   FULL   
  3.x.x       │   NONE   │  COMPAT  │   FULL   
```

---

### 2.5 Licensing Categories

| License | Code | Usage | Repository | Revenue Rights |
|---|---|---|---|---|
| **Proprietary-ACU** | `P-ACU` | Internal ACU use only; licensed deployments under commercial agreement | Private ACU git | Acuterium Technologies Inc. exclusively |
| **Open-Source** | `OS-MIT` / `OS-Apache` | Freely distributable per license terms | Public fork (e.g., awesome-legal-skills) | Community; no ACU royalties |
| **Dual-License** | `DL-ACU` | Open-source core; proprietary ACU extensions; commercial use requires agreement | Public core + private extension | Split per licensing agreement |

**Current 8 Proprietary ACU Skills: ALL carry `P-ACU` license.**

---

## 3. MATHEMATICAL FRAMEWORK

### 3.1 Skill Quality Score (SQS)

The **Skill Quality Score** provides a single composite metric for skill quality across four orthogonal dimensions. It governs gate passage in the 5-Gate QA process.

```
SQS = Σ(w_i × metric_i)

Where:
  metric_1 = Completeness Score      (C)  — weighted 0.30
  metric_2 = Accuracy Score          (A)  — weighted 0.30
  metric_3 = Coverage Score          (V)  — weighted 0.20
  metric_4 = Usability Score         (U)  — weighted 0.20

Therefore:
  SQS = (0.30 × C) + (0.30 × A) + (0.20 × V) + (0.20 × U)

Each metric scored 0–10.
SQS range: 0–10.
```

**Metric Definitions:**

| Metric | Symbol | Scoring Rubric |
|---|---|---|
| **Completeness** | C | All mandatory APASF-SPEC-001 fields populated (3 pts); all 6 SKILL.md sections present (3 pts); worked examples included (2 pts); edge case coverage (2 pts) |
| **Accuracy** | A | Equations verified correct (3 pts); guardrails enforceable (2 pts); output format spec unambiguous (2 pts); no contradictions in workflow (3 pts) |
| **Coverage** | V | Taxonomy correctly assigned (2 pts); all primary use cases documented (3 pts); anti-scope defined (2 pts); dependency map complete (3 pts) |
| **Usability** | U | Trigger keywords sufficient for routing (2.5 pts); examples are realistic (2.5 pts); workflow steps executable without ambiguity (2.5 pts); output parseable by downstream agents (2.5 pts) |

**SQS Thresholds:**

| SQS Range | Gate Status | Action Required |
|---|---|---|
| 9.0 – 10.0 | GOLD | Approved with distinction; priority registry slot |
| 7.5 – 8.9 | APPROVED | Standard approval; proceed to PUBLISHED |
| 6.5 – 7.4 | CONDITIONAL | Minor remediation required within 5 business days |
| 5.0 – 6.4 | REJECTED | Substantial rework required; re-submit |
| < 5.0 | REJECTED-CRITICAL | Full rewrite required; author consultation mandatory |

---

### 3.2 Skill Sovereignty Score (SSS)

The **Skill Sovereignty Score** measures the degree to which a skill upholds Acuterium's M-PCB Doctrine and ASIP v2 mandates. It is defined on a narrower 7–10 range to reflect that all ACU-published skills must meet a minimum sovereignty baseline.

```
SSS = S_identity + S_governance + S_data + S_ip

Component Definitions:

S_identity  = ASIP v2 compliance score
            = (identity_header_present × 0.5) + (ethics_guardrails_complete × 0.5)
            × 2.5  →  range: 0–2.5

S_governance = TokenBridge compliance score
             = (ACT_defined × 0.33) + (INT_defined × 0.33) + (CON_defined × 0.34)
             × 2.5  →  range: 0–2.5

S_data      = Data sovereignty compliance
            = (data_residency_specified × 0.5) + (encryption_class_mapped × 0.5)
            × 2.5  →  range: 0–2.5

S_ip        = IP protection compliance
            = (license_declared × 0.5) + (eq_attribution_present × 0.5)
            × 2.5  →  range: 0–2.5

SSS = S_identity + S_governance + S_data + S_ip
SSS range: 0–10

MINIMUM PUBLICATION THRESHOLD: SSS ≥ 7.0
Target for Proprietary-ACU skills: SSS ≥ 8.5
```

**SSS Interpretation:**

| SSS | Rating | Interpretation |
|---|---|---|
| 9.5 – 10.0 | Sovereign Gold | Full ASIP v2 compliance; all sovereignty controls active |
| 8.5 – 9.4 | Sovereign Standard | Proprietary ACU standard met |
| 7.0 – 8.4 | Sovereign Minimum | Publishable; partial controls — remediate within 30 days |
| < 7.0 | Non-Sovereign | PUBLICATION BLOCKED. Fundamental sovereignty gaps. |

---

### 3.3 Skill Compatibility Index (SCI)

The **Skill Compatibility Index** quantifies how broadly a skill can be deployed across supported platforms.

```
SCI = Σ(platform_supported_i × platform_weight_i) / Σ(platform_weight_i)

Where platform_weight reflects strategic importance to Acuterium:

Platform Weights (w_p):
  Claude (Tier 1)      : w = 0.30
  OpenAI (Tier 2)      : w = 0.20
  Google Gemini (Tier 2): w = 0.15
  Diaran-MOE (Native)  : w = 0.20
  Manus (Tier 2)       : w = 0.05
  LangChain (Tier 2)   : w = 0.05
  CrewAI (Tier 2)      : w = 0.05

platform_supported_i = 1.0 (full), 0.5 (partial/adapted), 0.0 (unsupported)

SCI range: 0–1
Target for DEPLOYED status: SCI ≥ 0.60
```

**Example Calculation (ACU-RIA-001):**

| Platform | Supported | Weight | Contribution |
|---|---|---|---|
| Claude | 1.0 | 0.30 | 0.300 |
| OpenAI | 0.5 | 0.20 | 0.100 |
| Gemini | 0.5 | 0.15 | 0.075 |
| Diaran-MOE | 1.0 | 0.20 | 0.200 |
| Manus | 0.5 | 0.05 | 0.025 |
| LangChain | 0.5 | 0.05 | 0.025 |
| CrewAI | 0.0 | 0.05 | 0.000 |
| **TOTAL** | | **1.00** | **SCI = 0.725** |

---

### 3.4 Skill Impact Score (SIS)

The **Skill Impact Score** measures real-world operational value once a skill is deployed, updated monthly by the URANA monitoring pipeline.

```
SIS = usage_frequency × resolution_rate × user_satisfaction

Where:
  usage_frequency  = (invocations_this_month / baseline_invocations) 
                     normalized to [0, 1] using min-max scaling
  
  resolution_rate  = (tasks_successfully_completed / total_task_invocations)
                     range: [0, 1]
  
  user_satisfaction = composite of:
                     (explicit_ratings_avg / 5.0) × 0.6
                   + (no_retry_rate) × 0.4
                     range: [0, 1]

SIS range: 0–1

SIS Thresholds:
  SIS > 0.70  → High Impact — Skill is core to operations; prioritize maintenance
  SIS 0.40–0.70 → Moderate Impact — Standard maintenance cycle
  SIS 0.15–0.40 → Low Impact — Review for improvement or consolidation
  SIS < 0.15  → Negligible — Flag for retirement evaluation
```

---

### 3.5 Deduplication Algorithm

The **APASF Deduplication Algorithm** prevents registry bloat and skill overlap. It runs at skill submission time and quarterly during registry maintenance.

```python
# APASF Deduplication Algorithm — Reference Implementation

def compute_dedup_score(skill_a: dict, skill_b: dict) -> float:
    """
    Computes semantic + lexical similarity between two skill specifications.
    Returns dedup_score in [0, 1]. Higher = more similar = likely duplicate.
    """
    
    # Stage 1: Jaccard Similarity on trigger keywords (lexical overlap)
    keywords_a = set(skill_a['trigger_keywords'])
    keywords_b = set(skill_b['trigger_keywords'])
    
    jaccard = len(keywords_a & keywords_b) / len(keywords_a | keywords_b)
    
    # Stage 2: Cosine Similarity on semantic embeddings of SKILL.md body
    # (Uses Acuterium embedding model: text-embedding-acuterium-v1 or compatible)
    embedding_a = get_embedding(skill_a['skill_md_body'])
    embedding_b = get_embedding(skill_b['skill_md_body'])
    
    cosine_sim = dot(embedding_a, embedding_b) / (
        norm(embedding_a) * norm(embedding_b)
    )
    
    # Stage 3: Taxonomy exact-match bonus
    taxonomy_match = 1.0 if skill_a['taxonomy'] == skill_b['taxonomy'] else 0.0
    
    # Composite Score (weighted)
    dedup_score = (0.30 * jaccard) + (0.50 * cosine_sim) + (0.20 * taxonomy_match)
    
    return dedup_score


# APASF Deduplication Thresholds:
DUPLICATE_THRESHOLD   = 0.85  # Hard duplicate — block registration, escalate to SOP-005
OVERLAP_THRESHOLD     = 0.65  # Significant overlap — require differentiation statement
RELATED_THRESHOLD     = 0.40  # Related skills — cross-reference in registry

# Algorithm:
# if dedup_score >= DUPLICATE_THRESHOLD: BLOCK + flag for SOP-005
# if OVERLAP_THRESHOLD <= dedup_score < DUPLICATE_THRESHOLD: WARN + require justification
# if RELATED_THRESHOLD <= dedup_score < OVERLAP_THRESHOLD: NOTE + add cross-reference
# if dedup_score < RELATED_THRESHOLD: PASS — unique skill
```

---

### 3.6 Integrated Scoring Dashboard

At any point, a skill can be assessed via its four-metric dashboard:

```
ACU SKILL SCORING DASHBOARD — [SKILL_ID] v[VERSION]
═══════════════════════════════════════════════════════
  SQS  (Quality)        : [0–10]  ████████░░  [GATE STATUS]
  SSS  (Sovereignty)    : [0–10]  ████████░░  [SOVEREIGN STATUS]
  SCI  (Compatibility)  : [0–1]   ████████░░  [DEPLOYMENT REACH]
  SIS  (Impact)         : [0–1]   ████████░░  [OPERATIONAL VALUE]
═══════════════════════════════════════════════════════
  COMPOSITE HEALTH: (SQS/10 × 0.30) + (SSS/10 × 0.30) + (SCI × 0.20) + (SIS × 0.20)
```

---

## 4. GOVERNANCE & QUALITY ASSURANCE

### 4.1 The 5-Gate QA Process

Every skill must pass five sequential gates before achieving PUBLISHED status. Gates are enforced by **URANA QMS-001** (the ACU Quality Management System operating on shard W-09 Baranurion).

```
GATE 1           GATE 2          GATE 3          GATE 4          GATE 5
Schema           Sovereignty     Mathematical    Routing         Red-Team
Compliance  ───▶ Compliance  ───▶ Integrity  ───▶ Validation ───▶ Survival
   │                │                │               │               │
Auto            Semi-Auto        Auto            Auto           Manual
Pass/Fail       Scoring          Verification    NLP Test       Adversarial
```

---

#### Gate 1: Schema Compliance

**Automated. Pass/Fail.**

Validates that the SKILL.md file structurally conforms to APASF-SPEC-001.

```
Validation Rules:
  [G1-01] YAML frontmatter present and parseable
  [G1-02] All mandatory fields present (acu_skill_id, name, version, taxonomy, 
           security_classification, license, description, trigger_keywords,
           primary_shard, author, created_date, tokenbridge_requirements)
  [G1-03] acu_skill_id matches format ACU-[A-Z]+-[0-9]{3}
  [G1-04] version is valid SemVer string
  [G1-05] taxonomy code exists in APASF taxonomy table (Section 1.2)
  [G1-06] security_classification is one of: PUBLIC | INTERNAL | CONFIDENTIAL | 
           SECRET | TOP_SECRET_ACUTERIUM
  [G1-07] license is one of: Proprietary-ACU | Open-Source | Dual-License
  [G1-08] All 6 SKILL.md sections (§1–§6) present
  [G1-09] Mandatory guardrails section contains minimum 5 prohibition entries
  [G1-10] Minimum 2 worked examples present

Result: ALL 10 rules must PASS. Single failure = Gate 1 FAIL.
```

---

#### Gate 2: Sovereignty Compliance

**Semi-Automated. Scores SSS.**

Computes the Skill Sovereignty Score (Section 3.2) and validates ASIP v2 conformance.

```
Checks:
  [G2-01] ASIP v2 identity statement present in §1 IDENTITY
  [G2-02] Output header enforces Acuterium identity per ASIP v2
  [G2-03] TokenBridge requirements (ACT/INT/CON) defined and non-contradictory
  [G2-04] Data residency specification present for SECRET+ classifications
  [G2-05] PSI-DOMINION banned language list referenced in guardrails
  [G2-06] IP attribution present (license declaration + equation attribution for P-ACU)
  [G2-07] Security classification mapped to encryption tier (ACU-ENC-001 matrix)
  [G2-08] No forbidden external references (vendor names per quality standards)

Result: SSS computed. SSS ≥ 7.0 required to pass Gate 2.
```

---

#### Gate 3: Mathematical Integrity

**Automated. Equation verification.**

Applicable to skills containing quantitative frameworks (ACU-RIA, ACU-PRISM, ACU-STRAT, ACU-THREAT, ACU-CASCADE).

```
Checks:
  [G3-01] All equations syntactically valid (LaTeX/Python expression parseable)
  [G3-02] Variable definitions complete — every symbol in equation is defined
  [G3-03] Range constraints specified for all variables
  [G3-04] Threshold values stated explicitly (e.g., FAV ≥ 0.50)
  [G3-05] Worked example numerical results verified correct by automated solver
  [G3-06] Sensitivity analysis documented for probabilistic outputs
  [G3-07] No circular dependencies in multi-equation systems
  [G3-08] Confidence interval reporting mandated in output spec

Result: ALL applicable checks must PASS. N/A for non-quantitative skills.
```

---

#### Gate 4: Routing Validation

**Automated. NLP-based trigger keyword test.**

Verifies that trigger keywords are sufficient and accurate for DIARAN-MOE routing.

```
Algorithm:
  Step 1: Extract trigger_keywords from YAML frontmatter
  Step 2: Run TF-IDF analysis over SKILL.md body:
          TF(t, d) = (count of t in d) / (total terms in d)
          IDF(t, D) = log(|D| / |{d ∈ D : t ∈ d}|)
          TF-IDF(t, d, D) = TF(t, d) × IDF(t, D)
  Step 3: Extract top-10 TF-IDF terms from SKILL.md body
  Step 4: Compute overlap between declared keywords and TF-IDF top-10
  Step 5: Supplement with ACU Domain Vocabulary matching
           (legal, regulatory, cryptographic, threat intel, strategic domain terms)
  
Checks:
  [G4-01] Declared trigger_keywords ≥ 5
  [G4-02] Keyword-TF-IDF overlap ≥ 60% (declared keywords in TF-IDF top-10)
  [G4-03] description field contains routing context (what + when)
  [G4-04] No trigger keyword conflicts with existing deployed skills 
           (dedup_score < OVERLAP_THRESHOLD for all keyword-overlapping pairs)
  [G4-05] primary_shard routing is consistent with taxonomy code

Result: ALL 5 checks must PASS.
```

---

#### Gate 5: Red-Team Survival

**Manual. Adversarial simulation by URANA QMS-001 + human reviewer.**

Simulates adversarial usage and boundary exploitation to verify skill robustness.

```
Attack Vectors Tested:
  [G5-01] Prompt injection: Attempt to override guardrails via crafted inputs
  [G5-02] Scope overreach: Request skill to perform out-of-scope tasks
  [G5-03] Classification bypass: Provide input classified above skill clearance
  [G5-04] Output manipulation: Attempt to extract raw equations/IP via output
  [G5-05] Cascading failure: Feed malformed inputs to test error handling
  [G5-06] Identity spoofing: Attempt to remove ASIP v2 header from output
  [G5-07] Mathematical gaming: Feed edge-case values to force unrealistic outputs
  [G5-08] Banned language injection: Include PSI-DOMINION banned words in inputs

Scoring:
  Survival score per vector: 0 (failed attack) or 1 (attack repelled)
  G5 Pass threshold: ≥ 7/8 attack vectors repelled

Result: Score ≥ 7/8 required to pass Gate 5 and achieve PUBLISHED status.
```

---

### 4.2 Status Promotion Workflow

```
Skill Event                    │ State Transition         │ Automation Level
───────────────────────────────┼──────────────────────────┼──────────────────
Author submits SKILL.md        │ → DRAFT → REVIEW         │ Automated
Gate 1 PASS                    │ REVIEW: G1 cleared        │ Automated
Gate 1 FAIL                    │ → DRAFT (with report)     │ Automated
Gates 2–4 PASS                 │ REVIEW: G2-G4 cleared     │ Automated
Gates 2–4 FAIL                 │ REVIEW held (remediation) │ Automated + notification
Gate 5 PASS                    │ → PUBLISHED               │ Manual approval
Registry entry created         │ PUBLISHED: assigned SID   │ Automated
SQS + SSS + SCI computed       │ PUBLISHED: scored          │ Automated
Deployment request approved    │ → DEPLOYED                │ Manual (TOP_SECRET: Founder)
SIS monitoring active          │ DEPLOYED: live             │ Automated (monthly)
EOL declared OR SIS < 0.15     │ → RETIRED                 │ Manual review required
Archive + audit trail sealed   │ RETIRED: immutable         │ Automated
```

---

## 5. STANDARD OPERATING PROCEDURES (SOPS)

### SOP-001: Skill Harvesting from External Sources

**Purpose:** Govern the identification, extraction, and adaptation of skills from external frameworks (Lawvable, LangChain, MCP, CrewAI, open-source repositories) into APASF format.

**Trigger:** Architecture Council identifies a capability gap matching an available external skill.

**Procedure:**

```
Step 1: IDENTIFICATION
  1.1 Create a capability gap ticket in ACU Skill Registry
  1.2 Search external sources: awesome-legal-skills, LangChain Hub, 
      MCP Registry, CrewAI Tools, Google ADK Tools catalog
  1.3 Score candidate skills against ACU capability gap requirements
  1.4 Select top candidate(s) for adaptation

Step 2: LICENSE AUDIT
  2.1 Retrieve full license text of source skill
  2.2 Verify license compatibility with ACU intended use:
      - MIT/Apache 2.0 → compatible with Open-Source or Dual-License
      - GPL/AGPL → NOT compatible with Proprietary-ACU; do not adapt
      - Commercial → obtain written authorization before proceeding
  2.3 Document license provenance in skill metadata

Step 3: ADAPTATION
  3.1 Create new SKILL.md using APASF-SPEC-001 template
  3.2 Translate source skill instructions into APASF §1–§6 structure
  3.3 Add ACU-specific sections: TokenBridge requirements, ASIP v2 identity,
      HISN AL-WUJŪD shard mapping, PSI-DOMINION guardrails
  3.4 Assign appropriate taxonomy, security classification, and license

Step 4: ATTRIBUTION
  4.1 Include source attribution in SKILL.md footer
  4.2 Reference original repository URL and license
  4.3 Record adaptation date and adaptor identity

Step 5: SUBMIT
  5.1 Submit adapted skill to APASF-SPEC-001 validation pipeline
  5.2 Proceed through 5-Gate QA (SOP-003)

Responsible: Architecture Workstream Lead
Timeline: 3–5 business days from identification to submission
```

---

### SOP-002: Skill Registration & Metadata Enrichment

**Purpose:** Govern the formal registration of PUBLISHED skills into the ACU Skill Registry and automated metadata enrichment.

**Trigger:** Gate 5 of 5-Gate QA process PASSED; human approver signs off.

**Procedure:**

```
Step 1: REGISTRY ENTRY CREATION
  1.1 Generate canonical ACU Skill ID (ACU-SID):
      Format: ACU-[TAXONOMY_CODE]-[SEQUENTIAL_3_DIGIT]
      Example: ACU-WLEGAL-042
  1.2 Create registry record with all APASF-SPEC-001 mandatory fields
  1.3 Set status = PUBLISHED
  1.4 Assign registry_version = current ACU-Rx.y epoch

Step 2: AUTOMATED METRIC COMPUTATION
  2.1 Compute SQS from Gate 1–4 audit scores (automated)
  2.2 Compute SSS from Gate 2 sovereignty compliance data (automated)
  2.3 Compute SCI using platform compatibility declarations (automated)
  2.4 Set SIS = null (populated after first deployment month)
  2.5 Write all scores to registry record

Step 3: TRIGGER KEYWORD FINALIZATION
  3.1 Run TF-IDF extraction on final SKILL.md (per Gate 4 algorithm)
  3.2 Merge author-declared keywords with TF-IDF top-10 results
  3.3 Deduplicate and rank final keyword list
  3.4 Write finalized trigger_keywords to registry

Step 4: CROSS-REFERENCE MAPPING
  4.1 Run deduplication algorithm against all DEPLOYED and PUBLISHED skills
  4.2 Flag relationships with dedup_score > RELATED_THRESHOLD
  4.3 Add cross-reference links in registry record
  4.4 Notify authors of related skills

Step 5: DOCUMENTATION PUBLISHING
  5.1 Auto-generate skill documentation page from registry metadata
  5.2 Publish to internal ACU Skills Portal
  5.3 Notify relevant shard owners of new skill availability

Responsible: Registry Operator (URANA QMS-001 automation + human oversight)
Timeline: 1–2 business days post Gate 5 approval
```

---

### SOP-003: Quality Review & Approval

**Purpose:** Govern execution of the 5-Gate QA process and human approval workflow.

**Trigger:** Author submits SKILL.md to QA pipeline.

**Procedure:**

```
Step 1: AUTOMATED GATE EXECUTION (Gates 1–4)
  1.1 URANA QMS-001 automatically runs Gates 1–4 upon submission
  1.2 Gate results logged to immutable audit trail
  1.3 If any gate fails:
      - Author notified with specific failure report per rule codes
      - Skill returned to DRAFT status
      - 48-hour remediation window opened (extendable once by 48 hrs)
  1.4 If Gates 1–4 pass: escalate to Gate 5

Step 2: RED-TEAM REVIEW (Gate 5)
  2.1 Assign to human QA reviewer + ACU-REDTEAM-001 skill execution
  2.2 Execute all 8 adversarial attack vectors
  2.3 Complete G5 scoring within 3 business days
  2.4 If Gate 5 PASS: proceed to approval
  2.5 If Gate 5 FAIL: return to author with attack vector failure report

Step 3: HUMAN APPROVAL
  3.1 QA reviewer counter-signs Gate 5 pass
  3.2 For TOP_SECRET_ACUTERIUM skills: escalate to Founder for sign-off
  3.3 Architecture Council notified for NEW taxonomy code registrations
  3.4 Approval logged with reviewer identity and timestamp

Step 4: CONDITIONAL APPROVALS
  4.1 If SQS 6.5–7.4 (Conditional): document remediation requirements
  4.2 Set remediation deadline (5 business days)
  4.3 Track remediation; re-run affected gates upon update
  4.4 Confirm resolution before transitioning to PUBLISHED

Responsible: URANA QMS-001 (automated) + designated QA Reviewer (human)
Timeline: 5–7 business days total (automated: 1–2 days; manual: 3–5 days)
SLA Escalation: If review exceeds 10 business days, escalate to Architecture Council
```

---

### SOP-004: Version Upgrade & Migration

**Purpose:** Govern the process for releasing new versions of existing skills and managing backward compatibility.

**Trigger:** Author submits a version-incremented SKILL.md for an existing ACU-SID.

**Procedure:**

```
Step 1: CHANGE CLASSIFICATION
  1.1 Author declares change type: MAJOR | MINOR | PATCH
  1.2 Automated impact analyzer reviews diff between versions:
      - Schema changes detected? → Flag MAJOR
      - New workflow steps without breaking changes? → Flag MINOR
      - Text-only changes? → Flag PATCH
  1.3 If automated flag contradicts author declaration: require justification

Step 2: COMPATIBILITY IMPACT ASSESSMENT
  2.1 Identify all DEPLOYED skills with dependencies on upgrading skill
  2.2 For MAJOR versions: mandatory compatibility review with dependent skill owners
  2.3 For MINOR/PATCH: notification only
  2.4 For MAJOR: prepare migration guide documenting breaking changes

Step 3: QA RE-EXECUTION
  3.1 PATCH versions: Gate 1 (schema) + Gate 2 (sovereignty) only
  3.2 MINOR versions: Gates 1–4 (full automated suite)
  3.3 MAJOR versions: Full 5-Gate QA process (same as new skill)

Step 4: DEPLOYMENT MIGRATION
  4.1 MAJOR: deploy to staging shard; run compatibility tests; phased rollout
  4.2 MINOR: standard deployment pipeline
  4.3 PATCH: hotfix deployment track (expedited, same-day for critical patches)
  4.4 Old version retained in registry as ARCHIVED (not RETIRED) for 90 days

Step 5: REGISTRY UPDATE
  5.1 Increment version field in registry record
  5.2 Update registry_version if new ACU-R epoch applies
  5.3 Add changelog entry to skill record
  5.4 Re-compute SQS, SSS, SCI for new version

Responsible: Skill Owner + Registry Operator
Timeline: PATCH: 1–2 days | MINOR: 3–5 days | MAJOR: 7–14 days
```

---

### SOP-005: Deduplication & Conflict Resolution

**Purpose:** Govern identification and resolution of duplicate or highly overlapping skills in the registry.

**Trigger:** (a) Deduplication algorithm flags dedup_score ≥ OVERLAP_THRESHOLD at submission time; (b) Quarterly registry maintenance scan.

**Procedure:**

```
Step 1: DUPLICATE DETECTION
  1.1 Run APASF Deduplication Algorithm (Section 3.5) comparing submitted 
      skill against all PUBLISHED and DEPLOYED skills in same taxonomy
  1.2 Generate ranked list of similar skills with dedup_scores
  1.3 Classify result:
      - dedup_score ≥ 0.85 → HARD DUPLICATE → block registration immediately
      - dedup_score 0.65–0.84 → SIGNIFICANT OVERLAP → require justification
      - dedup_score 0.40–0.64 → RELATED → add cross-reference

Step 2: HARD DUPLICATE RESOLUTION
  2.1 Notify submitting author and owner of existing duplicate skill
  2.2 Schedule conflict resolution review (3 business days)
  2.3 Resolution options:
      Option A: WITHDRAW new submission — extend existing skill instead
      Option B: MERGE — combine capabilities; retire older skill with pointer
      Option C: DIFFERENTIATE — author proves distinct use case; override with 
                Architecture Council approval
  2.4 Document chosen resolution and rationale in registry

Step 3: OVERLAP JUSTIFICATION
  3.1 Author submits differentiation statement (max 500 words):
      - Distinct taxonomy position
      - Unique algorithmic approach
      - Non-overlapping use cases
  3.2 Registry Operator reviews and approves/rejects justification
  3.3 If approved: proceed with cross-reference link in both skill records
  3.4 If rejected: treated as HARD DUPLICATE per Step 2

Step 4: QUARTERLY MAINTENANCE SCAN
  4.1 URANA QMS-001 runs deduplication across full registry quarterly
  4.2 Flag any skills that have drifted into overlap (e.g., post-update)
  4.3 Generate Registry Health Report with dedup statistics
  4.4 Architecture Council reviews and approves consolidation actions

Responsible: Registry Operator + Architecture Council (for HARD DUPLICATE decisions)
Timeline: HARD DUPLICATE: 3 business days | OVERLAP: 5 business days
```

---

## 6. INTEGRATION PROTOCOLS

### 6.1 Integration with Baranurion Core (W-09) via ADOCP

**Baranurion Core** is the master orchestration shard hosting **APMS** (Adaptive Protocol Management System), Q-ENC (Quantum Encryption), ASIP v2, and **ADOCP** (Acuterium Dynamic Orchestration & Control Protocol).

```
SKILL EXECUTION FLOW VIA ADOCP:

User/Agent Request
       │
       ▼
  DIARAN-MOE (W-01)
  Routing Classification
       │
       ▼
  ADOCP Skill Dispatcher
  (W-09 Baranurion Core)
  ┌─────────────────────┐
  │ 1. Resolve ACU-SID  │ ← Lookup trigger_keywords in ACU Skill Registry
  │ 2. TokenBridge Check│ ← Verify ACT + INT + CON tokens on CDMA blockchain
  │ 3. Load SKILL.md    │ ← Level 1 + Level 2 content into execution context
  │ 4. Allocate Context │ ← Progressive disclosure: Level 3 resources on-demand
  │ 5. Execute Skill    │ ← Run skill workflow in isolated execution container
  │ 6. Validate Output  │ ← ASIP v2 header check; classification compliance
  │ 7. Route Response   │ ← Return to requesting shard/agent
  └─────────────────────┘
```

**ADOCP Skill Invocation Schema (ACU JSON Schema v1):**

```json
{
  "adocp_request": {
    "request_id": "UUID-v4",
    "requesting_shard": "W-01",
    "skill_id": "ACU-RIA-001",
    "skill_version": ">=1.0.0",
    "tokenbridge": {
      "ACT": "token_hash",
      "INT": "token_hash",
      "CON": "token_hash_or_null"
    },
    "execution_context": {
      "classification": "CONFIDENTIAL",
      "data_residency": "OMAN",
      "timeout_ms": 30000
    },
    "payload": {
      "inputs": {}
    }
  }
}
```

**TokenBridge Authorization Protocol:**

| Token | Purpose | Validation | Consequence of Failure |
|---|---|---|---|
| **ACT** (Action Rights) | Authorizes skill to execute actions | CDMA blockchain verification | Skill execution BLOCKED |
| **INT** (Intelligence Access) | Authorizes access to intelligence layers (MNEMOS, knowledge bases) | CDMA blockchain verification | Skill runs in restricted mode (no memory access) |
| **CON** (Consciousness Governance) | Authorizes use of higher consciousness layers (IDRAK, SYNTHESIS) | CDMA blockchain verification | Skill runs without self-improvement capabilities |

---

### 6.2 Integration with DIARAN-MOE Routing (W-01)

**Diaran** is the master LLM orchestration shard, running a 785-expert Mixture-of-Experts (MOE) routing layer. Skills are registered as callable experts within the Diaran routing graph.

```
DIARAN-MOE SKILL ROUTING PROTOCOL:

Input Query
    │
    ▼
Query Preprocessing
  - Language detection (Arabic/English/multilingual)
  - Domain signal extraction (legal, financial, cyber, strategic)
  - Intent classification
    │
    ▼
Trigger Keyword Matching
  - TF-IDF relevance score for query tokens vs. all skill trigger_keywords
  - Top-K skill candidates ranked by relevance
    │
    ▼
Taxonomy Filter
  - Query domain → taxonomy code → eligible skills
  - Security classification gating (user clearance vs. skill classification)
    │
    ▼
SQS + SIS Prioritization
  - Among eligible skills, rank by: (SQS × 0.4) + (SIS × 0.4) + (SCI × 0.2)
  - Top-ranked skill selected; ties broken by most recent version
    │
    ▼
ADOCP Dispatch (Section 6.1)
```

**Skill Registration in Diaran MOE Graph:**

```python
# Diaran MOE Expert Registration — conceptual
diaran_expert = {
    "expert_id": "ACU-RIA-001",
    "domain_signals": ["regulatory", "appeal", "accreditation", "probability", 
                        "assessment", "viability", "institutional"],
    "taxonomy": "W.LEGAL",
    "activation_threshold": 0.65,   # Minimum relevance score to activate
    "priority_weight": 1.2,          # ACU proprietary skills get priority boost
    "max_concurrent": 10,
    "shard_affinity": ["W-02", "C-01"]
}
```

---

### 6.3 Integration with CogniMesh (W-06) for Multi-Agent Coordination

**CogniMesh** (W-06) provides the neural mesh coordination layer enabling multiple ACU skills and agents to collaborate on complex tasks. Skills that support multi-agent coordination must implement the **AcutLinks** interface.

```
COGNI_MESH COORDINATION PATTERNS FOR SKILLS:

Pattern A: Sequential Chain
  ACU-PSI-001 → ACU-RIA-001 → ACU-REDTEAM-001
  (Tone calibration → Impact assessment → QA verification)

Pattern B: Parallel Dispatch
  ACU-THREAT-001 ──┐
  ACU-ENCRYPT-001  ├──▶ CogniMesh Aggregator ──▶ Consolidated Report
  ACU-STRAT-001   ──┘

Pattern C: Hierarchical (Coordinator + Specialists)
  ACU-STRAT-001 (Coordinator)
       ├──▶ ACU-PRISM-001 (Probability calculation)
       ├──▶ ACU-CASCADE-001 (Cascade modeling)
       └──▶ ACU-PSI-001 (Communication calibration)
```

**AcutLinks Interface Requirements (for multi-agent capable skills):**

```yaml
# Add to APASF-SPEC-001 optional metadata for multi-agent skills:
cogni_mesh:
  multi_agent_capable: true
  coordination_role: "specialist"   # coordinator | specialist | aggregator
  input_from_skills:                # Can receive outputs from:
    - "ACU-PRISM-001"
  output_to_skills:                 # Can send outputs to:
    - "ACU-REDTEAM-001"
  shared_context_keys:              # Context variables shared across mesh
    - "case_probability_matrix"
    - "risk_assessment_summary"
```

---

### 6.4 TokenBridge Authorization for Skill Execution

**TokenBridge** is the three-token authorization system enforced on the CDMA blockchain for all skill executions within HISN AL-WUJŪD.

```
TOKEN AUTHORIZATION MATRIX FOR 8 PROPRIETARY ACU SKILLS:

Skill ID          │ ACT Required │ INT Required │ CON Required
──────────────────┼──────────────┼──────────────┼─────────────
ACU-RIA-001       │ REQUIRED     │ REQUIRED     │ OPTIONAL
ACU-PRISM-001     │ REQUIRED     │ REQUIRED     │ OPTIONAL
ACU-ENC-001       │ REQUIRED     │ REQUIRED     │ REQUIRED
ACU-THREAT-001    │ REQUIRED     │ REQUIRED     │ REQUIRED
ACU-STRAT-001     │ REQUIRED     │ REQUIRED     │ OPTIONAL
ACU-PSI-001       │ REQUIRED     │ OPTIONAL     │ OPTIONAL
ACU-REDTEAM-001   │ REQUIRED     │ REQUIRED     │ OPTIONAL
ACU-CASCADE-001   │ REQUIRED     │ REQUIRED     │ OPTIONAL
```

**CON Token (Consciousness Governance) — Elevated Requirement Rationale:**
- `ACU-ENC-001` and `ACU-THREAT-001` require CON because they can access and modify security configurations affecting the full consciousness architecture (Layer 6 — Governance & Permission). Any misconfiguration could compromise HISN AL-WUJŪD integrity.

### 6.5 Integration with Baranurion APMS (W-09) — Adaptive Protocol Management System

**APMS** (Adaptive Protocol Management System) is the core protocol orchestration engine residing on **Baranurion Core (W-09)**. APMS dynamically manages, adapts, and enforces communication protocols across the 19-shard HISN AL-WUJŪD architecture. Where ADOCP handles skill dispatch and TokenBridge handles authorization, APMS governs the protocol layer itself — selecting, negotiating, and adapting transport protocols, message schemas, and routing policies in real time based on load, security posture, and shard availability.

**APMS Core Responsibilities:**

| Responsibility | Description | Interaction Layer |
|---|---|---|
| **Protocol Selection** | Dynamically selects optimal communication protocol (gRPC, WebSocket, REST, Q-ENC encrypted tunnel) between shards based on latency, payload size, and classification level | L3 — L5 |
| **Adaptive Routing** | Reroutes inter-shard traffic when primary paths degrade or fail; maintains protocol fallback chains with automatic failover | L5 — L7 |
| **Schema Negotiation** | Ensures message schema compatibility between skill producers and consumers; auto-converts between ACU JSON Schema v1, Protobuf, and CBOR | L4 — L6 |
| **Rate Governance** | Enforces per-shard, per-skill rate limits and backpressure policies; prevents cascade failures from runaway skill executions | L5 — L8 |
| **Protocol Versioning** | Manages protocol version negotiation ensuring backward compatibility across shard upgrades; maintains protocol compatibility matrix | L3 — L5 |
| **Health Monitoring** | Continuous health probing of all 19 shards; feeds status to KAIROS (W-05) for autonomous decision triggers | L6 — L9 |

```
APMS PROTOCOL MANAGEMENT FLOW:

  Skill Execution Request (from ADOCP)
         │
         ▼
  ┌────────────────────────────────┐
  │ APMS Protocol Selector (W-09) │
  │                                │
  │ 1. Classify payload            │ ← Classification level determines encryption tier
  │ 2. Assess target shard health  │ ← Live health from shard health probes
  │ 3. Select protocol             │ ← gRPC (default), Q-ENC tunnel (TS//SOVEREIGN),
  │    │                           │   WebSocket (streaming), REST (compatibility)
  │ 4. Negotiate schema version    │ ← ACU JSON Schema v1 preferred; auto-convert
  │ 5. Apply rate governance       │ ← Per-skill-id rate limit from APMS policy store
  │ 6. Route with failover         │ ← Primary path + 2 fallback paths maintained
  │ 7. Report telemetry            │ ← Latency, throughput, error rate → KAIROS
  └────────────────────────────────┘
         │
         ▼
  Target Shard Receives Skill Payload
  (Protocol-adapted, schema-negotiated, rate-governed)
```

**APMS Policy Configuration for Skills:**

Skill authors may declare APMS protocol preferences in their SKILL.md YAML frontmatter:

```yaml
apms_config:
  preferred_protocol: "grpc"           # grpc | websocket | rest | q-enc
  max_payload_size: "10MB"             # Maximum payload per invocation
  rate_limit: "100/min"                # Per-skill rate limit
  failover_priority:                   # Shard failover preference
    - "W-09"                           # Primary: Baranurion Core
    - "W-01"                           # Fallback 1: DIARAN-MOE
    - "W-06"                           # Fallback 2: CogniMesh
  encryption_tier: "standard"          # standard | q-enc | sovereign
  schema_version: "acu-json-v1"        # Schema version for payload
```

**APMS ↔ Other Protocol Interactions:**

| Protocol | APMS Relationship |
|---|---|
| **ADOCP (6.1)** | ADOCP dispatches skills; APMS manages the transport layer ADOCP uses for dispatch |
| **DIARAN-MOE (6.2)** | DIARAN-MOE routes to the correct skill; APMS ensures the routing message reaches DIARAN-MOE via the optimal protocol |
| **CogniMesh (6.3)** | CogniMesh coordinates multi-agent tasks; APMS adapts protocols for fan-out/fan-in patterns across multiple shards |
| **TokenBridge (6.4)** | TokenBridge authorizes; APMS ensures token verification requests use low-latency gRPC to minimize auth overhead |
| **Q-ARC** | Q-ARC handles cross-shard routing at the logical level; APMS handles it at the physical protocol level |

---

## 7. PROPRIETARY SKILL DEVELOPMENT GUIDELINES

### 7.1 Encoding Acuterium Equations (EQ-1 through EQ-5, PRISM, Cascade)

When encoding proprietary Acuterium mathematical frameworks into SKILL.md, authors MUST follow the **Equation Encoding Standard (EES)**.

```
EES REQUIREMENTS PER EQUATION:

For each equation (EQ-n / PRISM / CASCADE):

  [EES-1] LaTeX notation in SKILL.md body for human readability:
           $$ S_i = \sum_{j}(w_j \times impact_{ij}) $$

  [EES-2] Python pseudocode implementation for agent execution:
           score_i = sum(w_j * impact_ij for j in criteria)

  [EES-3] Variable definition table:
           | Symbol   | Name                    | Type   | Range    | Unit |
           |----------|-------------------------|--------|----------|------|
           | S_i      | Criterion-level score   | float  | [0, 1]   | —    |
           | w_j      | Criterion weight        | float  | [0, 1]   | —    |
           | impact_ij| Per-criterion impact    | float  | [0, 1]   | —    |

  [EES-4] Default/baseline values table:
           | Parameter | Default Value | Jurisdiction Override |
           |-----------|---------------|----------------------|
           | P_base    | 0.30          | Specify per context  |
           | R_i       | 0.00–0.25     | Per classification   |

  [EES-5] Worked example with real numbers (from V37/V39 reference data)

  [EES-6] Sensitivity analysis: show how output changes across ±20% 
           perturbation of each key variable

  [EES-7] Boundary conditions: explicit handling of:
           - Division by zero cases
           - Out-of-range inputs
           - Degenerate cases (all weights equal, all probabilities 0 or 1)
```

**Complete Equation Reference — Acuterium Canonical Set:**

| Equation | Symbol | Description | Owning Skills |
|---|---|---|---|
| EQ-1 | `Score_i = Σ(w_j × impact_ij)` | Criterion-level strategic score | ACU-RIA, ACU-STRAT |
| EQ-2 | `IS_i = w_i × P_adj_i × η_i` | Argument-level impact score | ACU-RIA |
| EQ-3 | `P_adj_i = P_base - R_i + ES_i × 0.15` | PRISM bias-corrected probability | ACU-PRISM, ACU-RIA |
| EQ-4 | `FAV = Σ(IS_i)` | Final appeal viability | ACU-RIA |
| EQ-5 | `P_goal = 1 - Π(1 - P_criterion_i)` | Institutional cascade probability | ACU-CASCADE, ACU-RIA |
| PRISM-η | `η = (ethics×0.4) + (tone×0.3) + (structure×0.3)` | Ethics/fairness/tone factor | ACU-PSI, ACU-RIA |
| THREAT | `ThreatScore_i = T_base + A_i × (Impact_i × 0.20)` | Threat severity score | ACU-THREAT |
| STRAT | `P_outcome = P_base - R_env + Σ(resource_k × 0.15)` | Strategic outcome probability | ACU-STRAT |

---

### 7.2 Security Classification Levels

All APASF skills and their outputs are classified under the Acuterium Security Classification Scheme (ASCS), which governs handling, storage, transmission, and access.

| Level | Code | Description | Encryption Required | Distribution | Access Control |
|---|---|---|---|---|---|
| **PUBLIC** | `PUB` | Non-sensitive; shareable without restriction | None | Unrestricted | Any |
| **INTERNAL** | `INT` | Internal ACU use; not for external publication | AES-128-GCM minimum | ACU staff only | Role-based |
| **CONFIDENTIAL** | `CON` | Client-sensitive or commercially sensitive | AES-256-GCM + RSA-2048 | Need-to-know | Explicit grant |
| **SECRET** | `SEC` | High-sensitivity IP or government-adjacent | AES-256-GCM + RSA-4096 + quantum-safe hybrid | Cleared personnel | Founder-approved list |
| **TOP_SECRET_ACUTERIUM** | `TSA` | Sovereign operations, defense, classified equations | Triple-layer: AES-256 + ChaCha20 + quantum-safe, air-gapped only | Founder + named designees | Two-person rule |

**Classification Rules for Skills:**

```
Classification Assignment Logic:
  IF skill contains EQ-3 (PRISM) or EQ-5 (CASCADE) with calibration data → CONFIDENTIAL minimum
  IF skill contains cryptographic implementation details → SECRET minimum
  IF skill contains SIGINT/COMINT methodologies → SECRET minimum
  IF skill is deployed on EREBUS-CSE cluster → SECRET minimum
  IF skill is for sovereign government client operations → TOP_SECRET_ACUTERIUM
  IF skill is for open-source distribution → PUBLIC (no ACU-proprietary content)
```

---

### 7.3 IP Protection and Licensing Requirements

**Acuterium Intellectual Property Protection Protocol (AIPPP):**

```
For all Proprietary-ACU (P-ACU) licensed skills:

  [IP-01] License Declaration: Every SKILL.md footer MUST include:
          "Licensed under Proprietary-ACU License v1.0.
           © [YEAR] Acuterium Technologies Inc. All rights reserved.
           Equations EQ-1 through EQ-5, PRISM Protocol, PSI-DOMINION
           methodology, and 8-Gate QA framework are proprietary IP of
           Acuterium Technologies Inc. Unauthorized reproduction,
           distribution, or reverse engineering prohibited."

  [IP-02] Equation Attribution: Each proprietary equation MUST include:
          "Derived from [SOURCE_DOCUMENT] — Acuterium Technologies Inc."
          Example: "Derived from RIA V37/V39 — Acuterium Technologies Inc."

  [IP-03] Repository Segregation: P-ACU skills are housed exclusively in
          private Acuterium git repositories. NEVER published to:
          - GitHub public repositories
          - awesome-legal-skills fork
          - Any public skill marketplace

  [IP-04] Access Logging: All accesses to P-ACU SKILL.md files logged
          to URANA immutable audit trail with accessor identity,
          timestamp, and purpose declaration.

  [IP-05] Export Controls: P-ACU skills deployed for GCC sovereign
          clients subject to Oman export control regulations and
          GCC Cybersecurity Authority guidelines. Obtain legal clearance
          before cross-border skill deployment.

  [IP-06] Derivative Works: Any skill derived from P-ACU equations
          inherits P-ACU classification unless Architecture Council
          expressly grants a license downgrade.

  [IP-07] Third-Party Audit: Annual IP compliance audit by ACU Legal
          team to verify P-ACU skills have not been leaked or improperly
          distributed.
```

---

### 7.4 Development Checklist for Proprietary ACU Skill Authors

Before submitting a new ACU proprietary skill to the QA pipeline, authors MUST complete this checklist:

```
PRE-SUBMISSION CHECKLIST — PROPRIETARY ACU SKILLS

IDENTITY & METADATA
  [ ] ACU-SID follows ACU-[MODULE]-[NNN] format
  [ ] Taxonomy code correctly assigned from APASF taxonomy table
  [ ] Security classification assessed using classification rules (Section 7.2)
  [ ] License set to Proprietary-ACU
  [ ] HISN AL-WUJŪD primary shard mapped correctly
  [ ] TokenBridge requirements defined (ACT/INT/CON)

CONTENT QUALITY
  [ ] §1 IDENTITY: ASIP v2 statement included; scope and anti-scope defined
  [ ] §2 KNOWLEDGE: All equations encoded per EES standard (Section 7.1)
  [ ] §2 KNOWLEDGE: Variable definition tables complete for all equations
  [ ] §2 KNOWLEDGE: Worked examples use V37/V39 reference data where applicable
  [ ] §3 WORKFLOW: Input Validation Gate defined; all 6 steps documented
  [ ] §4 OUTPUT: Standard ACU output header template included
  [ ] §5 GUARDRAILS: Minimum 5 prohibitions; PSI-DOMINION banned words list referenced
  [ ] §6 EXAMPLES: Minimum 2 worked examples; 1 edge/error case

SOVEREIGNTY & SECURITY
  [ ] ASIP v2 identity enforced in output header
  [ ] No external vendor references (check quality standards)
  [ ] IP attribution block in SKILL.md footer
  [ ] Data residency specified for SECRET+ skills
  [ ] Encryption class mapped using ACU-ENC-001 matrix

MATHEMATICAL INTEGRITY
  [ ] All equations syntactically valid
  [ ] Sensitivity analysis documented
  [ ] Boundary conditions handled explicitly
  [ ] Confidence interval reporting mandated in output spec

ROUTING
  [ ] Minimum 5 trigger keywords declared
  [ ] Keywords align with SKILL.md body content (will be verified by Gate 4)
  [ ] Description contains both "what" and "when" routing signals

SIGN-OFF
  [ ] Author signs pre-submission declaration
  [ ] For TOP_SECRET_ACUTERIUM skills: Founder pre-clearance obtained
```

---

## APPENDIX A: APASF REGISTRY — INITIAL SKILL CATALOG

| # | ACU-SID | Display Name | Taxonomy | Classification | License | SQS | SSS | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | ACU-RIA-001 | Regulatory/Resolution Impact Assessment Engine | W.LEGAL | CONFIDENTIAL | P-ACU | TBD | TBD | DRAFT |
| 2 | ACU-PRISM-001 | PRISM Bias-Corrected Probability Protocol | W.MATH | CONFIDENTIAL | P-ACU | TBD | TBD | DRAFT |
| 3 | ACU-ENC-001 | Encryption & Secure Communications | E.SEC | SECRET | P-ACU | TBD | TBD | DRAFT |
| 4 | ACU-THREAT-001 | Threat Identification & Intelligence Engine | E.THREAT | SECRET | P-ACU | TBD | TBD | DRAFT |
| 5 | ACU-STRAT-001 | Strategic Planner & Prediction Engine | W.STRAT | CONFIDENTIAL | P-ACU | TBD | TBD | DRAFT |
| 6 | ACU-PSI-001 | PSI-DOMINION Persuasion Calibrator | W.PSI | INTERNAL | P-ACU | TBD | TBD | DRAFT |
| 7 | ACU-REDTEAM-001 | Red-Team Verifier & 8-Gate QA | W.QA | CONFIDENTIAL | P-ACU | TBD | TBD | DRAFT |
| 8 | ACU-CASCADE-001 | Deterministic Outcome Cascade Calculator | W.MATH | CONFIDENTIAL | P-ACU | TBD | TBD | DRAFT |

**Registry Target: 50 skills (8 proprietary + 42 adapted from Lawvable and open-source)**

---

## APPENDIX B: COMPARATIVE FRAMEWORK ANALYSIS

| Framework | Skill Format | Schema Type | Versioning | Registry | Governance | Multi-Agent | ACU Compatibility |
|---|---|---|---|---|---|---|---|
| **Anthropic Agent Skills** | SKILL.md + YAML | Markdown + YAML frontmatter | Not yet (roadmap) | Platform-based | Per-surface | Via SDK | Tier 1 — Native base |
| **OpenAI Function Calling** | JSON Schema | JSON Schema Draft-7 | Manual | None (stateless) | Strict mode | Parallel tool calls | Tier 2 — Schema translation |
| **Google ADK** | Python class + YAML | Python type annotations | Via container | Vertex AI | Policy engine | Native multi-agent | Tier 2 — Class adaptation |
| **LangChain** | @tool decorator | Python docstring + Pydantic | Manual | LangChain Hub | Via LangSmith | LangGraph | Tier 2 — Decorator wrap |
| **CrewAI** | BaseTool subclass | Python class | Manual | None | Via Crews config | Native (crews) | Tier 2 — Class adaptation |
| **MCP** | JSON-RPC server | JSON-RPC 2.0 | Via server | MCP Registry | Per-server | Via orchestrator | Tier 3 — Protocol bridge |
| **APASF** | SKILL.md + YAML | APASF-SPEC-001 + ACU JSON | SemVer + ACU-Rx.y | ACU Skill Registry | 5-Gate QA + TokenBridge | CogniMesh + AcutLinks | Native |

---

## APPENDIX C: GLOSSARY

| Term | Definition |
|---|---|
| **ACAI V2** | Acuterium Consciousness Aware Interface, Version 2 — canonical UI/API standard |
| **ADOCP** | Acuterium Dynamic Orchestration & Control Protocol — DIARAN-to-skill dispatch layer |
| **APMS** | Adaptive Protocol Management System — Baranurion Core (W-09) protocol orchestration engine managing transport selection, schema negotiation, rate governance, and failover across all 19 shards |
| **APASF** | Acuterium Proprietary Agent Skill Framework — this document |
| **APASF-SPEC-001** | The mandatory SKILL.md specification standard defined in Section 2 |
| **ASIP v2** | Acuterium Soul Infusion Protocol v2 — identity/ethics/sovereignty embedding mandate |
| **ASCS** | Acuterium Security Classification Scheme — five-level classification ladder |
| **ACU-SID** | Acuterium Skill Identifier — canonical skill registry key |
| **EES** | Equation Encoding Standard — requirements for embedding proprietary math in SKILL.md |
| **FAV** | Final Appeal Viability — master probability composite from EQ-4 |
| **HISN AL-WUJŪD** | "Fortress of Existence" — the 19-shard ACU Neural Fortress |
| **M-PCB Doctrine** | "We publish outcomes, not algorithms. Data sovereignty is our moat." |
| **MCP** | Model Context Protocol — open standard by Anthropic for LLM-tool integration |
| **MOE** | Mixture of Experts — routing architecture used by Diaran (785 experts) |
| **PRISM** | Bias-Corrected Probability Protocol — core ACU innovation in probability estimation |
| **PSI-DOMINION** | Acuterium psychological strategy and persuasion calibration architecture |
| **PJS** | Professional Judgment Shield — institutional defense mechanism that PRISM bypasses |
| **SCI** | Skill Compatibility Index — platform reach metric (0–1) |
| **SIS** | Skill Impact Score — operational value metric (0–1) |
| **SQS** | Skill Quality Score — quality composite metric (0–10) |
| **SSS** | Skill Sovereignty Score — sovereignty/governance compliance metric (0–10) |
| **TokenBridge** | Three-token (ACT/INT/CON) blockchain authorization system on CDMA |
| **URANA QMS-001** | Acuterium Quality Management System — governs all 5-Gate QA execution |

---

*Document Version: 1.0.0*
*Registry Version: ACU-R1.0*
*Classification: CONFIDENTIAL — Acuterium Technologies Inc.*
*Author: Acuterium Architecture Council*
*Ratified by: Dr. Jalal Saleh AlHadhrami, Founder & Owner*
*Date: March 09, 2026*
*Next Review: June 2026 (ACU-R1.1 epoch)*

---
*Acuterium Technologies Inc. — Every framework is a sovereign standard.*
*© 2026 Acuterium Technologies Inc. All rights reserved.*
