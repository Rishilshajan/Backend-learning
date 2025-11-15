# Backend API — Endpoint Reference

Version: 1.0  
Purpose: Concise, professional reference for authentication, user, task, comment, dashboard, and health endpoints. This document is suited for engineers implementing the API, QA writing tests, or product reviewing behavior.

---

Table of contents
- Authentication Endpoints
- User Endpoints
- Task Endpoints
- Comment Endpoints
- Dashboard Endpoints
- Health & Utility Endpoints
- Common behaviors, errors & notes
- Roles & permissions
- Examples & next steps

---

## Conventions used in this document
- HTTP methods are shown as METHOD /path
- JSON schema fragments show expected request bodies (required fields bolded)
- Responses show typical status codes and brief descriptions
- All endpoints that require authentication assume a Bearer JWT access token in Authorization: Bearer <token>, unless otherwise noted.

---

## 1. Authentication Endpoints

### POST /auth/register
Register a new user.

Request body (application/json)
{
  "name": "string",       // required
  "email": "string",      // required, unique, valid email
  "password": "string"    // required, follow password policy
}

Responses
- 201 Created — user created (returns minimal user profile)
- 400 Bad Request — validation errors (e.g., missing fields, weak password)
- 409 Conflict — email already in use

Notes
- Passwords must be stored hashed (e.g., bcrypt, argon2).
- Consider sending email verification as a separate flow.

---

### POST /auth/login
Login and receive authentication tokens.

Request body (application/json)
{
  "email": "string",      // required
  "password": "string"    // required
}

Responses
- 200 OK — returns { "accessToken": "...", "refreshToken": "..." }
- 400 Bad Request — missing fields
- 401 Unauthorized — invalid credentials
- 403 Forbidden — account disabled/unverified (if applicable)

Notes
- Access token: short-lived JWT for API access.
- Refresh token: long-lived, stored & rotated server-side for refresh flow.

---

### POST /auth/refresh
Refresh JWT access token using a valid refresh token.

Request body (application/json)
{
  "refreshToken": "string" // required
}

Responses
- 200 OK — returns new { "accessToken": "...", "refreshToken": "..." } (rotate tokens)
- 401 Unauthorized — invalid or revoked refresh token
- 400 Bad Request — missing token

Notes
- Implement refresh token rotation and revocation on logout or suspected compromise.

---

### POST /auth/logout
Invalidate refresh token and end session.

Request body (application/json)
{
  "refreshToken": "string" // required
}

Responses
- 200 OK — refresh token invalidated
- 400 Bad Request — missing token
- 401 Unauthorized — token not recognized

Notes
- Remove or mark refresh token as revoked server-side.

---

## 2. User Endpoints

### GET /users/me
Get current authenticated user's profile.

Auth: required

Responses
- 200 OK — returns user profile
- 401 Unauthorized — missing/invalid access token

---

### GET /users/
Admin only: get list of users.

Query parameters (optional)
- page (int), limit (int), sort, q (search by name/email), role

Responses
- 200 OK — paginated list of users
- 401 Unauthorized — not authenticated
- 403 Forbidden — not admin

Notes
- Support pagination and filtering for large user sets.

---

### PATCH /users/:id
Admin: update user role or other admin-editable fields.

Request body (application/json)
{
  "role": "admin|manager|user",   // optional
  "name": "string",               // optional
  "email": "string"               // optional (validate uniqueness)
}

Auth: required — Admin only

Responses
- 200 OK — updated user returned
- 400 Bad Request — validation errors
- 401 Unauthorized — not authenticated
- 403 Forbidden — not admin
- 404 Not Found — user id not found

Notes
- Role changes may affect permissions and visibility; consider notification on role change.

---

## 3. Task Endpoints

Task model highlights (example)
{
  "id": "string",
  "title": "string",            // required
  "description": "string",
  "dueDate": "ISO8601 string",
  "priority": "low|medium|high",
  "assignedTo": "userId",
  "status": "todo|in-progress|done|archived",
  "deleted": false,             // soft-delete flag
  "createdAt": "timestamp",
  "updatedAt": "timestamp"
}

---

### POST /tasks
Create a new task.

Auth: required

Request body (application/json)
{
  "title": "string",              // required
  "description": "string",
  "dueDate": "ISO8601 string",
  "priority": "low|medium|high",
  "assignedTo": "userId"
}

Responses
- 201 Created — returns created task
- 400 Bad Request — validation errors
- 401 Unauthorized — not authenticated

Notes
- Validate assignedTo exists and is active.
- Default status = "todo".

---

### GET /tasks
List tasks with optional filters.

Auth: required

Query parameters
- status (todo|in-progress|done)
- assignedTo (userId)
- dueBefore, dueAfter (ISO dates)
- priority (low|medium|high)
- page, limit, sort

Responses
- 200 OK — paginated list of tasks
- 401 Unauthorized

Notes
- Exclude soft-deleted tasks by default.
- Support field selection or embed related user info if requested.

---

### GET /tasks/:id
Get a single task by id.

Auth: required

Responses
- 200 OK — task object
- 401 Unauthorized
- 403 Forbidden — if access restricted (e.g., private tasks)
- 404 Not Found — not found or soft-deleted

---

### PATCH /tasks/:id
Update task fields (partial update).

Auth: required; permission rules apply (owner, assignee, manager, admin)

Request body (application/json) — any subset of:
{
  "title": "string",
  "description": "string",
  "dueDate": "ISO8601 string",
  "priority": "low|medium|high",
  "assignedTo": "userId",
  "status": "todo|in-progress|done|archived"
}

Responses
- 200 OK — updated task
- 400 Bad Request — validation errors
- 401 Unauthorized
- 403 Forbidden — insufficient permissions
- 404 Not Found — task not found

Notes
- Consider audit trail for important changes (assignee, status, priority).

---

### DELETE /tasks/:id
Soft delete a task.

Auth: required; permission rules apply (owner, admin, manager)

Behavior
- Mark task.deleted = true and optionally store deletedAt and deletedBy.
- Do not physically remove from DB to allow recovery and auditing.

Responses
- 200 OK — deletion acknowledged
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found

Notes
- Provide endpoint to restore if required (e.g., POST /tasks/:id/restore).

---

## 4. Comment Endpoints

### POST /tasks/:id/comments
Add a comment to a task.

Auth: required

Request body (application/json)
{
  "text": "string"   // required
}

Responses
- 201 Created — created comment
- 400 Bad Request — missing text
- 401 Unauthorized
- 403 Forbidden — cannot comment on this task
- 404 Not Found — task not found or deleted

Notes
- Comment model should include authorId, createdAt, updatedAt. Consider support for attachments or mentions as later enhancements.

---

### GET /tasks/:id/comments
List comments for a task.

Auth: required

Query params
- page, limit, sort (default createdAt asc/desc)

Responses
- 200 OK — paginated list of comments
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found — task not found

Notes
- Exclude comments for soft-deleted tasks unless admin.

---

## 5. Dashboard Endpoints

### GET /dashboard/summary
Global summary (admin/manager role recommended).

Auth: required; roles: admin, manager (or permit per-product rules)

Response (200 OK) example
{
  "totalTasks": 123,
  "completed": 80,
  "overdue": 10,
  "dueSoon": 15   // e.g., due in next 3 days
}

Notes
- Keep calculations efficient; consider caching or pre-aggregations for large datasets.

---

### GET /dashboard/user/:id
Per-user summary: tasks assigned to a specific user.

Auth: required; permitted to user themselves or admins/managers.

Response (200 OK) example
{
  "userId": "123",
  "totalTasks": 30,
  "completed": 20,
  "overdue": 2,
  "dueSoon": 3
}

Notes
- Respect privacy and permissions; do not expose other sensitive info.

---

## 6. Health & Utility Endpoints

### GET /health
Check server status and dependent services.

Response (200 OK) example
{
  "status": "ok",
  "db": "connected",
  "cache": "ok",
  "uptime": "12345s"
}

Responses
- 200 OK — all systems nominal
- 503 Service Unavailable — if critical dependencies down

Notes
- Keep health endpoint unauthenticated for orchestration tools, but be mindful of sensitive data exposure.

---

### GET /version
Return service metadata: version & environment info.

Response (200 OK) example
{
  "version": "1.2.3",
  "commit": "abcdef123",
  "env": "production"
}

Notes
- Expose minimal info; avoid revealing secrets or detailed infra topology.

---

## Common behaviors, errors & notes

- Authentication: All protected endpoints expect Authorization: Bearer <accessToken>. Access tokens should be short-lived; refresh tokens should be stored & validated server-side.
- Error responses should follow a consistent schema, e.g.:
  {
    "error": "Bad Request",
    "message": "Field X is required",
    "code": "BAD_REQUEST",
    "details": { ... }
  }
- Validation: Return 400 with field-level messages on invalid input.
- 401: Unauthorized — token missing/invalid; 403: Forbidden — authenticated but insufficient permissions.
- 404: When resource does not exist or is soft-deleted and not visible to the caller.
- 500: Internal Server Error — unexpected failures; log detailed traces server-side and return generic messages to clients.
- Soft delete behavior (DELETE /tasks/:id): mark with deleted=true. Ensure list endpoints filter out deleted resources by default.

---

## Roles & Permissions (recommended baseline)
- admin
  - Full access: manage users, view all dashboards, override tasks, restore/delete permanently.
- manager
  - Manage tasks for teams, view broader dashboards, moderate comments.
- user
  - CRUD on own tasks, comment on tasks they have access to, view personal dashboard.

Enforce RBAC per endpoint. Document role-required checks in implementation.

---


- Add automated tests: unit tests for business logic and integration tests for endpoints (use a test DB).
- Define rate limits, CORS policy, and monitoring/alerting for the health endpoint.

---
