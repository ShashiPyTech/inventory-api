
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from Database.database import Base

class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    customer = relationship("Customers", back_populates="orders")