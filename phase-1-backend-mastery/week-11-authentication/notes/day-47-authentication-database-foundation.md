# Day 47 — Authentication Database Foundation

## 1. What I learned

Authentication needs a reliable database foundation for storing user account information. Today, I prepared that foundation in the existing FastAPI and PostgreSQL project.

## 2. Alembic and model discovery

Alembic manages database schema changes through migration scripts.

SQLAlchemy models inherit from a shared `Base`. Their table definitions are collected in `Base.metadata` when the model modules are loaded.

Alembic uses this metadata during autogeneration to compare the application's expected schema with the existing database schema.

**Engineering lesson:** A model must be imported into the migration environment so Alembic can discover its table.

## 3. The User model

The new `User` model contains:

- `id`: primary key.
- `email`: required email identifier with a unique index.
- `password_hash`: required field intended to store a password hash.

Passwords must never be stored in plaintext. Password hashing will be implemented as part of the registration workflow.

## 4. Migration workflow

Today's workflow was:

1. Inspect `alembic/env.py` and the existing products migration.
2. Create `app/models/user.py`.
3. Register the User model with Alembic.
4. Generate the migration using `alembic revision --autogenerate`.
5. Inspect the generated migration.
6. Apply it using `alembic upgrade head`.
7. Verify the resulting PostgreSQL schema.

The new migration revision is `9f5baf31b3aa`, following the existing products migration `9a2c17379f01`.

## 5. Verification results

The database inspection confirmed:

- The `users` and `products` tables exist.
- The User model's `id`, `email`, and `password_hash` columns are present and non-nullable.
- The `ix_users_email` index exists and is unique.
- Alembic's current revision matches the new migration head.

## 6. Engineering insight

Generating a migration and applying it are separate operations. Reviewing a migration before applying it helps prevent unintended schema changes.

Database verification provides stronger evidence than relying on a command's success message alone.

## 7. Implementation status

**Completed:** User model, Alembic migration, migration application, and direct schema verification.

**Not yet implemented:** Password hashing, user registration, login, token issuance, token validation, and protected endpoints.

## 8. Next session

Begin secure user registration:

1. Inspect the installed password-hashing and validation dependencies.
2. Choose and configure an appropriate password-hashing library.
3. Create the registration request schema.
4. Implement repository and service logic.
5. Connect the registration router.
6. Verify registration manually through Swagger, including duplicate-email and invalid-input cases.