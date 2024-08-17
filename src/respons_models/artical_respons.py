from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

class ArticleModel(BaseModel):
    title: str
    content: str
    published: bool
    
    class Config:
        orm_mode = True

class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User
    
    class Config:
        orm_mode = True