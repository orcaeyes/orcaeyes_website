import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import home

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(home.router)

@app.on_event("startup")
async def startup():
    pass

@app.on_event("shutdown")
async def shutdown():
    pass

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)