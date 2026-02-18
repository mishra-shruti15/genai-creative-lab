from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This script sets up the PostgreSQL connection and session handling.
DATABASE_URL = (
    "postgresql://postgres:postgres123@localhost:5432/feedback_db"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

