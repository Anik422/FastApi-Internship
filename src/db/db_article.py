from sqlalchemy.orm import Session
from db.models import DbArticle
from fastapi import HTTPException, status
from exceptions.stroy_exceptions import StroryException


def create_article(db: Session, request: DbArticle):
    """
    Create a new article in the database.

    :param article: The article to be created.
    :type article: Article
    """
    if request.content.startswith("Once upon a time"):
        raise StroryException(status_code=status.HTTP_418_IM_A_TEAPOT, name="No stories please")
    new_article = DbArticle(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creator_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

def get_article(db: Session, id: int):
    """
    Get an article from the database by its id.

    :param id: The id of the article to retrieve.
    :type id: int
    """
    artcle = db.query(DbArticle).filter(DbArticle.id == id).first()
    if not artcle:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article with id {id} not found")
    return artcle