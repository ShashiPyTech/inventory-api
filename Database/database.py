
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


##DATABASE_URL = "sqlite:///inventory.db"
DATABASE_URL = "postgresql+psycopg2://localhost:5433/inventory_db"

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
