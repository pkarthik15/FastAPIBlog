import email
from typing import List, Optional
from datetime import datetime
from pydantic import  BaseModel, EmailStr


class ArticleBase(BaseModel):
    title : str 
    body : Optional[str] = None


class  ArticleCreate(ArticleBase):
    pass


class  Article(ArticleBase):
    id: int
    author: EmailStr
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email:EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    articles: List[Article] = []

