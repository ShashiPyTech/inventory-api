from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict

class CreateOrder(BaseModel):
    customer_id: int
    name: str
    price: float

class OrderResponse(CreateOrder):
    id: int

    model_config = ConfigDict(from_attributes=True)

