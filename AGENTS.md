# AGENTS.md — Freelancer Webscraping

## 1. Project Overview

**Project:** Freelancer Webscraping

This project is a Python-based web scraping application with FastAPI capabilities.

AI coding agents must prioritize correctness, maintainability, reliability, and minimal implementation complexity.

All changes must follow the project's Constitution, existing architecture, and applicable feature specifications.

## 2. Source of Truth

Before implementing or modifying code, consult the following resources when available:

1. `.specify/memory/constitution.md` — Mandatory engineering principles and architectural rules.
2. `specs/` — Feature specifications, requirements, and acceptance criteria.
3. `README.md` — Project documentation and execution instructions.
4. `pyproject.toml` — Dependencies and development tooling.
5. Existing source code and tests — Established implementation patterns.

### Instruction Priority

- The Constitution defines mandatory engineering standards.
- Feature specifications define the expected behavior and acceptance criteria.
- This file defines how AI agents should operate within the repository.
- Existing code establishes implementation conventions, provided they do not conflict with higher-priority requirements.

If instructions conflict, identify the conflict instead of silently choosing an incompatible implementation.

Do not duplicate or redefine principles already established in the Constitution.

## 3. Technology Stack

| Category | Technology |
|---|---|
| Language | Python 3.13 |
| API Framework | FastAPI |
| Testing | Pytest |
| Type Checking | mypy |
| Linting & Formatting | Ruff |
| Logging | Loguru |
| Environment Configuration | python-dotenv |

Additional dependencies must be verified against `pyproject.toml` before use.

Prefer the Python standard library and existing dependencies before introducing new packages.

Do not add dependencies without a concrete technical requirement.

## 4. Development Workflow

### 4.1 Before Implementation

AI agents must:

1. Read the project Constitution.
2. Read the relevant specification under `specs/`, if one exists.
3. Identify the acceptance criteria.
4. Inspect the affected source files and their dependencies.
5. Review related tests and existing implementation patterns.
6. Use CodeGraph to explore relationships when available and useful.
7. Determine the smallest change required to complete the task.

For larger features, establish an implementation plan before changing code.

For small bug fixes or isolated adjustments, avoid unnecessary planning artifacts.

Do not introduce functionality that is not required by the task.

### 4.2 During Implementation

- Follow the existing project structure.
- Preserve architectural boundaries.
- Keep changes focused on the requested behavior.
- Prefer existing functions, classes, utilities, and dependencies.
- Use type hints in public functions and methods.
- Keep business logic independent from HTTP and infrastructure concerns.
- Update affected callers when modifying function contracts.
- Preserve existing validation, security, and error-handling behavior.
- Add or update tests for changed behavior.
- Avoid unnecessary refactoring.

Do not create abstractions, wrappers, configuration options, or extensibility mechanisms without a present requirement.

### 4.3 After Implementation

AI agents must:

1. Review the changes against the acceptance criteria.
2. Confirm that unrelated functionality was not modified.
3. Run the relevant automated tests.
4. Run configured linting and type checks.
5. Inspect failures and address their root causes.
6. Review the changes for compliance with the Constitution.
7. Report the final implementation and verification status.

Never claim a test or validation succeeded unless it was actually executed successfully.

## 5. Architecture & Code Organization

The project follows an object-oriented, modular approach.

### General Rules

- Separate responsibilities into cohesive classes and modules.
- Prefer composition over complex inheritance hierarchies.
- Each class should have a clear purpose.
- Use functions instead of classes when state or abstraction is unnecessary.
- Avoid circular dependencies.
- Keep implementation details encapsulated.
- Respect the existing package structure.

### Responsibility Boundaries

- **Scrapers:** Page retrieval, navigation, parsing, and extraction.
- **Services:** Business rules and workflow orchestration.
- **Models:** Internal data representations.
- **Schemas:** Data validation and serialization.
- **Repositories/Storage:** Data persistence and retrieval.
- **API:** FastAPI routes, HTTP contracts, and dependencies.
- **Core:** Configuration, shared infrastructure, and logging setup.
- **Utilities:** Small reusable operations that do not belong to a specific domain.

These boundaries describe responsibilities, not mandatory directories.

Do not create unused modules or architectural layers merely to match this list.

## 6. Web Scraping & Playwright Guidelines

Playwright is the official technology for browser automation, navigation, and data extraction.

All scraping implementations MUST use Playwright unless a different approach is explicitly approved.

### 6.1 Browser Automation

- Prefer Playwright's asynchronous Python API (`playwright.async_api`).
- Use `BrowserContext` to isolate scraping sessions.
- Reuse browser instances when appropriate.
- Create separate contexts for independent sessions.
- Close pages, contexts, and browsers properly.
- Configure explicit navigation and operation timeouts.
- Avoid unnecessary browser launches.
- Use headless mode by default, unless interactive execution is required.
- Avoid mixing synchronous and asynchronous Playwright APIs in the same execution flow.

### 6.2 Navigation & Waiting

- Prefer Playwright's built-in auto-waiting mechanisms.
- Use `Locator` objects for interacting with page elements.
- Use explicit waits for meaningful page states when necessary.
- Avoid arbitrary `sleep()` calls.
- Do not depend exclusively on `networkidle` for page readiness.
- Handle redirects, navigation failures, timeouts, and dynamically loaded content.
- Use pagination and scrolling only when required by the target application.

### 6.3 Data Extraction

- Use Playwright locators as the primary extraction mechanism.
- Prefer stable locators based on roles, labels, test IDs, or meaningful attributes.
- Use CSS selectors when semantic locators are unavailable or unsuitable.
- Avoid fragile XPath expressions and deeply nested CSS selectors.
- Centralize reusable selectors and target URLs.
- Keep extraction logic separate from browser initialization and navigation.
- Validate extracted data before further processing.
- Handle missing elements, empty values, and unexpected page structures explicitly.
- Preserve existing extraction contracts unless changes are approved.

### 6.4 Scraper Architecture

Organize scraping responsibilities into clearly separated components:

- **Browser Management:** Browser lifecycle, contexts, sessions, and cleanup.
- **Navigation:** Page navigation, pagination, and interaction flows.
- **Extraction:** Locate elements and extract raw information.
- **Processing:** Normalize, validate, and transform extracted data.
- **Storage:** Persist processed information when required.

These are logical responsibilities, not mandatory classes or directories.

Follow existing project patterns and avoid unnecessary abstractions.

### 6.5 Error Handling & Reliability

- Handle Playwright timeouts explicitly.
- Distinguish navigation failures from extraction failures.
- Detect missing or changed page elements.
- Apply bounded retries only to recoverable operations.
- Avoid retrying non-idempotent actions without safeguards.
- Log relevant execution context using Loguru.
- Never silently ignore extraction errors.
- Ensure resources are released after failures.

### 6.6 Responsible Scraping

- Respect applicable `robots.txt` directives.
- Follow target-site terms and access requirements.
- Implement reasonable request pacing and concurrency limits.
- Do not bypass authentication, CAPTCHAs, or access restrictions.
- Avoid excessive requests that could degrade target-site availability.

### 6.7 Testing Playwright Scrapers

- Use Pytest for automated testing.
- Prefer local HTML fixtures for extraction tests.
- Mock external services where appropriate.
- Test missing elements and unexpected HTML structures.
- Test timeout and navigation-failure scenarios.
- Avoid dependencies on live websites in standard unit tests.
- Keep browser integration tests separate from isolated unit tests.
- Ensure tests close Playwright resources after execution.

### 6.8 Performance

- Reuse browser instances when beneficial.
- Limit concurrent pages and contexts.
- Avoid unnecessary page reloads.
- Extract only the data required by the specification.
- Avoid CPU-intensive processing in asynchronous browser routines.
- Measure performance before introducing concurrency optimizations. 

## 7. Configuration & Secrets

All environment-specific or sensitive configuration must be managed centrally.

- Use `.env` for local environment configuration.
- Use `python-dotenv` according to the existing project configuration.
- Access settings through a centralized configuration module.
- Prefer `pydantic-settings` when already adopted by the application.
- Do not introduce multiple competing configuration mechanisms.
- Never hardcode credentials, tokens, API keys, or secrets.
- Keep environment-dependent URLs and frequently changed values configurable.
- Stable, non-sensitive constants may remain in source code when appropriate.
- Never commit sensitive `.env` files.
- Update `.env.example` when introducing required environment variables.

Configuration changes must preserve compatibility with existing environments unless explicitly approved.

## 8. Logging & Error Handling

Loguru is the project's logging library.

### Logging

- Configure Loguru once during application initialization.
- Reuse the configured logger across modules.
- Prefer descriptive messages with relevant execution context.
- Use appropriate logging levels.
- Include useful identifiers when available.
- Avoid unnecessary logging inside high-frequency operations.
- Never log passwords, tokens, credentials, or sensitive information.

### Error Handling

- Handle expected exceptions at appropriate boundaries.
- Preserve original exception context when re-raising errors.
- Do not use broad exception handling without justification.
- Do not silently suppress failures.
- Distinguish recoverable failures from terminal errors.
- Provide actionable diagnostic information.
- Ensure failed scraping operations have clear outcomes.

Retries must not hide persistent failures.

## 9. Code Quality & Development Style

### Implementation Principles

- Implement only what was requested.
- Prefer the smallest complete solution.
- Keep changes localized and readable.
- Reuse existing helpers before creating new ones.
- Avoid premature optimization.
- Avoid speculative abstractions.
- Fix bugs at their root cause.
- Preserve public contracts and existing behavior.
- Keep comments minimal and meaningful.

### Naming & Typing

- Follow PEP 8 conventions.
- Use descriptive names for classes, functions, and variables.
- Use explicit type annotations in public interfaces.
- Avoid unnecessary use of `Any`.
- Follow existing patterns for optional and nullable values.

### Documentation

- Write docstrings for public interfaces when their behavior is not obvious.
- Comments should explain *why*, not repeat *what* the code does.
- Keep comments concise.
- Update documentation when behavior or configuration changes.

### Shortcuts

If a justified shortcut introduces a known limitation, document it using:

`shortcut: <limitation>, <condition for improvement>`

Do not use shortcuts that weaken security, data integrity, or mandatory constitutional requirements.

## 10. Testing & Validation

Tests must cover the behavior introduced or modified by each task.

### Testing Rules

- Use Pytest.
- Prefer existing fixtures and test utilities.
- Keep tests deterministic and independent.
- Mock external HTTP calls in unit tests.
- Test important error and edge cases.
- Add regression tests for reproducible bugs when feasible.
- Do not depend on live websites during standard unit tests.
- Do not remove or weaken tests merely to make changes pass.

### Validation Commands

Run the following commands from the project root.

**Tests**

```bash
pytest -q
```

**Type checking**

```bash
mypy .
```

**Linting**

```bash
ruff check .
```

**Formatting verification**

```bash
ruff format --check .
```

Use project-defined alternatives if `pyproject.toml` specifies different commands or scopes.

### Execution Policy

- Run relevant tests after modifying behavior.
- Run `pytest -q` before completing a development task when the test environment is available.
- Run mypy and Ruff checks for affected Python code.
- Resolve failures caused by the current changes.
- Report unrelated or pre-existing failures separately.
- Do not modify unrelated code solely to make global checks pass without authorization.

If validation cannot run, explain why.

## 11. Scope Control & Prohibited Actions

AI agents must not:

- Modify unrelated files without justification.
- Implement unrequested features.
- Introduce dependencies without necessity.
- Add unused classes, modules, or configuration.
- Hardcode secrets or environment-specific credentials.
- Disable security or validation checks.
- Suppress exceptions without meaningful handling.
- Silently change API or data contracts.
- Perform destructive operations without authorization.
- Change existing architecture without a justified requirement.
- Claim validation success without execution.
- Apply superficial fixes that leave the root cause unresolved.

When a proposed change would violate the Constitution, stop and report the conflict.

## 12. Completion Criteria

A task is considered complete when:

- [ ] The requested behavior is implemented.
- [ ] Applicable acceptance criteria are satisfied.
- [ ] Changes follow the Constitution.
- [ ] Existing architecture and conventions are respected.
- [ ] Relevant tests are added or updated.
- [ ] Required validation checks pass, or limitations are reported.
- [ ] No unrelated modifications are introduced.
- [ ] Configuration and documentation are updated when necessary.
- [ ] Known limitations are disclosed.

## 13. Agent Response & Development History

After completing an implementation task, provide a concise technical summary.

### 13.1 Response Format

- **Changes:** What was implemented or corrected.
- **Files:** Files created, modified, or removed.
- **Validation:** Tests and checks executed, including their results.
- **Notes:** Relevant assumptions, unresolved issues, or limitations.

### 13.2 Persistent Development History

AI agents MUST maintain persistent development records for significant completed changes.

Store these records in:

`docs/changes/`

Each record MUST use the following naming convention:

`YYYY-MM-DD-short-description.md`

**Naming rules:**

- Use the completion date in `YYYY-MM-DD` format.
- Use lowercase letters.
- Separate words with hyphens (`kebab-case`).
- Describe the primary objective of the change.
- Prefer concise, meaningful names.
- Avoid generic names such as `update.md`, `changes.md`, or `fix.md`.
- If multiple changes share the same date and objective, append a numeric suffix such as `-02` to avoid overwriting existing records.
- Never overwrite an unrelated historical record.

**Examples:**

- `2026-10-28-implement-playwright-scraping.md`
- `2026-10-28-fix-pagination-extraction.md`
- `2026-10-29-add-api-authentication.md`
- `2026-10-30-refactor-browser-management.md`

### 13.3 Development Record Structure

Each record MUST contain:

```markdown
# Change: <Short Description>

**Date:** YYYY-MM-DD
**Type:** Feature | Bug Fix | Refactor | Improvement
**Status:** Completed | Partial

## Objective
Describe the problem or requirement addressed.

## Changes
Summarize the implementation and technical decisions.

## Affected Files
List created, modified, and removed files.

## Validation
Document executed tests and their results.

## Notes
Record relevant limitations, assumptions, or follow-up work.
```

### 13.4 Recording Rules

- Create a development record after implementing and attempting relevant validation.
- Record significant features, bug fixes, refactoring, and architectural changes.
- Do not create records for trivial edits or conversational interactions.
- Do not record credentials, tokens, secrets, or sensitive data.
- Document incomplete validation accurately.
- Keep records concise, factual, and technically relevant.
- Consult relevant historical records before modifying existing features.
- Do not modify historical records unless correcting factual inaccuracies.

### 13.5 Completion Requirements

Before concluding a significant development task, the agent MUST:

1. Review the implementation.
2. Execute relevant validation checks.
3. Create the development record in `docs/changes/`.
4. Verify that the filename follows the naming convention.
5. Include the development record path in the final response.

Do not claim that a record was saved unless it was successfully written to the repository.

---

**Core Directive:** Read the Constitution and applicable specifications, inspect existing code, implement the smallest correct change, validate the result, and report accurately.
