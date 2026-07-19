# Nginx Reverse Proxy

The application uses Nginx as a reverse proxy in front of Gunicorn.

## Architecture

Browser
→ Nginx
→ Gunicorn
→ Flask
→ PostgreSQL

## Why Nginx?

- Reverse proxy
- Better performance
- Static file serving
- SSL/TLS support (future)
- Load balancing (future)

## Commands

Start:

```bash
docker compose up
```

View logs:

```bash
docker compose logs nginx
```