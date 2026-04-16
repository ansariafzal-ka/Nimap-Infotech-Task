from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.db import get_db

router = APIRouter(prefix='/api/categories', tags=['category'])

@router.get('/', status_code=status.HTTP_200_OK)
def get_all_categories(db:Session=Depends(get_db)):
    pass

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_category(request, db:Session=Depends(get_db)):
    pass

@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_category(id:int, db:Session=Depends(get_db)):
    pass

@router.put('/{id}', status_code=status.HTTP_201_CREATED)
def update_category(id:int, db:Session=Depends(get_db)):
    pass

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_category(id:int, db:Session=Depends(get_db)):
    pass