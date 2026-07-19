import os
from dotenv import load_dotenv

load_dotenv()


def _normalize_database_url(url):
    """Convert Railway/Heroku-style mysql:// URLs for SQLAlchemy + PyMySQL."""
    if url.startswith("mysql://"):
        return url.replace("mysql://", "mysql+pymysql://", 1)
    if url.startswith("mysql+pymysql://"):
        return url
    return url


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev")

    database_url = os.getenv("DATABASE_URL") or os.getenv("MYSQL_URL")
    if database_url:
        SQLALCHEMY_DATABASE_URI = _normalize_database_url(database_url)
    else:
        db_user = os.getenv("DB_USER", "root")
        db_password = os.getenv("DB_PASSWORD", "root123")
        db_host = os.getenv("DB_HOST", "localhost")
        db_port = os.getenv("DB_PORT", "3306")
        db_name = os.getenv("DB_NAME", "ai_exam_generator")
        SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "dev")

    AI_API_KEY = os.getenv("AI_API_KEY")
    AI_API_URL = os.getenv("AI_API_URL")
    AI_MODEL = os.getenv("AI_MODEL", "gpt-4o-mini")

    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
