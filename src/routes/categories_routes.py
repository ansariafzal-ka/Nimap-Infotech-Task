from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.models.categories_model import CategorySchema, CategoryOutSchema
from src.controllers import categories_controllers
from typing import List

router = APIRouter(prefix='/api/categories', tags=['category'])

@router.get('/', response_model=List[CategoryOutSchema], status_code=status.HTTP_200_OK)
def get_all_categories(page:int=1, db:Session=Depends(get_db)):
    return categories_controllers.get_all_categories(db, page)

@router.post('/',response_model=CategoryOutSchema, status_code=status.HTTP_201_CREATED)
def create_category(request:CategorySchema, db:Session=Depends(get_db)):
    return categories_controllers.create_category(request, db)

@router.get('/{id}', response_model=CategoryOutSchema, status_code=status.HTTP_200_OK)
def get_category(id:int, db:Session=Depends(get_db)):
    return categories_controllers.get_category(id, db)

@router.put('/{id}', response_model=CategoryOutSchema, status_code=status.HTTP_201_CREATED)
def update_category(id:int, request:CategorySchema, db:Session=Depends(get_db)):
    return categories_controllers.update_category(id, request, db)

@router.delete('/{id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def delete_category(id:int, db:Session=Depends(get_db)):
    return categories_controllers.delete_category(id, db)