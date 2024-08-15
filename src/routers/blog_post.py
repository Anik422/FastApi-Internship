from fastapi import APIRouter, status, Query
from typing import Optional
from  request_models.bolg_model import BlogModel


router = APIRouter(
    prefix="/blog",
    tags=['Blog']
)



@router.post('/new/{id}', status_code=status.HTTP_201_CREATED)
def create_blog(blog: BlogModel, id:int, version: int = 1):
    """
    This API creates a new blog
    - **blog**: blog object
    - **id**: blog id
    - **version**: version
    """

    return {"id" : id, "data" : blog, "version" : version, "message" : "Blog created successfully"}


@router.post("/new/{id}/comment", status_code=status.HTTP_201_CREATED)
def create_comment(blog: BlogModel, id:int, commnt_id=Query(None, title="Comment ID", description="This is the comment ID")):
    """
    This API creates a new comment
    - **blog**: blog object
    - **id**: blog id
    - **comment_id**: comment id
    """

    return {"id" : id, "data" : blog, "comment_id" : commnt_id, "message" : "Comment created successfully"}