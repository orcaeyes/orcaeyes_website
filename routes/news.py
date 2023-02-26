from fastapi import APIRouter, Request
from templates import templates
from services.new import *

router = APIRouter(tags=["News"])

@router.get("/news")
async def news(request: Request):
    title = "Новости"
    news = get_news()
    return templates.TemplateResponse('news.html', context={'request': request, 'title': title, 'news': news})

@router.get("/new/{id}")
async def new(request: Request, id: int):
    response_new = get_new(id)
    title = response_new.title
    return templates.TemplateResponse('new.html', context={'request': request, 'title': title, 'new': response_new})