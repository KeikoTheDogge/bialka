from fastapi import FastAPI
import authorization
from routers import routers_protein
from routers import routers_user
from routers import routers_uniprot
from docs import description


app = FastAPI(
    title="Backend",
    description=description
)


app.include_router(routers_protein.router)
app.include_router(routers_user.router)
app.include_router(routers_uniprot.router)
app.include_router(authorization.router)

@app.get("/")
async def root():
    return {"message": "App is alive and healthy"}
