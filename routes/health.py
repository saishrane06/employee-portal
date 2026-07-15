from flask import Blueprint, jsonify
from database.db import get_connection
import logging

health = Blueprint("health", __name__)


@health.route("/health")
def health_check():
    logging.info("Health endpoint called")
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT 1")

        cursor.fetchone()

        cursor.close()
        conn.close()

        return jsonify(
            {
                "status": "healthy",
                "database": "connected"
            }
        ), 200

    except Exception as e:
        logging.error(f"Health check failed: {e}")
        return jsonify(
            {
                "status": "unhealthy",
                "error": str(e)
            }
        ), 500
    
    @health.route("/ready")
    def readiness():

        return {
            "status": "ready"
        }, 200