# -------------------------------
# Base Image
# -------------------------------
FROM python:3.12-slim

# -------------------------------
# Metadata
# -------------------------------
LABEL maintainer="Saish Rane"
LABEL project="Employee Management System"

# -------------------------------
# Prevent Python from writing .pyc files
# -------------------------------
ENV PYTHONDONTWRITEBYTECODE=1

# -------------------------------
# Enable unbuffered logging
# -------------------------------
ENV PYTHONUNBUFFERED=1

# -------------------------------
# Working Directory
# -------------------------------
WORKDIR /app

# -------------------------------
# Install dependencies
# -------------------------------
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# -------------------------------
# Copy Application
# -------------------------------
COPY . .

# -------------------------------
# Runtime Variables
# -------------------------------
ENV SECRET_KEY=docker-secret-key
ENV DEBUG=True
ENV DATABASE_NAME=employee.db

# -------------------------------
# Expose Port
# -------------------------------
EXPOSE 5000

# -------------------------------
# Start Flask
# -------------------------------
CMD ["python","app.py"]