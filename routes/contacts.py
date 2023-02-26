from fastapi import APIRouter, Request
from templates import templates

router = APIRouter(tags=["Contacts"])

@router.get("/contacts")
async def home(request: Request):
    title = "Контакты"
    return templates.TemplateResponse('contacts.html', context={'request': request, 'title': title})