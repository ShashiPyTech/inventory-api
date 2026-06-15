from fastapi import FastAPI

from Database.database import Base
from Database.database import engine
from routers.order_router import orders_router
from routers.customer_router import customer_router

from routers.product_router import router
from Models import init

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Inventory API"
)

app.include_router(router)
app.include_router(customer_router)

app.include_router(orders_router)