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