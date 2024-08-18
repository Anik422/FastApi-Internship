from pydantic import BaseModel

class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int
    
    class Config:
        from_attributes = True