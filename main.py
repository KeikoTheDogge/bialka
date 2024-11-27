from fastapi import FastAPI, Depends
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


@app.post("/proteins")
async def create_protein(protein: ProteinCreate, db: Session = Depends(get_db)):
    new_protein = Protein(
        name=protein.name,
        gene_symbol=protein.gene_symbol,
        sequence=protein.sequence,
        amino_acid=protein.amino_acid,
        organism=protein.organism,
        function=protein.function,
        localization=protein.localization
    )
    db.add(new_protein)
    db.commit()
    db.refresh(new_protein)
    return new_protein
