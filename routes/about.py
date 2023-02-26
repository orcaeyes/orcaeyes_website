from fastapi import APIRouter, Request
from templates import templates

router = APIRouter(tags=["About"])

@router.get("/about")
async def home(request: Request):
    title = "О нас"
    return templates.TemplateResponse('about.html', context={'request': request, 'title': title})