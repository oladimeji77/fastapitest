from fastapi import FastAPI
from routers import buy

app = FastAPI(title="Test Docker", version='1.1.2')
app.include_router(buy.router)

@app.get("/")
async def index():
    return {"message":"Welcome"}

