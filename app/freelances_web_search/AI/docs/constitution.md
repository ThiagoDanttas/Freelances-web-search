# Python & FastAPI Project Constitution

**Version:** 1.0.0
**Ratified:** 2026-10-27
**Last Amended:** 2026-10-27

## Core Principles

### I. Clean Architecture & Modularity

The application MUST follow a modular architecture with clearly separated responsibilities.

- **Routers:** Handle HTTP requests, input validation, dependency injection, and response formatting.
- **Services:** Implement business logic and orchestrate application operations.
- **Repositories:** Encapsulate database access and persistence operations.
- **Models:** Represent domain and persistence entities.
- **Schemas:** Define request, response, and validation contracts using Pydantic.
- **Core:** Contain configuration, security, exceptions, and shared infrastructure.

Mandatory rules:

- Routers MUST NOT contain business logic.
- Services MUST NOT depend on FastAPI request or response objects.
- Database queries MUST NOT be implemented directly in routers.
- Dependencies MUST be injected rather than instantiated throughout the codebase.
- Modules MUST have a single, clearly defined responsibility.
- Circular imports MUST be avoided.
- Existing architecture conventions MUST be respected.

**Rationale:** Separation of concerns improves maintainability, testing, and extensibility.

### II. Python Standards & Code Quality

All Python code MUST follow modern Python engineering practices.

- Python 3.12+ MUST be used unless explicitly constrained by project requirements.
- Public functions and methods MUST include type annotations.
- PEP 8 naming and formatting conventions MUST be followed.
- Ruff MUST be used for linting and formatting.
- A type checker such as mypy MUST be configured.
- `Any` SHOULD be avoided unless justified.
- Mutable default arguments MUST NOT be used.
- Broad exception handling MUST NOT silently suppress errors.
- Functions SHOULD remain small and focused.
- Code MUST be self-explanatory, with comments explaining non-obvious decisions.
- Unused imports, dead code, and debugging statements MUST NOT be committed.
- Public interfaces SHOULD include meaningful docstrings.


Code SHOULD favor clarity over cleverness.

### III. FastAPI Best Practices

All API endpoints MUST follow consistent FastAPI conventions.

- Endpoints MUST use `APIRouter`.
- Request and response bodies MUST use explicit Pydantic models.
- Endpoints MUST declare appropriate HTTP methods and status codes.
- Dependencies MUST use FastAPI's `Depends` or `Security` mechanisms.
- Routers MUST remain thin.
- API exceptions MUST use centralized handling where appropriate.
- Public API contracts MUST be reflected accurately in OpenAPI.
- Long-running operations MUST NOT block the event loop.
- Synchronous blocking operations MUST NOT run directly inside asynchronous endpoints.
- Async operations MUST be used when supported by the underlying libraries and when beneficial.

**Rationale:** Consistent endpoint design ensures predictable behavior and reliable API documentation.

### IV. Data Validation & Type Safety

All external data MUST be considered untrusted.

- Incoming request data MUST be validated using Pydantic.
- Responses MUST use explicit response schemas.
- Database entities MUST NOT be exposed directly when they contain internal fields.
- Input constraints MUST be expressed declaratively whenever possible.
- Validation MUST occur at application boundaries.
- Business invariants MUST be enforced in the domain or service layer.
- Serialization MUST be deterministic and consistent.
- Optional fields MUST explicitly declare nullability.
- Date and time values MUST use timezone-aware representations when they represent instants.

**Rationale:** Explicit contracts prevent invalid states, accidental data exposure, and inconsistent integration behavior.

### V. Security by Default

Security MUST be implemented from the beginning.

- Protected endpoints MUST enforce authentication.
- Resource access MUST enforce authorization, not merely authentication.
- Passwords MUST use secure password hashing algorithms such as Argon2id.
- Secrets MUST be loaded through environment variables or a secrets manager.
- Credentials MUST NOT be stored in source code.
- Sensitive information MUST NOT be included in logs or API error responses.
- CORS MUST use an explicit list of allowed origins appropriate to the environment.
- JWT tokens, when used, MUST validate signatures, expiration, allowed algorithms, and applicable claims.
- OAuth2 or OpenID Connect SHOULD be used when appropriate.
- SQL queries MUST use parameterized statements or safe ORM queries.
- File uploads MUST validate size, type, and permitted content.
- External requests MUST use explicit timeouts.
- Rate limiting SHOULD be applied to abuse-sensitive endpoints.
- Multi-tenant applications MUST enforce tenant isolation in data access and authorization.

**Rationale:** APIs frequently expose sensitive operations and must resist unauthorized access and common attack vectors.

### VI. Database & Persistence

Database access MUST follow consistent persistence patterns.

- SQLAlchemy 2.x SHOULD be used when relational persistence is required.
- PostgreSQL SHOULD be the default production relational database.
- Database access MUST be isolated from routers.
- Database sessions MUST have clearly defined lifecycles.
- Transactions MUST be used for operations requiring atomicity.
- Related writes MUST NOT be partially committed.
- Queries MUST avoid unnecessary database round trips.
- Pagination MUST be implemented for potentially large collections.
- Database indexes SHOULD be introduced based on query patterns and performance evidence.
- Destructive migrations MUST be explicitly reviewed.
- Schema changes MUST NOT rely on automatic table creation in production.

**Rationale:** Consistent persistence management protects data integrity and supports long-term maintainability.

### VII. Error Handling & Observability

Errors MUST be predictable, traceable, and safe.

- Domain-specific exceptions SHOULD be used for expected business failures.
- Exception handlers MUST translate known failures into appropriate HTTP responses.
- Internal exceptions MUST NOT expose stack traces to API consumers.
- Unexpected errors MUST be logged with sufficient diagnostic context.
- Structured logging (From Loguru library) SHOULD be used.
- Request correlation identifiers SHOULD be supported.
- Secrets, access tokens, and sensitive payloads MUST NOT be logged.
- Health endpoints SHOULD be available for deployed services.
- External integrations MUST define timeout and failure behavior.
- Retries MUST be bounded and limited to operations that are safe to retry.
- Errors MUST NOT be silently ignored.

**Rationale:** Operational visibility is essential for diagnosing failures and maintaining reliable services.

### VIII. Automated Testing

All business-critical functionality MUST be covered by automated tests.

- Pytest MUST be used as the primary test framework.
- Service-layer business logic MUST have unit tests.
- API endpoints MUST have integration tests for important success and failure cases.
- Authentication and authorization logic MUST be tested.
- Validation errors MUST be tested.
- Database operations MUST be tested against an isolated test environment.
- External APIs SHOULD be mocked or replaced with test doubles in unit tests.
- Async tests MUST use compatible tooling such as pytest-asyncio or AnyIO.
- Regression tests MUST be added for reproducible defects when feasible.
- Tests MUST be deterministic and independent.
- Required tests MUST pass before merging changes.

**Rationale:** Automated tests enable confident refactoring and reduce regressions in production APIs.

### IX. Performance & Async Execution

The application MUST manage execution resources appropriately.

- Async endpoints MUST NOT perform blocking I/O on the event loop.
- CPU-intensive operations SHOULD execute outside the event loop, using suitable workers or process-based execution.
- Database connections MUST be managed through controlled pooling.
- Large responses SHOULD support pagination or streaming when appropriate.
- Expensive operations SHOULD be measured before introducing optimization.
- Caching SHOULD be introduced only when justified by requirements or measurements.
- Background processing MUST have defined failure and retry behavior.
- FastAPI `BackgroundTasks` MUST NOT be treated as a durable job queue for critical workloads.
- External HTTP clients SHOULD reuse connections when appropriate.

**Rationale:** Efficient resource management supports API responsiveness and reliable execution under load.

### X. Configuration & Environment Management

Application configuration MUST be explicit and environment-independent.

- Configuration MUST be centralized, preferably using `pydantic-settings`.
- Environment variables MUST control environment-specific values.
- Required configuration MUST be validated at startup.
- Secrets MUST NOT have insecure production defaults.
- Development, staging, and production MUST use separately managed configuration and credentials.
- Dependency versions MUST be managed through a reproducible dependency-locking strategy.
- `.env` files containing secrets MUST NOT be committed.
- An `.env.example` SHOULD document required configuration keys without actual secrets.
- Docker images SHOULD run as non-root users wherever feasible.

**Rationale:** Reproducible environments reduce deployment failures and configuration-related security risks.

## Project Structure

The recommended starting structure is:

```text
project/
├── .specify/
│   └── memory/
│       └── constitution.md
│
├── app/
|   ├── freelances_web_search/
│       ├── api/
│   │       ├── dependencies.py
│   │       └── v1/
│   │           ├── router.py
│   │           └── endpoints/
│       ├── core/
│   │       ├── config.py
│   │       ├── security.py
│   │       ├── exceptions.py
│   │       └── setup_log.py
|       ├── log/

│       ├── models/
│       ├── schemas/
│       ├── services/
│       ├── repositories/
│       ├── db/
│       |    ├── session.py
│       │    └── base.py
│            └── integrations/
│
        ├── tests/
│       ├── unit/
│       ├── integration/
│       └── conftest.py
│
├── pyproject.toml
├── .env
├── .env.example
└── README.md
```

This structure is a default, not a requirement to create unused folders. Feature-based organization MAY be adopted when it better suits the project.

## AI Coding Agent Rules

AI agents MUST respect the following rules when working on the repository.

### Before Implementation

1. Read this Constitution.
2. Inspect the existing repository structure.
3. Identify established coding and architectural patterns.
4. Review relevant interfaces, schemas, and tests.
5. Confirm that the implementation matches the approved specification.
6. Identify security, data integrity, and compatibility risks.

### During Implementation

1. Follow existing project conventions.
2. Keep changes limited to the approved feature.
3. Prefer existing services and utilities over duplication.
4. Use typed functions and explicit schemas.
5. Keep routers thin and business logic in services.
6. Implement meaningful error handling.
7. Add relevant automated tests.
8. Avoid unnecessary dependencies and abstractions.
9. Keep important or environment-specific variables in `.env`; load them with `python-dotenv` and access them through a configuration module or `os.getenv`. 

### Prohibited Actions

AI agents MUST NOT:

- Never hardcode secrets, URLs, credentials, API keys, or values likely to change.
- Invent database fields or external API contracts.
- Remove security checks to simplify implementation.
- Modify unrelated functionality without justification.
- Disable tests to hide implementation failures.
- Introduce unapproved breaking API changes.
- Create unnecessary architectural layers.
- Claim that unexecuted tests have passed.
- Replace existing libraries without technical justification.
- Perform destructive database operations without explicit authorization.


### After Implementation

AI agents MUST:

1. Run Ruff checks.
2. Run configured type checks.
3. Run relevant Pytest suites.
4. Verify API contracts and response schemas.
5. Review security-sensitive changes.
6. Report modified files and implementation outcomes.
7. Clearly state any unverified assumptions or incomplete checks.

## Definition of Done

A feature is complete only when:

- [ ] Functional requirements are satisfied.
- [ ] Constitution principles are respected.
- [ ] Endpoints use appropriate schemas and status codes.
- [ ] Business logic is separated from HTTP handling.
- [ ] Authentication and authorization are implemented where required.
- [ ] Relevant automated tests pass.
- [ ] Ruff and configured type checks pass.
- [ ] Database migrations are included when applicable.
- [ ] Configuration changes are documented.
- [ ] No secrets or sensitive information are exposed.
- [ ] Relevant documentation is updated.

## Governance

This Constitution takes precedence over conflicting feature-level implementation instructions.

### Amendments

- Amendments MUST document the rationale for change.
- Changes MUST be approved by the project maintainer.
- Changes MUST be reflected in relevant templates and engineering documentation.
- Security-related exceptions MUST document risks and mitigating controls.

### Versioning

- **MAJOR:** Removal or incompatible redefinition of existing principles.
- **MINOR:** Addition of principles or material expansion of requirements.
- **PATCH:** Clarifications without substantive changes.

### Compliance

All specifications, implementation plans, and pull requests MUST be reviewed against applicable constitutional principles.

Exceptions require explicit documentation and approval.

**Constitution Version:** 1.0.0
**Last Updated:** 2026-10-27
