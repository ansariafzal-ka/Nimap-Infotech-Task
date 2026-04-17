from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field
from datetime import datetime
from src.config.db import Base

class CategoryModel(Base):
    __tablename__='category'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    products = relationship('ProductModel', back_populates='category')

class CategorySchema(BaseModel):
    name: str = Field(...)

class CategoryOutSchema(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(...)
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True