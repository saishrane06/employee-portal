# Docker Hub

Docker images are published using semantic versioning.

## Login

```bash
docker login
```

## Build

```bash
docker compose build
```

## Tag

```bash
docker tag employee-portal-employee-app:latest <dockerhub-username>/employee-portal:v1.0
```

## Push

```bash
docker push <dockerhub-username>/employee-portal:v1.0
```

## Pull

```bash
docker pull <dockerhub-username>/employee-portal:v1.0
```