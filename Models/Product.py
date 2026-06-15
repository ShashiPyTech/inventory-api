from sqlalchemy import column, Column, Boolean
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from Database.database import Base

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    is_deleted = Column(Boolean, nullable=False, default=False)
