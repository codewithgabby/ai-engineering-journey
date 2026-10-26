# Authentication Fundamentals

## 1. Authentication vs Authorization

**Authentication** answers: Who is making this request?

**Authorization** answers: Is this user permitted to perform this action or access this resource?

A user can be authenticated successfully and still be denied access to a resource owned by another user or business.

## 2. Why backend enforcement matters

In a multi-tenant SaaS application, hiding another business's information in the frontend is insufficient. The backend must verify permissions before returning or modifying protected data.

For example, a valid user belonging to Business B must not automatically be able to access Business A's sales reports.

## 3. Access tokens

After successful login, an application may issue an access token. The client presents the token on subsequent requests, commonly through the HTTP `Authorization` header using the Bearer scheme.

Tokens are credentials and must be protected. Access tokens commonly expire after a limited period. The backend must validate a token rather than trusting its presence alone.

## 4. Password storage

Never store plaintext passwords in the database. Store password hashes produced by a suitable password-hashing algorithm, such as Argon2, using an appropriate library and configuration.

During login, verify the submitted password against the stored hash. Do not decrypt a stored password; password hashes are designed for verification rather than recovery.

## 5. FastAPI dependencies

FastAPI dependencies allow shared logic to run before an endpoint's main function. A reusable authentication dependency can validate credentials and provide the current user to protected endpoints.

This reduces duplicated code while keeping security checks consistent.

## 6. Planned request flow

1. The user submits login credentials.
2. The backend finds the account and verifies the password.
3. The backend issues an access token.
4. The client presents the token on later requests.
5. The backend validates the token and identifies the user.
6. Authorization checks determine whether the user may access the requested resource.
7. The API returns permitted data or rejects the request.

## 7. Implementation status

These concepts have been introduced, but no authentication code has been implemented yet.

### Next practical task
Inspect the existing Alembic configuration and migration history before creating the User model. Then implement registration, secure password hashing, login, token validation, and protected endpoints in stages.

**Engineering principle:** Authentication establishes identity; authorization enforces boundaries.