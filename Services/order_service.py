
from Repositories.order_repository import OrderRepository
from Schemas.order_schema import CreateOrder, OrderResponse
from fastapi import HTTPException


class OrderService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def create_order(self, order: CreateOrder):
        return self.repository.create(order)

    def get_all_orders(self):
       return self.repository.get_all_orders()

    def get_order_by_customer_id(self, customer_id: int):
        customer_available  = self.repository.get_customer_order(customer_id)

        if not customer_available:
            raise  HTTPException(
                status_code=404,
                detail="Customer not found"
            )

        return customer_available