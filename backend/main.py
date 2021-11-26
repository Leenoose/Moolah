from fastapi import FastAPI
from fastapi import APIRouter

from api.routers import router

app = FastAPI()
app.include_router(router)


@app.get("/")
async def root():
    return {"Hello": "World"}
