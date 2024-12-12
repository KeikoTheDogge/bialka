from fastapi import FastAPI, \
    Depends, \
    HTTPException
from sqlalchemy.orm import Session
from routers import routers_protein
from routers import routers_user
from routers import routers_uniprot


app = FastAPI()
app.include_router(routers_protein.router)
app.include_router(routers_user.router)
app.include_router(routers_uniprot.router)

@app.get("/")
async def root():
    return {"message": "Satoru Gojo is alive and healthy"}
