# Configuration

The application supports multiple environments.

## Available Configurations

| Environment | Purpose |
|-------------|---------|
| development | Local Development |
| docker | Docker Containers |
| testing | GitHub Actions |
| production | Production Deployment |

## Environment Variable

```env
FLASK_CONFIG=development
```

## Database Variables

- DB_HOST
- DB_PORT
- DB_NAME
- DB_USER
- DB_PASSWORD