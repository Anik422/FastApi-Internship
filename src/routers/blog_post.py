from fastapi import APIRouter, status, Query, Body, Path
from typing import Optional, List, Dict
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
def create_comment(blog: BlogModel, id:int, 
                   commnt_title = Query(None, 
                                        min_length=5, 
                                        max_length=50, 
                                        title="Comment Title",
                                        description="Title of the comment",
                                        alias="commentTitle",
                                        deprecated=True
                                    ),
                    content: str =  Body(..., 
                                         min_length=10, 
                                         max_length=100,
                                        
                                        ),              
                    v: Optional[List[str]] = Query(["1.0", "1.1", "1.2"],),
                    commnt_id: Optional[int] = Path(..., 
                                                    title="Comment Id", 
                                                    description="Id of the comment",
                                                    ge=1,
                                                    le=100,
                                                    )               
                    ):
    """
    This API creates a new comment
    - **blog**: blog object
    - **id**: blog id
    - **commnt_title**: comment title
    - **commentId**: comment id
    - **content**: comment content
    - **v**: version 
    """

    return {"id" : id, 
            "comment_title" : commnt_title,
            "blog" : blog, 
            "comment_id" : commnt_id, 
            "content" : content, 
            "version" : v,
            "message" : "Comment created successfully"
            }