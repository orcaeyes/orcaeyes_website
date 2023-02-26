from fastapi import APIRouter, Request
from templates import templates

router = APIRouter(tags=["Home"])

@router.get("/")
async def home(request: Request):
    title = "Orca Eyes"
    return templates.TemplateResponse('index.html', context={'request': request, 'title': title})