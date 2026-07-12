# Employee Management System

A Flask-based Employee Management System built as part of a DevOps learning journey.

---

## Project Overview

This project demonstrates how to:

- Build a Flask web application
- Containerize applications using Docker
- Manage Docker images and containers
- Persist data using Docker Volumes
- Configure Docker Networks
- Apply Docker security best practices
- Follow professional Git workflows
- Prepare applications for Docker Compose and Kubernetes

---

## Tech Stack

| Technology | Version |
|------------|----------|
| Python | 3.12 |
| Flask | Latest |
| SQLite | Built-in |
| Docker | Latest |
| Git | Latest |

---

## Features

- Employee Login
- Employee Dashboard
- Employee CRUD Operations
- Logging
- Environment Configuration
- Docker Support
- Persistent Database
- Professional Git Workflow

---

## Project Architecture

```text
Browser
    │
    ▼
Flask Application
    │
    ▼
SQLite Database

Containerized Using Docker
```

---

## Docker Architecture

```text
Browser
      │
      ▼
+-------------------------+
| Docker Container        |
|                         |
| Flask Application       |
|                         |
| SQLite Database         |
+-------------------------+
          │
          ▼
Docker Volume
```

---

## Folder Structure

```text
app.py
config.py
routes/
templates/
static/
database/
logs/
docs/
screenshots/
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/employee-management-system.git
```

```bash
cd employee-management-system
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

Open

```
http://localhost:5000
```

---

# Docker Commands

## Build Docker Image

```bash
docker build -t employee-management-system:v1 .
```

---

## List Images

```bash
docker images
```

---

## Run Container

```bash
docker run -d --name employee-app -p 5000:5000 employee-management-system:v1
```

---

## View Running Containers

```bash
docker ps
```

---

## View All Containers

```bash
docker ps -a
```

---

## View Logs

```bash
docker logs employee-app
```

---

## Stop Container

```bash
docker stop employee-app
```

---

## Start Container

```bash
docker start employee-app
```

---

## Restart Container

```bash
docker restart employee-app
```

---

## Remove Container

```bash
docker rm employee-app
```

---

## Remove Image

```bash
docker image rm employee-management-system:v1
```

---

## Create Docker Volume

```bash
docker volume create employee-db
```

---

## List Volumes

```bash
docker volume ls
```

---

## Inspect Volume

```bash
docker volume inspect employee-db
```

---

## Run with Persistent Storage

```bash
docker run -d \
--name employee-app \
-p 5000:5000 \
-v employee-db:/app/database \
employee-management-system:v1
```

---

## Create Docker Network

```bash
docker network create employee-network
```

---

## List Networks

```bash
docker network ls
```

---

## Inspect Network

```bash
docker network inspect employee-network
```

---

## Run Container on Custom Network

```bash
docker run -d \
--name employee-app \
--network employee-network \
-p 5000:5000 \
-v employee-db:/app/database \
employee-management-system:v1
```

---

## Enter Running Container

```bash
docker exec -it employee-app bash
```

---

## Build Optimized Image

```bash
docker build -t employee-management-system:v2 .
```

---

## Run Production Image

```bash
docker run -d \
--restart unless-stopped \
--name employee-app-v2 \
-p 5000:5000 \
employee-management-system:v2
```

---

## Inspect Image

```bash
docker image inspect employee-management-system:v2
```

---

## Image History

```bash
docker history employee-management-system:v2
```

---

###  Security and Best Practice
```bash
docker run -d --restart unless-stopped --name employee-app-v3 -p 5002:5000 --memory="512m" --cpus="1.0" employee-management-system:v3
```

---

# Git Workflow

Create Feature Branch

```bash
git checkout -b feature/docker
```

Stage Changes

```bash
git add .
```

Commit

```bash
git commit -m "Meaningful commit message"
```

Push

```bash
git push -u origin feature/docker
```

Merge

```bash
git checkout main
git pull origin main
git merge feature/docker
git push origin main
```

Create Tag

```bash
git tag -a v2.0.0 -m "Dockerized Employee Management System"
```

Push Tag

```bash
git push origin v2.0.0
```

---

## Future Enhancements

- Docker Compose
- PostgreSQL
- Redis
- Nginx Reverse Proxy
- GitHub Actions CI/CD
- Kubernetes Deployment
- Helm Charts
- Monitoring using Prometheus & Grafana

---

## Screenshots

(Add screenshots here as your UI evolves.)

---

## Author

Saish Rane

DevOps Engineer | Infrastructure Automation | Python | Docker | Kubernetes