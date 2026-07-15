# Health Check

The application exposes two monitoring endpoints.

## Health

GET /health

Checks:

- Flask application
- PostgreSQL connectivity

Returns HTTP 200 if healthy.

---

## Readiness

GET /ready

Returns whether the application is ready to receive requests.

---

## Docker Healthcheck

Docker automatically checks:

http://localhost:5000/health

every 30 seconds.