from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.categories_routes import router as category_router
from src.routes.products_routes import router as product_router
from src.config.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title='Nimap Infotech Task')
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True
)

app.include_router(category_router)
app.include_router(product_router)