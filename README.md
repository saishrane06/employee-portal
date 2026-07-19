# Employee Management System

A production-style Employee Management System built with Flask while following Agile development practices, Git workflows, and DevOps principles.

---

## Features

### Authentication
- Login
- Logout
- Session Management
- Password Hashing

### Employee Management
- View Employees
- Add Employee
- Edit Employee
- Delete Employee
- Search Employee

### Other Features
- Flash Messages
- Logging
- SQLite Database
- MVC Architecture
- Blueprints

---

## Tech Stack

| Technology | Version |
|------------|----------|
| Python | 3.x |
| Flask | Latest |
| SQLite | Built-in |
| HTML5 | ✓ |
| CSS3 | ✓ |
| Jinja2 | ✓ |
| Git | ✓ |

---

## Project Architecture

(Add architecture image here)

---

## Folder Structure

(Add folder tree)

---

## Screenshots

### Dashboard

(Add Screenshot)

### Employee List

(Add Screenshot)

### Add Employee

(Add Screenshot)

### Edit Employee

(Add Screenshot)

### Search Employee

(Add Screenshot)

---

## Releases

v1.1.0

Authentication Module

v1.2.0

Employee CRUD Module

---

## Upcoming Features

- Docker
- Docker Compose
- Jenkins
- GitHub Actions
- Kubernetes
- Terraform
- Prometheus
- Grafana

## Database Initialization

The PostgreSQL database is automatically initialized when the containers are started for the first time.

Initialization scripts:

- `database/init.sql` → Creates tables
- `database/seed.sql` → Creates the default administrator

Default credentials:

Username: admin

Password: Admin@123

## Health Monitoring

The application exposes production-style monitoring endpoints.

| Endpoint | Purpose |
|----------|---------|
| /health | Application + Database health |
| /ready | Readiness probe |

Docker uses `/health` for automatic container health monitoring.

## Logging

The application uses structured logging and writes logs to standard output.

Logs can be viewed using:

```bash
docker compose logs -f employee-app
```

# Sprint 4 Features

- Docker Compose
- PostgreSQL
- Automatic Database Initialization
- Docker Volumes
- Health Checks
- Readiness Endpoint
- Production Logging
- Environment Validation
- Custom Error Pages

## Project Architecture

Browser

↓

Flask

↓

PostgreSQL

↓

Docker Compose

↓

Persistent Volume

## Docker Image

```bash
docker pull <dockerhub-username>/employee-portal:latest
```

## Features

- User Authentication
- Employee CRUD Operations
- Employee Search
- PostgreSQL Database
- Dockerized Application
- Docker Compose Deployment
- GitHub Actions CI Pipeline
- Docker Hub Image Publishing
- Flake8 Code Linting
- Automated Testing with Pytest
- Multi-Environment Configuration
- Health Check Endpoint
- Logging

## Technology Stack

| Category | Technology |
|----------|------------|
| Backend | Flask |
| Database | PostgreSQL |
| ORM/Driver | psycopg2 |
| Authentication | Werkzeug Security |
| Containerization | Docker |
| Container Orchestration | Docker Compose |
| CI/CD | GitHub Actions |
| Image Registry | Docker Hub |
| Testing | Pytest |
| Linting | Flake8 |
| Environment Management | python-dotenv |

## CI/CD Pipeline

Every push or pull request automatically performs:

1. Install Dependencies
2. Run Pytest
3. Run Flake8
4. Build Docker Image
5. Push Docker Image to Docker Hub

## Docker Commands

### Build

```bash
docker compose build
```

### Start

```bash
docker compose up
```

### Start in Background

```bash
docker compose up -d
```

### Stop

```bash
docker compose down
```

### Stop and Remove Volumes

```bash
docker compose down -v
```

### View Logs

```bash
docker compose logs

docker compose logs employee-app

docker compose logs postgres-db
```

### Restart

```bash
docker compose restart
```

### Rebuild

```bash
docker compose up --build
```

### List Containers

```bash
docker ps
```

### List Images

```bash
docker images
```

### Remove Unused Images

```bash
docker image prune
```

## Production Stack

- Flask
- Gunicorn
- PostgreSQL
- Docker
- Docker Compose
- GitHub Actions


## Project Progress

| Sprint | Status |
|---------|--------|
| Sprint 1 - Flask Basics | ✅ Completed |
| Sprint 2 - Employee Management | ✅ Completed |
| Sprint 3 - Docker | ✅ Completed |
| Sprint 4 - PostgreSQL | ✅ Completed |
| Sprint 5 - CI/CD | ✅ Completed |
| Sprint 6 - Production Deployment | 🚧 In Progress |

## Production Architecture

```text
Browser
    │
    ▼
Nginx
    │
    ▼
Gunicorn
    │
    ▼
Flask
    │
    ▼
PostgreSQL
```

## Static File Handling

Static assets are served directly by Nginx.

Benefits:

- Faster page loads
- Browser caching
- Reduced application server load