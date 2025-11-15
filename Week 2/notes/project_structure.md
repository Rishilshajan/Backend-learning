# TaskFlow Backend — Architecture & Developer Guide

Version: 1.0  
Last updated: 2025-11-15  
Maintainer: TaskFlow Backend team (Rishilshajan)

---

## 1. Overview

TaskFlow Backend is a Node.js + TypeScript service that provides authentication, task management, role-based access, dashboards and workflow support for the TaskFlow productivity application.

Core architectural principles
- Layered, modular design: Route → Controller → Service → Repository → Database
- Separation of concerns and domain-driven design (DDD) concepts
- Small expressive modules with well-defined responsibilities
- Testable units and clear boundaries between business logic and transport

Purpose of this document
- Provide a concise reference for contributors and reviewers
- Describe folder layout, responsibilities of layers, technology choices and the development workflow
- Give practical checklists and conventions for adding endpoints and features

---

## 2. High-level folder structure

Recommended project layout:

backend/
├─ package.json  
├─ tsconfig.json  
├─ prisma/  
│  └─ schema.prisma  
├─ src/  
│  ├─ server.ts           # bootstrapping (listen, load env, metrics)  
│  ├─ app.ts              # express app, middleware, routes mounting  
│  ├─ routes/             # route definitions -> controllers  
│  ├─ controllers/        # HTTP handlers: map req -> service call -> res  
│  ├─ services/           # business logic, orchestration, rules  
│  ├─ repositories/       # DB queries using Prisma (one repo per model)  
│  ├─ validation/         # request schemas (Zod/Joi) + validators  
│  ├─ middleware/         # auth, validation, error handlers, logging  
│  ├─ models/             # TS domain models & DTOs (TaskModel, UserModel)  
│  ├─ utils/              # helpers (logger, paginate, date utils)  
│  ├─ config/             # env loading, typed config, feature flags  
│  ├─ tests/              # unit & integration tests (jest/ts-node/ava)  
│  └─ types/              # shared TS types & interfaces

Tip: Keep each directory focused; aim for files < 300 lines where possible.

---

## 3. Layer Responsibilities (concise)

- Routes
  - Define HTTP paths, methods and attach middleware
  - Lightweight; route files should import controller handlers only

- Controllers
  - Extract validated input from req, call appropriate service, handle response formatting + HTTP status codes
  - No business logic; only translate transport <-> domain

- Services
  - Implement business rules, orchestration across repositories and external services
  - Permission checks, state transitions, validation beyond schema-level
  - Return domain objects (or throw domain-specific errors)

- Repositories
  - Encapsulate database access (Prisma client calls)
  - One repository per aggregate/entity
  - Keep SQL/ORM logic centralized for easier testing/mocking

- Validation
  - Zod/Joi schemas for incoming request bodies, params and queries
  - Validation middleware to short-circuit invalid requests before controllers

- Middleware
  - Cross-cutting concerns: auth (JWT), validation runner, global error handler, request logging, rate limiting
  - Compose middleware in app.ts in a consistent order:
    - Request logging → Auth (if required) → Validation → Controller → Error handler

- Utils
  - Pure helpers: logger wrapper (winston/pino), pagination helpers, date formatting, small deterministic utilities

- Models
  - TypeScript domain models, DTOs and mapping helpers between DB shapes and API shapes

- Config
  - Typed config built from environment variables, with sensible defaults and runtime validation

- Tests
  - Unit tests for services and repositories
  - Integration tests for controllers (spin a test DB or use transaction rollback)
  - End-to-end tests can run against a test environment

---

## 4. Technology choices & rationale

- Node.js + TypeScript — type safety, modern ecosystem
- Express.js — simple, battle-tested HTTP framework (or Fastify if performance is a priority)
- PostgreSQL — relational data model for tasks/users/relations
- Prisma ORM — typed DB client & schema-first workflow
- JWT Authentication — stateless access tokens + refresh token flow
- Zod or Joi — schema-based validation at the edge
- Winston or Pino — structured logging and log levels
- Jest / Vitest — unit tests; supertest for controller integration
- Docker for local development & reproducible CI images

Security patterns
- Hash passwords with bcrypt/argon2
- Short-lived access tokens, refresh token rotation & revocation
- RBAC (admin/manager/user) enforced in services or via middleware guards
- Rate limiting and CORS configured per environment

---

## 6. Authentication & Authorization

Authentication
- Login returns { accessToken, refreshToken }.
- Access token: short-lived JWT used in Authorization header.
- Refresh token: long-lived, stored in DB or token store for revocation and rotation.

Authorization
- Role-based access control (RBAC) with roles: admin, manager, user.
- Enforce coarse checks in middleware (e.g., requireRole('admin')) and fine-grained checks in services (resource ownership).

Token flow recommendations
- Rotate refresh tokens on use and mark previous refresh token as revoked.
- On logout, mark refresh token revoked and optionally blacklist access until expiry.

---

## 7. Validation & Error Handling

Validation
- Use Zod/Joi schemas per endpoint (body, params, query).
- Central validation middleware returns consistent 400 responses with field-level errors.

Error handling
- Define domain error types (ValidationError, NotFoundError, ForbiddenError, ConflictError, ServerError).
- Global error handler maps domain errors to HTTP codes and a consistent error response:
- Log stack traces server-side; return safe messages to clients.

---

## 8. Development workflow (step-by-step)

When implementing a new endpoint or feature:

1. Define the API (blueprint/OpenAPI): path, method, request/response schemas, auth & roles.
2. Add Zod/Joi validation schema in `src/validation/`.
3. Add route in `src/routes/` and wire to controller.
4. Implement controller in `src/controllers/` (map req -> call service -> res).
5. Implement service logic in `src/services/` (permission checks, orchestration).
6. Implement repository functions in `src/repositories/` for DB access (Prisma).
7. Add/update Prisma schema and migrations if DB model changed.
8. Add unit tests for service + repository and integration tests for controller endpoint.
9. Run linting, type-check and tests locally.
10. Update API docs (OpenAPI/Swagger) and Postman collection.
11. Submit PR with a clear description and testing notes.

Checklist for PRs
- [ ] Typesafe changes (tsc)
- [ ] Lint passes (eslint/prettier)
- [ ] Unit tests added and passing
- [ ] Integration tests for controller (supertest)
- [ ] Database migrations included (if applicable)
- [ ] API docs updated

---

## 9. Conventions & patterns

- Naming
  - files: kebab-case (e.g., tasks.service.ts)
  - classes: PascalCase
  - functions/consts: camelCase
- Error handling
  - Throw domain errors in services; controllers only map to responses
- Transactions
  - Use transactions in repository layer when multiple related writes must be atomic
- Pagination
  - Use cursor or page/limit consistently; include totalCount when useful
- Soft-delete
  - Use a soft-delete flag + deletedAt for recoverability and auditing

---

## 11. Testing strategy

- Unit tests: services, utils (fast, no DB)
- Repository tests: run against ephemeral test DB or use Prisma transactions to rollback
- Controller integration tests: supertest against test server with DB prepared per test
- CI pipeline: run lint, typecheck, tests, and build; run migrations only on release pipeline

---

## 12. Observability & ops

- Structured logs (JSON) with request id and user id when available
- Metrics: request counts, latencies, error rates (Prometheus + Grafana)
- Health endpoints:
  - GET /health → service + DB status
  - GET /version → build metadata
- Alerts on high error rate, DB connection failures, or high latency

---

## 13. Recommended next steps

- Create an OpenAPI (v3) specification for all endpoints; auto-generate a Postman collection and client SDKs as needed.
- Add CI pipeline with lint, typecheck, tests and build steps.
- Add a test orchestration script for local development (start DB, run migrations, seed).
- Document role & permission matrix for each endpoint.

---
