from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.models.products_model import ProductSchema, ProductOutSchema
from src.controllers import products_controllers
from typing import List

router = APIRouter(prefix='/api/products', tags=['product'])

@router.get('/',response_model=List[ProductOutSchema], status_code=status.HTTP_200_OK)
def get_all_products(page:int=1, db:Session=Depends(get_db)):
    return products_controllers.get_all_products(db, page)

@router.post('/', response_model=ProductOutSchema, status_code=status.HTTP_201_CREATED)
def create_product(request:ProductSchema, db:Session=Depends(get_db)):
    return products_controllers.create_product(request, db)

@router.get('/{id}', response_model=ProductOutSchema, status_code=status.HTTP_200_OK)
def get_product(id:int, db:Session=Depends(get_db)):
    return products_controllers.get_product(id, db)

@router.put('/{id}', response_model=ProductOutSchema, status_code=status.HTTP_201_CREATED)
def update_product(id:int, request:ProductSchema, db:Session=Depends(get_db)):
    return products_controllers.update_product(id, request, db)

@router.delete('/{id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id:int, db:Session=Depends(get_db)):
    return products_controllers.delete_product(id, db)