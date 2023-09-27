import os

from dotenv import load_dotenv

load_dotenv()

"""
Configuration file.
"""

SERVICE_NAME = "bs-db_connector-ms"
"""Microservice name."""

MS_VERSION = str(os.environ.get("MS_VERSION", "NOT AVAILABLE"))
"""Microservice version."""

SERVICE_PORT = int(os.environ.get("SERVICE_PORT", 80))
"""Port where the service is available."""

WORKERS = int(os.environ.get("WORKERS", 1))
"""Number of gRPC workers within a single instance (the number of messages that are processed simultaneously)."""

MAX_MSG_LENGTH = int(os.environ.get("MAX_MSG_LENGTH", -1))
"""Maximum length of gRPC messages received and sent, -1 indicates unlimited size."""

LOGGING_MODE = str(os.environ.get("LOGGING_MODE", "DEBUG"))
"""Logging level for information and errors."""

LOGGER_FORMAT_INFO = "%(asctime)s.%(msecs)03d-%(levelname)s-%(funcName)s()-%(message)s"
"""Logger format for the info level."""

LOGGER_FORMAT_DEBUG = "%(asctime)s.%(msecs)03d-%(levelname)s-%(filename)s.%(funcName)s()-l.%(lineno)d-%(message)s"
"""Logger format for the debug level."""

LOGGER_FORMAT = LOGGER_FORMAT_INFO if LOGGING_MODE == "INFO" else LOGGER_FORMAT_DEBUG
"""Logger format."""

BS_DB_CONNECTOR_MS_IP = str(os.environ.get("BS_DB_CONNECTOR_MS_IP", "192.168.94.12"))
"""Address bs-db_connector-ms microservice"""

BS_DB_CONNECTOR_MS_PORT = str(os.environ.get("BS_DB_CONNECTOR_MS_PORT", "91"))
"""Port bs-db_connector-ms microservice"""

BS_DATABASE_IP = str(os.environ.get("BS_DATABASE_IP", "192.168.94.12"))
"""Database IP."""

BS_DATABASE_PORT = str(os.environ.get("BS_DATABASE_PORT", "6666"))
"""Database port."""

BS_DATABASE_USERNAME = str(os.environ.get("BS_DATABASE_USERNAME", "postgres"))
"""Database username."""

BS_DATABASE_PASSWORD = str(os.environ.get("BS_DATABASE_PASSWORD", "password"))
"""Database password."""

BS_DATABASE_NAME = str(os.environ.get("BS_DATABASE_NAME", "postgres"))
"""Database name."""

BS_DATABASE_SCHEMA = str(os.environ.get("BS_DATABASE_SCHEMA", "public"))
"""Database schema."""
