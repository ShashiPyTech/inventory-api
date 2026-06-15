
from pydantic import BaseModel
from pydantic import ConfigDict, Field



class CustomerCreate(BaseModel):
    name: str

class CustomerResponse(CustomerCreate):
    id: int
    name: str = Field(validation_alias="customer_name")

    model_config = ConfigDict(from_attributes=True)