

from sqlalchemy.orm import Session
from Models.customer_db_model import Customers
from Schemas.customer_schema import CustomerCreate
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

class CustomerRepository:

    def __init__(self,db: Session):
        self.db = db


    def create_customer(self, customer: CustomerCreate):

        try:
            db_customer = Customers(customer_name=customer.name)

            self.db.add(db_customer)
            self.db.commit()
            self.db.refresh(db_customer)
            return db_customer

        except SQLAlchemyError:
            self.db.rollback()
            raise HTTPException(
                status_code=500,
                detail="Internal Server Error"
            )


    def get_customer_by_id(self, customer_id: int):
        try:
            result = self.db.query(Customers).filter(Customers.id == customer_id).first()

            if not result:
                raise HTTPException(
                    status_code=404,
                    detail="Customer not found"
                )

        except SQLAlchemyError:
            HTTPException(
                status_code=500,
                detail="Internal Server Error"
            )

    def get_all(self):
        try:
            result = self.db.query(Customers).all()
            return result
        except SQLAlchemyError:
            HTTPException(
                status_code=500,
                detail="Internal Server Error"
            )