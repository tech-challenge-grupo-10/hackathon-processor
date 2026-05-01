# Implementation Plan: [FEATURE]

**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [link]
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/plan-template.md` for the execution workflow.

## Summary

[Extract from feature spec: primary requirement + technical approach from research]

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: [e.g., Python 3.11, Swift 5.9, Rust 1.75 or NEEDS CLARIFICATION]  
**Primary Dependencies**: [e.g., FastAPI, UIKit, LLVM or NEEDS CLARIFICATION]  
**Storage**: [if applicable, e.g., PostgreSQL, CoreData, files or N/A]  
**Testing**: [e.g., pytest, XCTest, cargo test or NEEDS CLARIFICATION]  
**Target Platform**: [e.g., Linux server, iOS 15+, WASM or NEEDS CLARIFICATION]
**Project Type**: [e.g., library/cli/web-service/mobile-app/compiler/desktop-app or NEEDS CLARIFICATION]  
**Performance Goals**: [domain-specific, e.g., 1000 req/s, 10k lines/sec, 60 fps or NEEDS CLARIFICATION]  
**Constraints**: [domain-specific, e.g., <200ms p95, <100MB memory, offline-capable or NEEDS CLARIFICATION]  
**Scale/Scope**: [domain-specific, e.g., 10k users, 1M LOC, 50 screens or NEEDS CLARIFICATION]

## Constitution Check

*CURRENT CONSTITUTION: 1.0.0 — Code Quality, Testing Standards, UX Consistency, Performance Requirements*

[GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.]

### I. Code Quality Gates (CONSTITUTION §I)

- [ ] All public APIs have type annotations
- [ ] All functions have docstrings (purpose, parameters, return, exceptions)
- [ ] No functions exceed 30 lines (exception: complex algorithms with comments)
- [ ] Error handling explicit, no silent failures
- [ ] Security review complete for sensitive operations
- [ ] Code style linted and formatting enforced

### II. Testing Gates (CONSTITUTION §II)

- [ ] Test pyramid established (unit ≥60%, integration ≥20%, e2e ≤10%)
- [ ] Minimum 80% branch coverage target defined
- [ ] Tests written first and failing before implementation
- [ ] Contract tests at all public API boundaries
- [ ] No god tests; each test independent and idempotent
- [ ] Mock external dependencies in test environment
- [ ] CI pipeline passes all tests before merging

### III. UX Consistency Gates (CONSTITUTION §III)

- [ ] Design system applied; custom components reviewed
- [ ] Navigation follows platform conventions
- [ ] Error messages user-friendly and actionable
- [ ] Accessibility requirements (WCAG 2.1 AA) addressed
- [ ] Loading states documented for async operations
- [ ] i18n strings extracted, hardcoded text avoided

### IV. Performance Gates (CONSTITUTION §IV)

- [ ] SLOs defined per service (e.g., p95 <200ms critical)
- [ ] Resource budgets documented (memory, CPU limits)
- [ ] Scalability targets defined and tested
- [ ] Monitoring/alerting configured for SLOs
- [ ] Latency budgeting documented per critical path

### Gate Results

**Phase 0 Status**: `NEEDS COMPLETE REVIEW` | **Phase 1 Status**: `NEEDS COMPLETE REVIEW`

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->

```text
# [REMOVE IF UNUSED] Option 1: Single project (DEFAULT)
src/
├── models/
├── services/
├── cli/
└── lib/

tests/
├── contract/
├── integration/
└── unit/

# [REMOVE IF UNUSED] Option 2: Web application (when "frontend" + "backend" detected)
backend/
├── src/
│   ├── models/
│   ├── services/
│   └── api/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/

# [REMOVE IF UNUSED] Option 3: Mobile + API (when "iOS/Android" detected)
api/
└── [same as backend above]

ios/ or android/
└── [platform-specific structure: feature modules, UI flows, platform tests]
```

**Structure Decision**: [Document the selected structure and reference the real
directories captured above]

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
