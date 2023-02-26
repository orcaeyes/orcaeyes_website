import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import home
from routes import contacts
from routes import products
from routes import news
from routes import about

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(home.router)
app.include_router(contacts.router)
app.include_router(products.router)
app.include_router(news.router)
app.include_router(about.router)

@app.on_event("startup")
async def startup():
    pass

@app.on_event("shutdown")
async def shutdown():
    pass

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)