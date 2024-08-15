from fastapi import FastAPI, status
from routers import blog_get
from routers import blog_post

app  = FastAPI()

app.include_router(blog_get.router)
app.include_router(blog_post.router)




@app.get("/", 
            status_code=status.HTTP_200_OK,
            tags=['Root'],
            summary="Root API",
            description="This is the root API",
            response_description="Root API response"
         ) 
def index():
    return {"message": "Hello, World"}