from fastapi import APIRouter, Response, Header, Cookie, Form
from fastapi.responses import HTMLResponse, PlainTextResponse
from typing import Optional, List
from custom_log import log
import time

router = APIRouter(
    prefix="/product",
    tags=['Product']
)


products = [ 'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine', 'watermelon']


async def time_consuming_functionality():
    time.sleep(5)
    return "Ok"




@router.post('/new')
def create_product(name: str = Form(...)):
    products.append(name)
    return {"data": products}


@router.get('/all')
async def get_all_products():
    # log("MyAPI", "Call to get all products")
    await time_consuming_functionality()
    data = " ".join(products)
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key="test_cookie", value="cookie_value")
    return response


@router.get('/withheader')
def get_products(response:Response, 
                custom_header: Optional[List[str]] = Header(None),
                test_cookie: Optional[str] = Cookie(None)
                 ):
    if custom_header:
        response.headers['custom_response_header'] = " ".join(custom_header)
    return {"data":products, 'custom_header': custom_header, 'test_cookie': test_cookie}


@router.get('/{id}', responses={
    200: {
        'content': {'text/html': {
            'example': '<html><body><h1>Product</h1></body></html>'
        }},
        'description': 'Return the HTML for an object'
    },
    404:{
        'content': {'text/plain': {
            'example': 'Product not available'
        }},
        'description': 'A cleartext error message'

    }
})
def get_product(id: int):
    if id > len(products):
        return PlainTextResponse(content="Product not found", status_code=404, media_type="text/plain")
    product = products[id]
    out = f"""
    <html>
        <head>
            <title>Product</title>
            <style>
             .product {{
                width: 500px;
                height: 30px;
                border: 2px solid green;
                background-color: lightblue;
                text-align: center;
                }}
            </style>
        </head>
        <body>
           <div class="product">{product}</div> 
        </body>
    </html>
    """
    return HTMLResponse(content=out, media_type="text/html", status_code=200)