from enum import Enum
from fastapi import FastAPI, status, Response
from typing import Optional


app  = FastAPI()



@app.get("/", status_code=status.HTTP_200_OK) 
def index():
    return {"message": "Hello, World"}

# path parameters order by value type
# @app.get("/blog/all")
# def get_all_blogs():
#     return {"message": "All blogs provided"}

#Query Parameters
@app.get("/blog/all", status_code=status.HTTP_200_OK) 
def get_all_blogs(page = 1, page_size : Optional[int] = None):
    return {"message": f"All {page_size} blogs on page {page}"}


@app.get("/blog/{id}/comments/{comment_id}", status_code=status.HTTP_200_OK) 
def get_comment(id:int, comment_id:int, valid:bool = True, username: Optional[str] = None):
    return {"message": f"blog_id {id}, comment_id {comment_id}, valid {valid}, username: {username}"}

# Enum class 
class BlogType(str, Enum):
    short = "Short"
    story = "Story" 
    howto = "Howto"
#predefined value
@app.get("/blog/type/{type}", status_code=status.HTTP_200_OK) 
def get_blog_type(type : BlogType):
    return {"message": f"Blog type {type}"}

# path parameters
@app.get('/blog/{id}', status_code=status.HTTP_200_OK) 
def get_blog(id:int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Blog {id} not found"}
    response.status_code = status.HTTP_200_OK
    return {"message": f"Blog with id {id}"}
