
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import os


##DATABASE_URL = "sqlite:///inventory.db"
#DATABASE_URL = "postgresql+psycopg2://localhost:5433/inventory_db"

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:your_password@localhost:5433/inventory_db"
)

if not DATABASE_URL:
    raise Exception("DATABASE_URL environment variable is not set")

engine = create_engine(DATABASE_URL)

# engine = create_engine(
#     DATABASE_URL,
#     connect_args={"check_same_thread": False}
# )

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
