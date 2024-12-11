from fastapi import FastAPI, \
    Depends, \
    HTTPException
from sqlalchemy.orm import Session
from routers import routers_protein
from routers import routers_user


app = FastAPI()
app.include_router(routers_protein.router)
app.include_router(routers_user.router)

@app.get("/")
async def root():
    return {"message": "Satoru Gojo is alive and healthy"}
