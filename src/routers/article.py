from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_article
from typing import List
from request_models.artical_request import ArticleBase
from respons_models.artical_respons import ArticleModel, ArticleDisplay
from request_models.user_request import UserBase
from auth.oauth2 import get_current_user


router = APIRouter(
    prefix="/article",
    tags=['Article']
)


@router.post('/', response_model=ArticleModel)
def create_article(request: ArticleBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_article.create_article(db, request)


@router.get('/{id}', ) #response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    # return db_article.get_article(db, id)
    return {
        "data": db_article.get_article(db, id),
        "user": current_user
    }