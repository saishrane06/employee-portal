# Logging

The application writes all logs to standard output.

## Why?

Containerized applications should not write logs to local files.

Docker automatically captures stdout/stderr.

## Useful Commands

View logs:

```bash
docker compose logs employee-app
```

Follow logs:

```bash
docker compose logs -f employee-app
```

View PostgreSQL logs:

```bash
docker compose logs postgres-db
```

View all logs:

```bash
docker compose logs
```