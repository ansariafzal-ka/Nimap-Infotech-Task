from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.models.categories_model import CategoryModel, CategorySchema


def get_all_categories(db:Session, page:int=1):
    try:
        page_size=10
        skip = (page - 1) * page_size
        categories = db.query(CategoryModel).offset(skip).limit(page_size).all()
        return categories
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Failed to get all categories: {e}'
        )

def create_category(request:CategorySchema, db:Session):
    try:
        new_category = CategoryModel(
            name=request.name
        )
        db.add(new_category)
        db.commit()
        db.refresh(new_category)

        return new_category
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Failed to create category: {e}'
        )


def get_category(id:int, db:Session):
    try:
        category = db.query(CategoryModel).get(id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Category not found with id {id}'
            )
        return category
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Failed to get the category: {e}'
        )


def update_category(id:int, request:CategorySchema, db:Session):
    try:
        category = db.query(CategoryModel).get(id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Category not found with id {id}'
            )
        category.name = request.name

        db.commit()
        db.refresh(category)

        return category
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Failed to update the category: {e}'
        )

def delete_category(id:int, db:Session):
    try:
        category = db.query(CategoryModel).get(id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Category not found with id {id}'
            )
        
        db.delete(category)
        db.commit()
        return None
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Failed to delete the category: {e}'
        )