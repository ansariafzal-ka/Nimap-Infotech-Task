from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.config.db import get_db

router = APIRouter(prefix='/api/products', tags=['product'])

@router.get('/', status_code=status.HTTP_200_OK)
def get_all_products(db:Session=Depends(get_db)):
    pass