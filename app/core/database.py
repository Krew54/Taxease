
"""
Database configuration and session management for FastAPI application.

Sets up SQLAlchemy engine, session, and base class for ORM models.
"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import get_settings

settings = get_settings()

DATABASE_URL: str = f"postgresql+psycopg2://{settings.db_username}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base(metadata=MetaData())

def get_db() -> Session:
    """
    Dependency that provides a SQLAlchemy database session.

    Yields:
        Session: SQLAlchemy session object.

    Ensures the session is closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()