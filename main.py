from fastapi import FastAPI
from src.routes.categories_routes import router as category_router
from src.routes.products_routes import router as product_router
from src.config.db import Base, engine

Base.metadata_create_all(engine)

app = FastAPI(title='Nimap Infotech Task')

app.include_router(category_router)
app.include_router(product_router)