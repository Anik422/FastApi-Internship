from fastapi import FastAPI, status
from routers import blog_get, product, blog_post, user, article, file,dependencies
from auth import authentication
from templates import templates
from db import models
from db.database import engine
from exceptions.stroy_exceptions import StroryException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi import Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import time
from client import html
from fastapi.websockets import WebSocket



app  = FastAPI()
app.include_router(authentication.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router) 
app.include_router(product.router)
app.include_router(file.router)
app.include_router(templates.router)
app.include_router(dependencies.router)





@app.get("/index", 
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

@app.get("/")
async def get(): 
    return HTMLResponse(html)


clients = []

@app.websocket("/chat")
async def chat_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    while True:
        data = await websocket.receive_text()
        for claient in clients:
            await claient.send_text(data)
            

models.Base.metadata.create_all(engine)



@app.middleware("http")
async def add_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    response.headers["X-Response-Time"] = str(duration)
    return response


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
app.mount("/templates/static", StaticFiles(directory="templates/static"), name="static")