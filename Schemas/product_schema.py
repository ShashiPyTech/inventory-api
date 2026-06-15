
from pydantic import BaseModel
from pydantic import ConfigDict

class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int
    is_deleted: bool = False

class ProductResponse(ProductCreate):
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )