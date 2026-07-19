# Gunicorn

The application uses Gunicorn as the production WSGI server.

## Why Gunicorn?

- Production-ready
- Multiple worker processes
- Better performance than Flask's development server
- Compatible with reverse proxies such as Nginx

## Local Run

```bash
gunicorn --bind 0.0.0.0:5000 app:app
```

## Docker

Gunicorn is started automatically by the Docker container.