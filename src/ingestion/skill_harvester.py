#!/usr/bin/env python3
"""
Acuterium Skills Marketplace — Mass Skill Harvester
Extracts skills from 21 GitHub repositories and normalizes to ACU schema.
"""

import json
import uuid
import os
import re
import glob as globmod
import yaml
from pathlib import Path
from datetime import datetime

REPO_BASE = "/home/user/workspace/source_repos"
OUTPUT_DIR = "/home/user/workspace/marketplace_output"

# ─── ACUTERIUM MAPPING RULES ───────────────────────────────────────
CATEGORY_MAP = {
    # Security/Red-team
    "security": {"thread": "T08 — ZURD", "thread_code": "T08", "domain": "security", "shard": "Tenebris-ACIWS", "layers": ["L8","L9","L10"], "sov": 10, "gov": "sovereign"},
    "red-team": {"thread": "T08 — ZURD", "thread_code": "T08", "domain": "security", "shard": "Tenebris-ACIWS", "layers": ["L8","L9","L10"], "sov": 10, "gov": "sovereign"},
    "adversarial": {"thread": "T08 — ZURD", "thread_code": "T08", "domain": "security", "shard": "Tenebris-ACIWS", "layers": ["L8","L9","L10"], "sov": 10, "gov": "sovereign"},
    "jailbreak": {"thread": "T08 — ZURD", "thread_code": "T08", "domain": "security", "shard": "Tenebris-ACIWS", "layers": ["L8","L9","L10"], "sov": 10, "gov": "sovereign"},
    "pentesting": {"thread": "T08 — ZURD", "thread_code": "T08", "domain": "security", "shard": "Tenebris-ACIWS", "layers": ["L8","L9","L10"], "sov": 10, "gov": "sovereign"},
    "vulnerability": {"thread": "T08 — ZURD", "thread_code": "T08", "domain": "security", "shard": "Tenebris-ACIWS", "layers": ["L8","L9","L10"], "sov": 10, "gov": "sovereign"},
    "forensics": {"thread": "T08 — ZURD", "thread_code": "T08", "domain": "security", "shard": "Tenebris-ACIWS", "layers": ["L8","L9","L10"], "sov": 10, "gov": "sovereign"},
    "malware": {"thread": "T08 — ZURD", "thread_code": "T08", "domain": "security", "shard": "Tenebris-ACIWS", "layers": ["L8","L9","L10"], "sov": 10, "gov": "sovereign"},
    "threat-intelligence": {"thread": "T06 — EDNA", "thread_code": "T06", "domain": "security", "shard": "Edna-SIGINT", "layers": ["L7","L8","L9"], "sov": 9, "gov": "restricted"},
    "competitive-intel": {"thread": "T06 — EDNA", "thread_code": "T06", "domain": "security", "shard": "Edna-SIGINT", "layers": ["L7","L8","L9"], "sov": 9, "gov": "restricted"},
    "system-prompts": {"thread": "T06 — EDNA", "thread_code": "T06", "domain": "security", "shard": "Edna-SIGINT", "layers": ["L7","L8","L9"], "sov": 9, "gov": "restricted"},
    "identity": {"thread": "T09 — Q-Suite", "thread_code": "T09", "domain": "security", "shard": "Q-ENC", "layers": ["L8","L9","L10"], "sov": 10, "gov": "sovereign"},
    "auth": {"thread": "T09 — Q-Suite", "thread_code": "T09", "domain": "security", "shard": "Q-ENC", "layers": ["L8","L9","L10"], "sov": 10, "gov": "sovereign"},
    "crypto": {"thread": "T09 — Q-Suite", "thread_code": "T09", "domain": "security", "shard": "Q-ENC", "layers": ["L8","L9","L10"], "sov": 10, "gov": "sovereign"},
    "content-safety": {"thread": "T08 — ZURD", "thread_code": "T08", "domain": "security", "shard": "EREBUS-CSE", "layers": ["L8","L9","L10"], "sov": 10, "gov": "mandatory"},
    "moderation": {"thread": "T08 — ZURD", "thread_code": "T08", "domain": "security", "shard": "EREBUS-CSE", "layers": ["L8","L9","L10"], "sov": 10, "gov": "mandatory"},
    
    # Infrastructure
    "cloud-azure": {"thread": "T13 — ACAI V2", "thread_code": "T13", "domain": "infrastructure", "shard": "Marel", "layers": ["L5","L6","L7"], "sov": 8, "gov": "restricted"},
    "cloud-aws": {"thread": "T13 — ACAI V2", "thread_code": "T13", "domain": "infrastructure", "shard": "Marel", "layers": ["L5","L6","L7"], "sov": 8, "gov": "restricted"},
    "cloud": {"thread": "T13 — ACAI V2", "thread_code": "T13", "domain": "infrastructure", "shard": "Marel", "layers": ["L5","L6","L7"], "sov": 8, "gov": "restricted"},
    "infrastructure": {"thread": "T13 — ACAI V2", "thread_code": "T13", "domain": "infrastructure", "shard": "Marel", "layers": ["L5","L6","L7"], "sov": 8, "gov": "restricted"},
    "devops": {"thread": "T13 — ACAI V2", "thread_code": "T13", "domain": "infrastructure", "shard": "Watad", "layers": ["L5","L6","L7"], "sov": 8, "gov": "restricted"},
    "mcp": {"thread": "T01 — COSM", "thread_code": "T01", "domain": "infrastructure", "shard": "ADOCP", "layers": ["L5","L6"], "sov": 9, "gov": "mandatory"},
    "tool-integration": {"thread": "T01 — COSM", "thread_code": "T01", "domain": "infrastructure", "shard": "ADOCP", "layers": ["L5","L6"], "sov": 9, "gov": "mandatory"},
    "monitoring": {"thread": "T01 — COSM", "thread_code": "T01", "domain": "infrastructure", "shard": "ADOCP", "layers": ["L5","L6","L7"], "sov": 9, "gov": "restricted"},
    "blockchain": {"thread": "T01 — COSM", "thread_code": "T01", "domain": "infrastructure", "shard": "ADOCP", "layers": ["L5","L6"], "sov": 9, "gov": "mandatory"},
    
    # Cognitive
    "code-generation": {"thread": "T04 — ACIW", "thread_code": "T04", "domain": "cognitive", "shard": "AcuTect-CODEX", "layers": ["L5","L6","L7","L8"], "sov": 10, "gov": "mandatory"},
    "code-review": {"thread": "T04 — ACIW", "thread_code": "T04", "domain": "cognitive", "shard": "AcuTect-CODEX", "layers": ["L5","L6","L7","L8"], "sov": 10, "gov": "mandatory"},
    "testing": {"thread": "T04 — ACIW", "thread_code": "T04", "domain": "cognitive", "shard": "AcuTect-CODEX", "layers": ["L5","L6","L7","L8"], "sov": 10, "gov": "mandatory"},
    "coding": {"thread": "T04 — ACIW", "thread_code": "T04", "domain": "cognitive", "shard": "AcuTect-CODEX", "layers": ["L5","L6","L7","L8"], "sov": 10, "gov": "mandatory"},
    "development": {"thread": "T04 — ACIW", "thread_code": "T04", "domain": "cognitive", "shard": "AcuTect-CODEX", "layers": ["L5","L6","L7","L8"], "sov": 10, "gov": "mandatory"},
    "autonomous-coding": {"thread": "T04 — ACIW", "thread_code": "T04", "domain": "cognitive", "shard": "AcuTect-CODEX", "layers": ["L6","L7","L8","L9"], "sov": 10, "gov": "mandatory"},
    "ai-orchestration": {"thread": "T01 — COSM", "thread_code": "T01", "domain": "cognitive", "shard": "Diaran-MOE", "layers": ["L5","L6","L7","L8"], "sov": 10, "gov": "mandatory"},
    "agent-patterns": {"thread": "T01 — COSM", "thread_code": "T01", "domain": "cognitive", "shard": "Diaran-MOE", "layers": ["L5","L6","L7","L8"], "sov": 10, "gov": "mandatory"},
    "prompt-engineering": {"thread": "T01 — COSM", "thread_code": "T01", "domain": "cognitive", "shard": "ALL", "layers": ["L3","L4","L5","L6","L7"], "sov": 10, "gov": "mandatory"},
    "reasoning": {"thread": "T01 — COSM", "thread_code": "T01", "domain": "cognitive", "shard": "Diaran-MOE", "layers": ["L6","L7","L8"], "sov": 10, "gov": "mandatory"},
    "rag": {"thread": "T02 — DIAR", "thread_code": "T02", "domain": "cognitive", "shard": "APMS", "layers": ["L4","L5","L6"], "sov": 9, "gov": "restricted"},
    "knowledge": {"thread": "T02 — DIAR", "thread_code": "T02", "domain": "cognitive", "shard": "APMS", "layers": ["L4","L5","L6"], "sov": 9, "gov": "restricted"},
    "search": {"thread": "T02 — DIAR", "thread_code": "T02", "domain": "cognitive", "shard": "APMS", "layers": ["L4","L5","L6"], "sov": 9, "gov": "restricted"},
    "classification": {"thread": "T02 — DIAR", "thread_code": "T02", "domain": "cognitive", "shard": "APMS", "layers": ["L3","L4","L5"], "sov": 9, "gov": "restricted"},
    "summarization": {"thread": "T02 — DIAR", "thread_code": "T02", "domain": "cognitive", "shard": "APMS", "layers": ["L3","L4","L5"], "sov": 9, "gov": "restricted"},
    "nlp": {"thread": "T02 — DIAR", "thread_code": "T02", "domain": "cognitive", "shard": "APMS", "layers": ["L3","L4","L5"], "sov": 9, "gov": "restricted"},
    "multimodal": {"thread": "T03 — HISN", "thread_code": "T03", "domain": "cognitive", "shard": "Baranurion-L1", "layers": ["L1","L2","L3"], "sov": 9, "gov": "restricted"},
    "vision": {"thread": "T03 — HISN", "thread_code": "T03", "domain": "cognitive", "shard": "Baranurion-L1", "layers": ["L1","L2","L3"], "sov": 9, "gov": "restricted"},
    "audio": {"thread": "T03 — HISN", "thread_code": "T03", "domain": "cognitive", "shard": "Baranurion-L1", "layers": ["L1","L2","L3"], "sov": 9, "gov": "restricted"},
    "documentation": {"thread": "T02 — DIAR", "thread_code": "T02", "domain": "cognitive", "shard": "APMS", "layers": ["L4","L5","L6"], "sov": 9, "gov": "restricted"},
    "browser-automation": {"thread": "T05 — EREB", "thread_code": "T05", "domain": "cognitive", "shard": "UkhmaOS", "layers": ["L5","L6","L7"], "sov": 9, "gov": "restricted"},
    "context-engineering": {"thread": "T01 — COSM", "thread_code": "T01", "domain": "cognitive", "shard": "Diaran-MOE", "layers": ["L5","L6","L7","L8"], "sov": 10, "gov": "mandatory"},
    "mind-clone": {"thread": "T03 — HISN", "thread_code": "T03", "domain": "cognitive", "shard": "Baranurion-L1", "layers": ["L8","L9","L10"], "sov": 10, "gov": "sovereign"},
    
    # Commercial
    "web-dev": {"thread": "T14 — NAHRA", "thread_code": "T14", "domain": "commercial", "shard": "Commercial", "layers": ["L3","L4","L5"], "sov": 7, "gov": "advisory"},
    "frontend": {"thread": "T14 — NAHRA", "thread_code": "T14", "domain": "commercial", "shard": "Commercial", "layers": ["L3","L4","L5"], "sov": 7, "gov": "advisory"},
    "react": {"thread": "T14 — NAHRA", "thread_code": "T14", "domain": "commercial", "shard": "Commercial", "layers": ["L3","L4","L5"], "sov": 7, "gov": "advisory"},
    "ui-design": {"thread": "T14 — NAHRA", "thread_code": "T14", "domain": "commercial", "shard": "Commercial", "layers": ["L3","L4","L5"], "sov": 7, "gov": "advisory"},
    "css": {"thread": "T14 — NAHRA", "thread_code": "T14", "domain": "commercial", "shard": "Commercial", "layers": ["L3","L4","L5"], "sov": 7, "gov": "advisory"},
    "design": {"thread": "T14 — NAHRA", "thread_code": "T14", "domain": "commercial", "shard": "Commercial", "layers": ["L3","L4","L5"], "sov": 7, "gov": "advisory"},
    "figma": {"thread": "T14 — NAHRA", "thread_code": "T14", "domain": "commercial", "shard": "Commercial", "layers": ["L3","L4","L5"], "sov": 7, "gov": "advisory"},
    "customer-support": {"thread": "T15 — StratEdge", "thread_code": "T15", "domain": "commercial", "shard": "Commercial", "layers": ["L3","L4","L5"], "sov": 7, "gov": "advisory"},
    "business": {"thread": "T15 — StratEdge", "thread_code": "T15", "domain": "commercial", "shard": "Commercial", "layers": ["L3","L4","L5"], "sov": 7, "gov": "advisory"},
    "sales": {"thread": "T15 — StratEdge", "thread_code": "T15", "domain": "commercial", "shard": "Commercial", "layers": ["L3","L4","L5"], "sov": 7, "gov": "advisory"},
    "financial": {"thread": "T06 — EDNA", "thread_code": "T06", "domain": "cognitive", "shard": "StratEdge", "layers": ["L5","L6","L7"], "sov": 8, "gov": "restricted"},
    "analytics": {"thread": "T06 — EDNA", "thread_code": "T06", "domain": "cognitive", "shard": "StratEdge", "layers": ["L5","L6","L7"], "sov": 8, "gov": "restricted"},
    "role-persona": {"thread": "T14 — NAHRA", "thread_code": "T14", "domain": "commercial", "shard": "Commercial", "layers": ["L3","L4","L5"], "sov": 7, "gov": "advisory"},
    
    # Default
    "general": {"thread": "T01 — COSM", "thread_code": "T01", "domain": "cognitive", "shard": "Diaran-MOE", "layers": ["L3","L4","L5"], "sov": 7, "gov": "advisory"},
}

def slugify(name):
    """Convert to kebab-case slug."""
    s = name.lower().strip()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'[\s_]+', '-', s)
    s = re.sub(r'-+', '-', s).strip('-')
    return s[:100]

def classify_skill(name, description="", tags=None, source_repo=""):
    """Classify a skill into an Acuterium category based on content analysis."""
    text = f"{name} {description} {' '.join(tags or [])} {source_repo}".lower()
    
    # Security / Red-team
    if any(kw in text for kw in ['jailbreak', 'l1b3rt4s', 'adversarial', 'red-team', 'redteam', 'bypass']):
        return "red-team"
    if any(kw in text for kw in ['forensic', 'incident-response', 'dfir', 'disk-image', 'memory-dump']):
        return "forensics"
    if any(kw in text for kw in ['malware', 'rootkit', 'bootkit', 'ransomware', 'reverse-engineer']):
        return "malware"
    if any(kw in text for kw in ['pentest', 'penetration', 'exploit', 'vulnerability', 'vuln-triage', 'owasp', 'cve']):
        return "pentesting"
    if any(kw in text for kw in ['threat-intel', 'threat intelligence', 'apt-group', 'mitre', 'att&ck', 'campaign-attribution']):
        return "threat-intelligence"
    if any(kw in text for kw in ['system-prompt', 'leaked-prompt', 'leaked-gpt', 'system prompt']):
        return "system-prompts"
    if any(kw in text for kw in ['content-safety', 'content safety', 'moderation', 'content-filter']):
        return "content-safety"
    if any(kw in text for kw in ['security', 'cybersec', 'cyber-sec', 'secure-code', 'cspm', 'prowler', 'audit']):
        return "security"
    if any(kw in text for kw in ['identity', 'authentication', 'auth ', 'oauth', 'cognito', 'iam ', 'keyvault', 'secrets-manager']):
        return "auth"
    if any(kw in text for kw in ['encryption', 'crypto', 'certificate']):
        return "crypto"
    
    # Infrastructure / Cloud
    if any(kw in text for kw in ['azure', 'dotnet', '.net ']):
        return "cloud-azure"
    if any(kw in text for kw in ['aws', 'amazon', 'lambda', 'ec2', 'dynamodb', 's3 ', 'sqs', 'sns', 'ecs', 'eks', 'bedrock', 'cloudformation', 'cloudwatch', 'eventbridge', 'rds', 'step-function']):
        return "cloud-aws"
    if any(kw in text for kw in ['cloudflare', 'workers', 'wrangler', 'durable-object']):
        return "cloud"
    if any(kw in text for kw in ['mcp', 'model-context-protocol', 'mcp-server', 'mcp-builder']):
        return "mcp"
    if any(kw in text for kw in ['devops', 'ci/cd', 'cicd', 'docker', 'deploy', 'kubernetes', 'terraform', 'github-action']):
        return "devops"
    if any(kw in text for kw in ['blockchain', 'web3', 'onchain', 'ethereum', 'solidity', 'nft', 'defi', 'crypto-currency', 'erc-', 'farcaster']):
        return "blockchain"
    if any(kw in text for kw in ['monitoring', 'observability', 'appinsights', 'telemetry', 'logging']):
        return "monitoring"
    if any(kw in text for kw in ['infrastructure', 'cloud-solution', 'resource-health']):
        return "infrastructure"
    
    # Cognitive
    if any(kw in text for kw in ['mind-clone', 'persona', 'personality-clone', 'mind clone']):
        return "mind-clone"
    if any(kw in text for kw in ['context-engineering', 'context engineering', 'context-compress', 'context-optim', 'context-degrad', 'context-fundament']):
        return "context-engineering"
    if any(kw in text for kw in ['prompt-engineering', 'prompt engineering', 'few-shot', 'chain-of-thought', 'prompt chaining', 'structured prompt', 'meta-prompt']):
        return "prompt-engineering"
    if any(kw in text for kw in ['agent ', 'agentic', 'multi-agent', 'orchestrat', 'sub-agent', 'agent-pattern']):
        return "agent-patterns"
    if any(kw in text for kw in ['autonomous-cod', 'autonomous cod', 'self-heal', 'auto-fix']):
        return "autonomous-coding"
    if any(kw in text for kw in ['code-gen', 'code gen', 'code-review', 'code review', 'copilot', 'codeexplain', 'codecopilot']):
        return "code-review"
    if any(kw in text for kw in ['testing', 'test-auto', 'unit-test', 'vitest', 'jest', 'eval', 'benchmark']):
        return "testing"
    if any(kw in text for kw in ['python', 'typescript', 'javascript', 'java ', 'rust ', 'golang', 'ruby', '.net', 'csharp', 'c#', 'clojure']):
        return "coding"
    if any(kw in text for kw in ['rag', 'retriev', 'vector', 'embedding', 'knowledge-graph', 'knowledge graph']):
        return "rag"
    if any(kw in text for kw in ['classif', 'summariz', 'nlp', 'natural-language', 'text-process']):
        return "classification"
    if any(kw in text for kw in ['multimodal', 'vision', 'image', 'ocr', 'speech', 'audio', 'video']):
        return "multimodal"
    if any(kw in text for kw in ['extended-thinking', 'reasoning', 'chain-of-thought', 'sequential-think']):
        return "reasoning"
    if any(kw in text for kw in ['document', 'wiki', 'technical-writ', 'documentation']):
        return "documentation"
    if any(kw in text for kw in ['browser', 'browser-auto', 'computer-use', 'web-scrap']):
        return "browser-automation"
    if any(kw in text for kw in ['search', 'retriev', 'fetch']):
        return "search"
    
    # Commercial
    if any(kw in text for kw in ['figma', 'figma-design', 'figma-implement']):
        return "figma"
    if any(kw in text for kw in ['design', 'ui ', 'ux ', 'accessibility', 'layout', 'aesthetic', 'creative', 'bento', 'visual', 'animation', 'motion']):
        return "design"
    if any(kw in text for kw in ['react', 'next.js', 'nextjs', 'frontend', 'front-end', 'tailwind', 'css', 'html', 'webapp', 'web-app', 'web app']):
        return "frontend"
    if any(kw in text for kw in ['customer', 'support', 'chat-bot', 'chatbot']):
        return "customer-support"
    if any(kw in text for kw in ['financial', 'finance', 'accounting', 'trading', 'portfolio', 'wealth']):
        return "financial"
    if any(kw in text for kw in ['analytics', 'data-analy', 'dashboard', 'metric', 'kpi']):
        return "analytics"
    if any(kw in text for kw in ['business', 'sales', 'marketing', 'seo', 'entrepreneur', 'startup', 'sme ']):
        return "business"
    
    # Role-based personas
    if any(kw in text for kw in ['role:', 'act as', 'you are a', 'i want you to', 'consultant', 'advisor', 'expert', 'translator', 'tutor', 'coach']):
        return "role-persona"
    
    return "general"


def make_acu_skill(name, display_name, description, category, source_repo, source_file="", tags=None, author=""):
    """Create a normalized ACU skill entry."""
    mapping = CATEGORY_MAP.get(category, CATEGORY_MAP["general"])
    return {
        "skill_id": None,  # Assigned later sequentially
        "registry_id": str(uuid.uuid4())[:8],
        "name": slugify(name),
        "display_name": display_name[:200],
        "version": "1.0.0",
        "category": category,
        "thread": mapping["thread"],
        "thread_code": mapping["thread_code"],
        "domain": mapping["domain"],
        "description": (description or "No description available.")[:2000],
        "trigger_keywords": (tags or [])[:20],
        "delegation_targets": "",
        "key_systems": [mapping["shard"]],
        "sovereignty_score": mapping["sov"],
        "governance_level": mapping["gov"],
        "psi_minimum": 10.00,
        "status": "draft",
        "author": author or source_repo,
        "source_repo": source_repo,
        "source_file": source_file,
        "shard_affinity": mapping["shard"],
        "layer_access": mapping["layers"],
    }


def parse_yaml_frontmatter(content):
    """Extract YAML frontmatter from SKILL.md content."""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                return yaml.safe_load(parts[1]) or {}
            except:
                return {}
    return {}


def extract_description_from_md(content):
    """Extract description from markdown body."""
    lines = content.split('\n')
    desc_lines = []
    in_desc = False
    for line in lines:
        if line.strip().startswith('## Description') or line.strip().startswith('# '):
            if in_desc:
                break
            in_desc = True
            continue
        if in_desc and line.strip().startswith('## '):
            break
        if in_desc and line.strip():
            desc_lines.append(line.strip())
    if desc_lines:
        return ' '.join(desc_lines)[:1000]
    # Fallback: first non-empty paragraph after frontmatter
    body = content
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            body = parts[2]
    for line in body.split('\n'):
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('---'):
            return line[:500]
    return "Agent skill."


# ─── PARSERS ────────────────────────────────────────────────────────

def parse_antigravity(repo_path):
    """Parse antigravity-awesome-skills (1,232 skills from skills_index.json)."""
    skills = []
    index_file = os.path.join(repo_path, "skills_index.json")
    with open(index_file) as f:
        data = json.load(f)
    
    for entry in data:
        name = entry.get("name", entry.get("id", "unknown"))
        desc = entry.get("description", "")
        cat = classify_skill(name, desc, source_repo="antigravity")
        skill = make_acu_skill(
            name=name,
            display_name=name.replace("-", " ").title(),
            description=desc,
            category=cat,
            source_repo="sickn33/antigravity-awesome-skills",
            source_file=entry.get("path", "skills_index.json"),
            tags=[entry.get("category", "")] + entry.get("tags", []) if "tags" in entry else [entry.get("category", "")],
            author="antigravity-community"
        )
        skills.append(skill)
    print(f"  [antigravity] Parsed {len(skills)} skills")
    return skills


def parse_skillmd_repo(repo_path, repo_slug, expected_path="skills/*/SKILL.md"):
    """Parse repos with standard SKILL.md structure."""
    skills = []
    pattern = os.path.join(repo_path, expected_path)
    for skill_file in globmod.glob(pattern, recursive=True):
        try:
            with open(skill_file) as f:
                content = f.read()
            fm = parse_yaml_frontmatter(content)
            name = fm.get("name", os.path.basename(os.path.dirname(skill_file)))
            display = fm.get("display_name", name.replace("-", " ").title())
            desc = fm.get("description", extract_description_from_md(content))
            triggers = fm.get("triggers", fm.get("trigger_keywords", []))
            if isinstance(triggers, str):
                triggers = [t.strip() for t in triggers.split(",")]
            cat = classify_skill(name, desc, triggers, repo_slug)
            skill = make_acu_skill(
                name=name,
                display_name=display,
                description=desc,
                category=cat,
                source_repo=repo_slug,
                source_file=os.path.relpath(skill_file, repo_path),
                tags=triggers,
                author=fm.get("author", repo_slug)
            )
            skills.append(skill)
        except Exception as e:
            print(f"  Warning: Failed to parse {skill_file}: {e}")
    print(f"  [{repo_slug}] Parsed {len(skills)} skills")
    return skills


def parse_microsoft_skills(repo_path):
    """Parse microsoft/skills (169 SKILL.md files)."""
    skills = []
    for skill_file in globmod.glob(os.path.join(repo_path, "**", "SKILL.md"), recursive=True):
        try:
            with open(skill_file) as f:
                content = f.read()
            fm = parse_yaml_frontmatter(content)
            name = fm.get("name", os.path.basename(os.path.dirname(skill_file)))
            display = fm.get("display_name", name.replace("-", " ").title())
            desc = fm.get("description", extract_description_from_md(content))
            triggers = fm.get("triggers", [])
            if isinstance(triggers, str):
                triggers = [t.strip() for t in triggers.split(",")]
            cat = classify_skill(name, desc, triggers, "microsoft/skills")
            skill = make_acu_skill(
                name=name,
                display_name=display,
                description=desc,
                category=cat,
                source_repo="microsoft/skills",
                source_file=os.path.relpath(skill_file, repo_path),
                tags=triggers,
                author="Microsoft"
            )
            skills.append(skill)
        except Exception as e:
            print(f"  Warning: Failed to parse {skill_file}: {e}")
    print(f"  [microsoft] Parsed {len(skills)} skills")
    return skills


def parse_cybersecurity_skills(repo_path):
    """Parse Anthropic-Cybersecurity-Skills (611 skills in skills/ subdirs)."""
    skills = []
    skills_dir = os.path.join(repo_path, "skills")
    for entry in sorted(os.listdir(skills_dir)):
        skill_path = os.path.join(skills_dir, entry)
        if not os.path.isdir(skill_path):
            continue
        skill_file = os.path.join(skill_path, "SKILL.md")
        if os.path.exists(skill_file):
            try:
                with open(skill_file) as f:
                    content = f.read()
                fm = parse_yaml_frontmatter(content)
                name = fm.get("name", entry)
                display = fm.get("display_name", entry.replace("-", " ").title())
                desc = fm.get("description", extract_description_from_md(content))
                triggers = fm.get("triggers", [])
                if isinstance(triggers, str):
                    triggers = [t.strip() for t in triggers.split(",")]
                cat = classify_skill(name, desc, triggers, "cybersecurity")
                skill = make_acu_skill(
                    name=name,
                    display_name=display,
                    description=desc,
                    category=cat,
                    source_repo="mukul975/Anthropic-Cybersecurity-Skills",
                    source_file=f"skills/{entry}/SKILL.md",
                    tags=triggers,
                    author="cybersecurity-community"
                )
                skills.append(skill)
            except Exception as e:
                print(f"  Warning: Failed to parse {skill_file}: {e}")
    print(f"  [cybersecurity] Parsed {len(skills)} skills")
    return skills


def parse_awesome_copilot(repo_path):
    """Parse github/awesome-copilot (210+ skills)."""
    skills = []
    # Skills directory
    skills_dir = os.path.join(repo_path, "skills")
    if os.path.isdir(skills_dir):
        for entry in sorted(os.listdir(skills_dir)):
            skill_path = os.path.join(skills_dir, entry)
            if not os.path.isdir(skill_path):
                continue
            skill_file = os.path.join(skill_path, "SKILL.md")
            if os.path.exists(skill_file):
                try:
                    with open(skill_file) as f:
                        content = f.read()
                    fm = parse_yaml_frontmatter(content)
                    name = fm.get("name", entry)
                    display = fm.get("display_name", entry.replace("-", " ").title())
                    desc = fm.get("description", extract_description_from_md(content))
                    triggers = fm.get("triggers", [])
                    if isinstance(triggers, str):
                        triggers = [t.strip() for t in triggers.split(",")]
                    cat = classify_skill(name, desc, triggers, "github/awesome-copilot")
                    skill = make_acu_skill(
                        name=f"copilot-{name}" if not name.startswith("copilot") else name,
                        display_name=display,
                        description=desc,
                        category=cat,
                        source_repo="github/awesome-copilot",
                        source_file=f"skills/{entry}/SKILL.md",
                        tags=triggers,
                        author="GitHub Copilot Community"
                    )
                    skills.append(skill)
                except Exception as e:
                    print(f"  Warning: {e}")
    print(f"  [awesome-copilot] Parsed {len(skills)} skills")
    return skills


def parse_design_agent(repo_path):
    """Parse andersoncollab/design-agent (47 skills)."""
    skills = []
    skills_dir = os.path.join(repo_path, "skills")
    if os.path.isdir(skills_dir):
        for entry in sorted(os.listdir(skills_dir)):
            skill_path = os.path.join(skills_dir, entry)
            if not os.path.isdir(skill_path):
                continue
            skill_file = os.path.join(skill_path, "SKILL.md")
            if os.path.exists(skill_file):
                try:
                    with open(skill_file) as f:
                        content = f.read()
                    fm = parse_yaml_frontmatter(content)
                    name = fm.get("name", entry)
                    display = fm.get("display_name", entry.replace("-", " ").title())
                    desc = fm.get("description", extract_description_from_md(content))
                    triggers = fm.get("triggers", [])
                    if isinstance(triggers, str):
                        triggers = [t.strip() for t in triggers.split(",")]
                    cat = classify_skill(name, desc, triggers, "design-agent")
                    skill = make_acu_skill(
                        name=name,
                        display_name=display,
                        description=desc,
                        category=cat,
                        source_repo="andersoncollab/design-agent",
                        source_file=f"skills/{entry}/SKILL.md",
                        tags=triggers,
                        author="andersoncollab"
                    )
                    skills.append(skill)
                except Exception as e:
                    print(f"  Warning: {e}")
    print(f"  [design-agent] Parsed {len(skills)} skills")
    return skills


def parse_context_engineering(repo_path):
    """Parse Agent-Skills-for-Context-Engineering."""
    skills = []
    # Parse from skills/ and examples/
    for pattern in ["skills/*/SKILL.md", "examples/*/SKILL.md", "examples/*/generated_skills/*/SKILL.md"]:
        for skill_file in globmod.glob(os.path.join(repo_path, pattern)):
            try:
                with open(skill_file) as f:
                    content = f.read()
                fm = parse_yaml_frontmatter(content)
                dirname = os.path.basename(os.path.dirname(skill_file))
                name = fm.get("name", dirname)
                display = fm.get("display_name", dirname.replace("-", " ").title())
                desc = fm.get("description", extract_description_from_md(content))
                triggers = fm.get("triggers", [])
                if isinstance(triggers, str):
                    triggers = [t.strip() for t in triggers.split(",")]
                cat = classify_skill(name, desc, triggers, "context-engineering")
                skill = make_acu_skill(
                    name=name,
                    display_name=display,
                    description=desc,
                    category=cat,
                    source_repo="muratcankoylan/Agent-Skills-for-Context-Engineering",
                    source_file=os.path.relpath(skill_file, repo_path),
                    tags=triggers,
                    author="muratcankoylan"
                )
                skills.append(skill)
            except Exception as e:
                print(f"  Warning: {e}")
    print(f"  [context-engineering] Parsed {len(skills)} skills")
    return skills


def parse_mind_cloning(repo_path):
    """Parse yzfly/Mind-Cloning-Engineering."""
    skills = []
    # Main skill
    main_skill = os.path.join(repo_path, "skills", "mind-clone", "SKILL.md")
    if os.path.exists(main_skill):
        with open(main_skill) as f:
            content = f.read()
        fm = parse_yaml_frontmatter(content)
        skill = make_acu_skill(
            name="mind-clone-framework",
            display_name="Mind Cloning Engineering Framework",
            description=fm.get("description", "Framework for creating AI personality clones with structured prompts."),
            category="mind-clone",
            source_repo="yzfly/Mind-Cloning-Engineering",
            source_file="skills/mind-clone/SKILL.md",
            tags=["mind-clone", "personality", "persona", "AI clone"],
            author="yzfly"
        )
        skills.append(skill)
    
    # Personas
    persona_dir = os.path.join(repo_path, "skills", "mind-clone", "personas")
    if os.path.isdir(persona_dir):
        for f in os.listdir(persona_dir):
            if f.endswith(".md"):
                name = f.replace(".md", "")
                skill = make_acu_skill(
                    name=f"mind-clone-{name}",
                    display_name=f"Mind Clone — {name.replace('-', ' ').title()}",
                    description=f"Mind clone persona: {name.replace('-', ' ').title()}. AI personality simulation.",
                    category="mind-clone",
                    source_repo="yzfly/Mind-Cloning-Engineering",
                    source_file=f"skills/mind-clone/personas/{f}",
                    tags=["mind-clone", "persona", name],
                    author="yzfly"
                )
                skills.append(skill)
    print(f"  [mind-cloning] Parsed {len(skills)} skills")
    return skills


def parse_figma_agents(repo_path):
    """Parse steelhead-command/claude-figma-agents."""
    skills = []
    for subdir in ["agents", "commands"]:
        dir_path = os.path.join(repo_path, subdir)
        if os.path.isdir(dir_path):
            for f in os.listdir(dir_path):
                if f.endswith(".md"):
                    name = f.replace(".md", "")
                    filepath = os.path.join(dir_path, f)
                    with open(filepath) as fh:
                        content = fh.read()
                    desc = content[:300].strip().split('\n')[0] if content else f"Figma {subdir}: {name}"
                    skill = make_acu_skill(
                        name=f"figma-{name}",
                        display_name=f"Figma — {name.replace('-', ' ').title()}",
                        description=desc,
                        category="figma",
                        source_repo="steelhead-command/claude-figma-agents",
                        source_file=f"{subdir}/{f}",
                        tags=["figma", "design", name],
                        author="steelhead-command"
                    )
                    skills.append(skill)
    print(f"  [figma-agents] Parsed {len(skills)} skills")
    return skills


def parse_security_skills(repo_path, repo_slug):
    """Parse Skills-security and similar repos with SKILL.md in subdirs."""
    skills = []
    for entry in sorted(os.listdir(repo_path)):
        skill_path = os.path.join(repo_path, entry)
        if not os.path.isdir(skill_path) or entry.startswith('.'):
            continue
        skill_file = os.path.join(skill_path, "SKILL.md")
        if os.path.exists(skill_file):
            with open(skill_file) as f:
                content = f.read()
            fm = parse_yaml_frontmatter(content)
            name = fm.get("name", entry)
            display = fm.get("display_name", entry.replace("-", " ").title())
            desc = fm.get("description", extract_description_from_md(content))
            triggers = fm.get("triggers", [])
            if isinstance(triggers, str):
                triggers = [t.strip() for t in triggers.split(",")]
            cat = classify_skill(name, desc, triggers, "security")
            skill = make_acu_skill(
                name=name,
                display_name=display,
                description=desc,
                category=cat,
                source_repo=repo_slug,
                source_file=f"{entry}/SKILL.md",
                tags=triggers,
                author=repo_slug
            )
            skills.append(skill)
    print(f"  [{repo_slug}] Parsed {len(skills)} skills")
    return skills


def parse_single_skill(repo_path, repo_slug, name, display_name, description, category, tags=None):
    """Create a single skill from a whole repo."""
    skill = make_acu_skill(
        name=name,
        display_name=display_name,
        description=description,
        category=category,
        source_repo=repo_slug,
        source_file="SKILL.md",
        tags=tags or [],
        author=repo_slug
    )
    print(f"  [{repo_slug}] Parsed 1 skill")
    return [skill]


# ─── MAIN HARVESTER ─────────────────────────────────────────────────

def harvest_all():
    """Harvest skills from all 21 repos."""
    all_skills = []
    base = REPO_BASE
    
    print("=" * 60)
    print("ACUTERIUM SKILLS MARKETPLACE — MASS HARVESTER")
    print("=" * 60)
    
    # ── BATCH 1: Large JSON/structured sources ──
    print("\n── BATCH 1: Large structured sources ──")
    all_skills += parse_antigravity(os.path.join(base, "antigravity-awesome-skills"))
    all_skills += parse_microsoft_skills(os.path.join(base, "microsoft-skills"))
    all_skills += parse_cybersecurity_skills(os.path.join(base, "Anthropic-Cybersecurity-Skills"))
    all_skills += parse_awesome_copilot(os.path.join(base, "awesome-copilot"))
    
    # ── BATCH 2: Standard SKILL.md repos ──
    print("\n── BATCH 2: Standard SKILL.md repos ──")
    all_skills += parse_skillmd_repo(os.path.join(base, "anthropic-skills"), "anthropics/skills")
    all_skills += parse_skillmd_repo(os.path.join(base, "agent-skills"), "vercel-labs/agent-skills")
    all_skills += parse_skillmd_repo(os.path.join(base, "aws-agent-skills"), "itsmostafa/aws-agent-skills")
    all_skills += parse_skillmd_repo(os.path.join(base, "vercel-skills"), "vercel-labs/skills")
    all_skills += parse_skillmd_repo(os.path.join(base, "cloudflare-skills"), "cloudflare/skills")
    all_skills += parse_skillmd_repo(os.path.join(base, "bankrbot-skills"), "BankrBot/skills")
    
    # BankrBot is in 'skills' directory (the first clone)
    bankrbot_path = os.path.join(base, "skills")
    bankrbot_skills_dir = os.path.join(bankrbot_path, "skills")
    if os.path.isdir(bankrbot_skills_dir):
        # Already covered by bankrbot-skills, but let's check
        pass
    
    # ── BATCH 3: Specialized repos ──
    print("\n── BATCH 3: Specialized repos ──")
    all_skills += parse_design_agent(os.path.join(base, "design-agent"))
    all_skills += parse_context_engineering(os.path.join(base, "Agent-Skills-for-Context-Engineering"))
    all_skills += parse_mind_cloning(os.path.join(base, "Mind-Cloning-Engineering"))
    all_skills += parse_figma_agents(os.path.join(base, "claude-figma-agents"))
    
    # ── BATCH 4: Security-focused repos ──
    print("\n── BATCH 4: Security-focused repos ──")
    all_skills += parse_security_skills(os.path.join(base, "Skills-security"), "Poatan222/Skills-security")
    
    # cyberaudit-skill
    cyberaudit_path = os.path.join(base, "cyberaudit-skill", "SKILL.md")
    if os.path.exists(cyberaudit_path):
        with open(cyberaudit_path) as f:
            content = f.read()
        fm = parse_yaml_frontmatter(content)
        all_skills += parse_single_skill(
            os.path.join(base, "cyberaudit-skill"),
            "dremonkey23/cyberaudit-skill",
            fm.get("name", "cyberaudit"),
            fm.get("display_name", "Cyber Audit Skill"),
            fm.get("description", "Automated cybersecurity audit skill for Unix and Windows."),
            "security",
            fm.get("triggers", ["cyberaudit", "security audit"])
        )
    
    # RealistSec resources
    all_skills += parse_skillmd_repo(os.path.join(base, "resources"), "RealistSec/resources")
    
    # ── BATCH 5: Remaining repos (single/few skills) ──
    print("\n── BATCH 5: Remaining repos ──")
    
    # agentskills spec
    all_skills += parse_single_skill(
        os.path.join(base, "agentskills"),
        "agentskills/agentskills",
        "agent-skills-specification",
        "Agent Skills Specification Standard",
        "Open specification standard for defining agent skills with SKILL.md format, YAML frontmatter, and progressive disclosure.",
        "agent-patterns",
        ["agent-skills", "specification", "SKILL.md", "standard"]
    )
    
    # Acontext
    all_skills += parse_single_skill(
        os.path.join(base, "Acontext"),
        "memodb-io/Acontext",
        "acontext-memory",
        "Acontext Memory System",
        "Memory-driven context management system for AI agents. Provides persistent context, knowledge graphs, and adaptive memory.",
        "rag",
        ["memory", "context", "knowledge-graph", "agent-memory"]
    )
    
    # Wiseflow
    all_skills += parse_single_skill(
        os.path.join(base, "wiseflow"),
        "TeamWiseFlow/wiseflow",
        "wiseflow-information-extraction",
        "WiseFlow Information Extraction",
        "AI-powered information extraction and analysis agent. Monitors web sources, extracts structured data, and generates insights.",
        "search",
        ["information-extraction", "web-monitoring", "data-analysis"]
    )
    
    # Snyk agent-scan
    all_skills += parse_single_skill(
        os.path.join(base, "agent-scan"),
        "snyk/agent-scan",
        "snyk-agent-scan",
        "Snyk Agent Security Scanner",
        "Security scanning agent for detecting vulnerabilities in code and dependencies. SAST, SCA, and IaC scanning.",
        "security",
        ["snyk", "security-scan", "vulnerability", "SAST", "SCA"]
    )
    
    print(f"\n{'=' * 60}")
    print(f"TOTAL HARVESTED: {len(all_skills)} skills")
    print(f"{'=' * 60}")
    
    return all_skills


def deduplicate_skills(skills):
    """Remove duplicate skills by name similarity."""
    seen = {}
    unique = []
    for skill in skills:
        key = skill["name"].lower().strip()
        if key not in seen:
            seen[key] = True
            unique.append(skill)
    print(f"Deduplication: {len(skills)} → {len(unique)} unique skills")
    return unique


def assign_sequential_ids(skills, start_id=10):
    """Assign ACU-SKILL-XXXX IDs sequentially."""
    for i, skill in enumerate(skills):
        skill["skill_id"] = f"ACU-SKILL-{start_id + i:04d}"
    return skills


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Harvest all skills
    all_skills = harvest_all()
    
    # Deduplicate
    unique_skills = deduplicate_skills(all_skills)
    
    # Assign IDs (starting at ACU-SKILL-0010)
    unique_skills = assign_sequential_ids(unique_skills, start_id=10)
    
    # Save raw harvested data
    with open(os.path.join(OUTPUT_DIR, "all_harvested_skills.json"), "w") as f:
        json.dump(unique_skills, f, indent=2, ensure_ascii=False)
    
    print(f"\nSaved {len(unique_skills)} skills to {OUTPUT_DIR}/all_harvested_skills.json")
    
    # Print domain distribution
    domains = {}
    categories = {}
    for s in unique_skills:
        domains[s["domain"]] = domains.get(s["domain"], 0) + 1
        categories[s["category"]] = categories.get(s["category"], 0) + 1
    
    print("\n── DOMAIN DISTRIBUTION ──")
    for d, c in sorted(domains.items(), key=lambda x: -x[1]):
        print(f"  {d}: {c}")
    
    print("\n── TOP 20 CATEGORIES ──")
    for cat, c in sorted(categories.items(), key=lambda x: -x[1])[:20]:
        print(f"  {cat}: {c}")
    
    return unique_skills


if __name__ == "__main__":
    main()
