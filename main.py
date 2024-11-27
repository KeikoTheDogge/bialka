from fastapi import FastAPI, Depends
from fastapi.responses import PlainTextResponse
from schemas import ProteinCreate
from models import Protein
from sqlalchemy.orm import Session
from dependency import get_db

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/proteins", response_class=PlainTextResponse)
async def create_protein(protein: ProteinCreate, db: Session = Depends(get_db)):
    new_protein = Protein(
        name=protein.name,
        gene_symbol=protein.gene_symbol,
        sequence=protein.sequence,
        molecular_weight=protein.molecular_weight,
        isoelectric_point=protein.isoelectric_point,
        organizm=protein.organizm,
        function=protein.function,
        localization=protein.localization,
        expression_level=protein.expression_level
    )
    db.add(new_protein)
    db.commit()
    db.refresh(new_protein)
    return f'protien successfully added to database! you awesome!'
