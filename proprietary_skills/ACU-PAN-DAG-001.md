---
skill_id: ACU-SKILL-PAN-008
name: dag-engine
display_name: DAG Engine — Directed Acyclic Graph Task Execution
description: >
  Executes multi-step tasks as a Directed Acyclic Graph with dependency resolution,
  topological ordering, parallel execution support, and compliance validation.
  Ensures tasks execute in correct order respecting inter-task dependencies.
category: Workflow Execution
domain: infrastructure
acuterium_shard: ADOCP
acuterium_layers: L5; L6; L7
sovereignty_score: 9
governance_level: mandatory
author: Acuterium Technologies Inc.
license: Proprietary-ACU
version: 1.0.0
status: published
tags: dag; dependency; topological-sort; parallel-execution; workflow; pipeline
trigger_keywords: >
  dag execution; dependency graph; topological sort; parallel tasks;
  workflow pipeline; task dependencies; execution order; cycle detection
---

# DAG Engine — Directed Acyclic Graph Task Execution

## Architecture

Nodes represent tasks. Edges represent dependencies. Execution proceeds in
topological order — a node executes only after all its dependencies complete.

## Core Functions

### `add_node(node_id, task, dependencies)`
Register a task node with its dependency list.

### `validate_dag() → bool`
Cycle detection via DFS with recursion stack. Returns False if cycles found.

### `topological_sort() → List[str]`
Returns nodes in valid execution order using recursive DFS visitation.

### `execute() → Dict[str, Any]`
Full execution: validate → sort → execute in order. Nodes with failed dependencies are SKIPPED.
Status tracking: PENDING → RUNNING → COMPLETED/FAILED/SKIPPED.

## Task Status Enum
`PENDING` | `RUNNING` | `COMPLETED` | `FAILED` | `SKIPPED`

## Pan Integration

- **Pan Pipeline**: The 8-phase pipeline itself is a DAG (CATEGORIZE depends on INGEST, etc.)
- **Phase 4 Execution**: Complex multi-step tasks decomposed into DAG nodes
- **War Game Plan**: 7 phases with inter-phase dependencies managed via DAG ordering
- **Task Categorizer**: Dependencies parsed from task input feed into DAG construction
