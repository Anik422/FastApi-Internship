from fastapi import FastAPI, status
from routers import blog_get, product, blog_post, user, article, file
from auth import authentication
from db import models
from db.database import engine
from exceptions.stroy_exceptions import StroryException
from fastapi.responses import JSONResponse
from fastapi import Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app  = FastAPI()
app.include_router(authentication.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router) 
app.include_router(product.router)
app.include_router(file.router)





@app.get("/", 
            status_code=status.HTTP_200_OK,
            tags=['Root'],
            summary="Root API",
            description="This is the root API",
            response_description="Root API response"
         ) 
def index():
    return {"message": "Hello, World"}





@app.exception_handler(StroryException)
async def story_exception_handler(request: Request, exc: StroryException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"datail": exc.name}
    )


models.Base.metadata.create_all(engine)


origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.mount("/files", StaticFiles(directory="files"), name="files")