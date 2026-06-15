
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from sqlalchemy.orm import Session
from Models.order_db_model import Orders
from Schemas.order_schema import CreateOrder


class OrderRepository:

    def __init__(self, db: Session):
        self.db = db


    def create(self, order: CreateOrder):
        try:
            db_order = Orders(name=order.name,price=order.price, customer_id=order.customer_id)
            self.db.add(db_order)
            self.db.commit()
            self.db.refresh(db_order)
            return db_order

        except SQLAlchemyError as e:
            self.db.rollback()

            print(str(e))
            raise HTTPException(
                status_code=500,
                detail="Database error occurred"
            )


    def get_all_orders(self):
        return self.db.query(Orders).all()

    def get_customer_order(self, customer_id: int):
        return self.db.query(Orders).filter(Orders.customer_id == customer_id).first()