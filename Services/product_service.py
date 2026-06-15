
# Standard Library
from fastapi import HTTPException

# Local imports
from Models.Product import Product
from Repositories.product_repository import ProductRepository
from Schemas.product_schema import ProductCreate

class ProductService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def create_product(self,data:ProductCreate):
        product = Product(
            name=data.name,
            price=data.price,
            quantity=data.quantity
        )
        return self.repository.create(product)

    def get_products(self):
        return self.repository.get_all()

    def update_product(self,product_id,data):
        product = self.repository.find_by_id(product_id)

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        product.name = data.name
        product.price = data.price
        product.quantity = data.quantity

        self.repository.save()

        return product

    def delete_product(self,product_id):
        product = self.repository.find_by_id(product_id)

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        product.is_deleted = True
        self.repository.save()

        return  {
            "message": "Product deleted"
        }