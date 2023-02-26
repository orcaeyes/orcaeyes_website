from fastapi import APIRouter, Request
from templates import templates

router = APIRouter(tags=["Products"])

@router.get("/products")
async def home(request: Request):
    title = "Продукты"
    return templates.TemplateResponse('products.html', context={'request': request, 'title': title})