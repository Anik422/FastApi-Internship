from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_article
from typing import List
from request_models.artical_request import ArticleBase
from respons_models.artical_respons import ArticleModel, ArticleDisplay

router = APIRouter(
    prefix="/article",
    tags=['Article']
)


@router.post('/', response_model=ArticleModel)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)


@router.get('/{id}', response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db)):
    return db_article.get_article(db, id)