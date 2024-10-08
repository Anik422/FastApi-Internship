from fastapi import APIRouter, BackgroundTasks
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from request_models.product_request import ProductBase
from custom_log import log



router = APIRouter(
    prefix="/templates",
    tags=['Templates']
)


tamplates = Jinja2Templates(directory="templates")


@router.post('/product/{id}', response_class=HTMLResponse)
def get_product(id: str, product: ProductBase, request: Request, bt:BackgroundTasks):
    bt.add_task(log_template_call, "Product template called")
    return tamplates.TemplateResponse(
        "product.html", 
        {
            "request": request, 
            "id": id,
            "title": product.title,
            "description": product.description,
            "price": product.price
        }
    )


def log_template_call(message: str):
    log("MyAPI", message)
