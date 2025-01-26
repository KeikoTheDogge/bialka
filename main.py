from fastapi import FastAPI
import authorization
from routers import routers_protein, routers_uniprot, routers_user, protein_tools
from docs import description
import AlphaFold

app = FastAPI(
    title="Backend",
    description=description
)


app.include_router(routers_protein.router)
app.include_router(routers_user.router)
app.include_router(routers_uniprot.router)
app.include_router(authorization.router)
app.include_router(AlphaFold.router)
app.include_router(protein_tools.router)


@app.get("/")
async def root():
    return {"message": "App is alive and healthy"}
