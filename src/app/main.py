from fastapi import FastAPI
from .endpoints import bots, users

app = FastAPI()

app.include_router(bots.router,prefix="/api", tags=["bots"])
app.include_router(users.router,prefix="/security",tags=["security"])

@app.get("/", tags=["status"])
async def root():
    return {"status": "connected"}