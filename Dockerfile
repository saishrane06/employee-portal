FROM python:3.12-slim

LABEL maintainer="Saish Rane"
LABEL project="Employee Management System"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create application user
RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup appuser

# Change ownership
RUN chown -R appuser:appgroup /app

# Switch user
USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"

#CMD ["python","app.py"]
#CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
CMD ["gunicorn", "-c", "gunicorn.conf.py", "app:app"]