
# Standard Library Import
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

# Local Import
from Repositories.customer_repository import CustomerRepository
from Schemas.customer_schema import CustomerCreate, CustomerResponse
from Database.dependencies import get_db
from Services.customer_service import CustomerService
from Schemas.api_response import APIResponse

customer_router = APIRouter()

@customer_router.post(
    "/customers",
    response_model=APIResponse[CustomerResponse]
)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    repository = CustomerRepository(db=db)
    service = CustomerService(repository=repository)

    result = service.create_customer(customer)
    return APIResponse(
        success=True,
        message="Customers created",
        data=result
    )

@customer_router.get(
    "/customers/{customer_id}",
    response_model=APIResponse[CustomerResponse],
)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    repository = CustomerRepository(db=db)
    service = CustomerService(repository=repository)

    result =  service.get_customer_by_id(customer_id=customer_id)

    return APIResponse(
        success=True,
        message="Customers listed",
        data=result
    )

@customer_router.get(
    "/customers",
    response_model=APIResponse[list[CustomerResponse]],
)
def list_customers(db: Session = Depends(get_db)):
    repository = CustomerRepository(db=db)
    service = CustomerService(repository=repository)
    result = service.get_all_customer()
    return APIResponse(
        success=True,
        message="Customers listed",
        data=result
    )