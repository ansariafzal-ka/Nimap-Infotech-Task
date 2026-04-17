from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.models.products_model import ProductModel, ProductSchema

def get_all_products(db:Session, page:int=1):
    try:
        page_size=10
        skip = (page - 1) * page_size
        products = db.query(ProductModel).offset(skip).limit(page_size).all()
        return products
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Failed to get all products: {e}')
            

def create_product(request:ProductSchema, db:Session):
    try:
        new_product = ProductModel(
            name = request.name,
            description = request.description,
            category_id = request.category_id,
        )
        db.add(new_product)
        db.commit()
        db.refresh(new_product)

        return new_product
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Failed to create product: {e}')
            

def get_product(id:int, db:Session):
    try:
        product = db.query(ProductModel).get(id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Product not found with id: {id}'
            )
        return product
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Failed to the product: {e}')
            

def update_product(id:int, request:ProductSchema, db:Session):
    try:
        product = db.query(ProductModel).get(id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Product not found with id: {id}'
            )
        product.name = request.name
        product.description = request.description
        product.category_id = request.category_id
        db.commit()
        db.refresh(product)

        return product
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Failed to update the product: {e}')
            

def delete_product(id:int, db:Session):
    try:
        product = db.query(ProductModel).get(id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Product not found with id: {id}'
            )
        db.delete(product)
        db.commit()

        return None
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Failed to delete the product: {e}')