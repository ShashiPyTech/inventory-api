
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from Database.database import Base



class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    customer_name = Column(String, nullable=False)

    orders = relationship("Orders", back_populates="customer")


