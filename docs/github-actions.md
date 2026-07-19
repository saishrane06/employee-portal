# GitHub Actions

The CI pipeline runs automatically on every push and pull request.

## Pipeline Steps

1. Checkout Repository
2. Setup Python
3. Install Dependencies
4. Run Pytest
5. Run Flake8
6. Build Docker Image
7. Push Docker Image

## Workflow File

.github/workflows/ci.yml