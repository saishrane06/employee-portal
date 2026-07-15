# Sprint 4 Summary

## Features Added

- PostgreSQL Integration
- Docker Compose
- Health Endpoint
- Readiness Endpoint
- Automatic Database Initialization
- Production Logging
- Environment Variable Validation
- Custom Error Pages

## Docker Commands

Build

```bash
docker compose build
```

Run

```bash
docker compose up -d
```

Logs

```bash
docker compose logs -f
```

Stop

```bash
docker compose down
```

Remove Volumes

```bash
docker compose down -v
```

Health

```
GET /health
```

Readiness

```
GET /ready
```