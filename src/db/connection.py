import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def get_source_engine():
    return create_engine(
        os.getenv("SOURCE_DB"),
        pool_size=5,
        max_overflow=10,
        pool_pre_ping=True
    )

def get_target_engine():
    return create_engine(
        "postgresql://user:password@localhost:5432/finance",
        pool_size=5,
        max_overflow=10,
        pool_pre_ping=True
    )