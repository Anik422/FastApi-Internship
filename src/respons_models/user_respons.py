from pydantic import BaseModel
from typing import List
from .artical_respons import ArticleModel


class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[ArticleModel] = []
    
    class Config:
        from_attributes = True

    