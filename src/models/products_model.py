from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from pydantic import BaseModel, Field
from datetime import datetime
from src.config.db import Base

class ProductModel(Base):
    __tablename__='product'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class ProductSchema(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: str | None = None
    category_id: int = Field(..., gt=0)

class ProductOutSchema(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1, max_length=255)
    description: str | None = None
    category_id: int = Field(..., gt=0)
    created_at: datetime
    updated_at: datetime