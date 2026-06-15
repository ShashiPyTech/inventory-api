from Repositories.customer_repository import CustomerRepository
from Schemas.customer_schema import CustomerCreate
from fastapi import HTTPException


class CustomerService:
    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def create_customer(self, data: CustomerCreate):
        return  self.repository.create_customer(data)

    def get_customer_by_id(self, customer_id: int):
        customer = self.repository.get_customer_by_id(customer_id)
        if not customer:
            raise HTTPException(
                status_code=404,
                detail="Customer not found"
            )
        return customer

    def get_all_customer(self):
        return self.repository.get_all()