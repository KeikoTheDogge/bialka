from fastapi import APIRouter, \
    Depends, \
    HTTPException, \
    UploadFile, \
    File
from sqlalchemy.orm import Session
from dependency import get_db
from functions.functions_protein import get_protein, \
    get_proteins, \
    get_protein_by_name, \
    create_protein, \
    add_fasta_file, \
    delete_protein
from schemas.schemas_protein import ProteinCreate
from typing import Annotated
from authorization import get_current_active_user
from schemas.schemas_user import User

router = APIRouter(
    prefix="/protein",
    tags=["protein"]
)


@router.get("/")
def read_proteins(current_user: Annotated[User, Depends(get_current_active_user)],
                  db: Session = Depends(get_db)):
    """
    Get all proteins from database
    """
    proteins = get_proteins(db)
    if not proteins:
        raise HTTPException(status_code=404, detail="There are no proteins in database")
    return proteins


@router.get("/{protein_id}")
def read_protein(current_user: Annotated[User, Depends(get_current_active_user)],
                 protein_id: int, db: Session = Depends(get_db)):
    """
    Get protein by ID
    """
    protein = get_protein(db, protein_id)
    if protein is None:
        raise HTTPException(status_code=404, detail="Protein not found")
    return protein


@router.get("/{name}")
def read_protein_by_name(current_user: Annotated[User, Depends(get_current_active_user)],
                         name: str, db: Session = Depends(get_db)):
    """
    Get protein by name
    """
    protein = get_protein_by_name(db, name)
    if protein is None:
        raise HTTPException(status_code=404, detail="Protein not found")
    return protein


@router.post("/")
def create_new_protein(current_user: Annotated[User, Depends(get_current_active_user)],
                       protein: ProteinCreate, db: Session = Depends(get_db)):
    """
    Create new protein
    - **amino_acid**: number of aminos in protein
    - **function**: protein function
    - **gene_symbol**: protein gene symbol (eg. HBB)
    - **organism**: protein organism
    """
    existing_protein = get_protein_by_name(db, protein.name)
    if existing_protein:
        raise HTTPException(status_code=400, detail="Protein with this name already exists")
    return create_protein(db=db, protein=protein)


@router.post("/add_fasta/{protein_id}")
def upload_fasta_endpoint(current_user: Annotated[User, Depends(get_current_active_user)],
                          protein_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    """
    Add fasta file to protein
    - **protein_id**: protein ID
    - **file**: file in fasta
    """
    return add_fasta_file(db=db, protein_id=protein_id, file=file)


@router.delete("/{protein_id}")
def delete_proteins(current_user: Annotated[User, Depends(get_current_active_user)],
                    protein_id: int, db: Session = Depends(get_db)):
    """
    Delete protein from database
    - **protein_id**: protein ID
    """
    return delete_protein(db, protein_id)
