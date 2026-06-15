

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List

from Repositories.order_repository import OrderRepository
from Schemas.api_response import APIResponse
from Schemas.order_schema import CreateOrder, OrderResponse
from Database.dependencies import get_db
from Services.order_service import OrderService

orders_router = APIRouter()

@orders_router.post("/orders", response_model=APIResponse[OrderResponse])
def create_order(order:CreateOrder, db: Session = Depends(get_db)):
    repository = OrderRepository(db=db)
    service = OrderService(repository=repository)
    result = service.create_order(order)

    return  APIResponse(
        success=True,
        message="Order created successfully",
        data=result
    )

@orders_router.get("/orders")
def get_orders(db: Session = Depends(get_db)):
    repository = OrderRepository(db=db)
    service = OrderService(repository=repository)
    return  service.get_all_orders()

@orders_router.get("/orders/{customer_id}")
def get_order_by_customer(customer_id: int, db: Session = Depends(get_db)):
    repository = OrderRepository(db=db)
    service = OrderService(repository=repository)
    return  service.get_order_by_customer_id(customer_id=customer_id)
