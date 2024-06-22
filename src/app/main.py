from fastapi import FastAPI
from endpoints import bots

app = FastAPI()

app.include_router(bots.router,prefix="/api", tags=["bots"])

@app.get("/")
async def root():
    return {"status": "connected"}