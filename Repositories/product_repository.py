from itertools import product

from sqlalchemy.orm import Session
from Schemas.product_schema import ProductCreate
from Models.Product import Product
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self):
        self.db.commit()

    def create(self, product: Product):
        try:
           self.db.add(product)
           self.db.commit()
           self.db.refresh(product)
           return product

        except SQLAlchemyError:
            self.db.rollback()
            raise HTTPException(
                status_code=500,
                detail="Database error occurred"
            )

    def get_all(self):
        return self.db.query(Product).filter(Product.is_deleted == False).all()

    def find_by_id(self, product_id: int):
        return self.db.query(Product).filter(
            Product.id == product_id,
            Product.is_deleted == False
        ).first()