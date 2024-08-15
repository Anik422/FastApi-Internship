from fastapi import APIRouter, status, Response
from typing import Optional
from enum import Enum



router = APIRouter(
    prefix="/blog",
    tags=['Blog']
)




#Query Parameters
@router.get("/all", 
            status_code=status.HTTP_200_OK, 
            summary="Get all blogs",
            description="This API returns all blogs",
            response_description="All blogs response"
         ) 
def get_all_blogs(page:int = 1, page_size : Optional[int] = None):
    return {"message": f"All {page_size} blogs on page {page}"}




@router.get("/{id}/comments/{comment_id}", 
            status_code=status.HTTP_200_OK, 
            tags=['Comment'],
            response_description="Blog comment response",
    )
def get_comment(id:int, comment_id:int, valid:bool = True, username: Optional[str] = None):
    """
    This API returns comment for a blog

    - **id**: blog id
    - **comment_id**: comment id
    - **valid**: valid comment
    - **username**: username

    """
    return {"message": f"blog_id {id}, comment_id {comment_id}, valid {valid}, username: {username}"}



# Enum class 
class BlogType(str, Enum):
    short = "Short"
    story = "Story" 
    howto = "Howto"
#predefined value
@router.get("/type/{type}", 
            status_code=status.HTTP_200_OK, 
            summary="Get blog type",
            description="This API returns blog type",
            response_description="Blog type response"
        ) 
def get_blog_type(type : BlogType):
    return {"message": f"Blog type {type}"}




# path parameters
@router.get('/{id}', 
            status_code=status.HTTP_200_OK, 
            summary="Get blog by id",
            description="This API returns blog by id",
            response_description="Blog by id response"
        ) 
def get_blog(id:int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Blog {id} not found"}
    response.status_code = status.HTTP_200_OK
    return {"message": f"Blog with id {id}"}
