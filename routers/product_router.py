
from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from Repositories.product_repository import ProductRepository
from Schemas.product_schema import ProductCreate
from Schemas.product_schema import ProductResponse
from Services.product_service import ProductService
from Database.dependencies import get_db

router = APIRouter()

@router.post("/products")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    repository = ProductRepository(db)
    service = ProductService(repository)
    return service.create_product(product)

@router.get("/products")
def get_products(db: Session = Depends(get_db)):
    repository = ProductRepository(db)
    service = ProductService(repository)
    return service.get_products()

@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    repository = ProductRepository(db)
    service = ProductService(repository)
    
    return  service.update_product(
        product_id,
        product
    )

@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    repository = ProductRepository(db)
    service = ProductService(repository)
    return service.delete_product(product_id)