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


router = APIRouter(
    prefix="/protein",
    tags=["protein"]
)


@router.get("/")
def read_proteins(db: Session = Depends(get_db)):
    proteins = get_proteins(db)
    if not proteins:
        raise HTTPException(status_code=404, detail="There are no proteins in database")
    return proteins


@router.get("/{protein_id}")
def read_protein(protein_id: int, db: Session = Depends(get_db)):
    protein = get_protein(db, id=protein_id)
    if protein is None:
        raise HTTPException(status_code=404, detail="Protein not found")
    return protein


@router.get("/{name}")
def read_protein_by_name(name: str, db: Session = Depends(get_db)):
    protein = get_protein_by_name(db, name=name)
    if protein is None:
        raise HTTPException(status_code=404, detail="Protein not found")
    return protein


# proba polaczenia w jedno, nie przechodzi przez postmana
# @router.post("/")
# async def create_new_user( protein: ProteinCreate, db: Session = Depends(get_db),
#                      file: UploadFile = File(...)):
#     existing_protein = get_protein_by_name(db, name=protein.name)
#     if existing_protein:
#         raise HTTPException(status_code=400, detail="Protein with this name already exists")
#     if check_file(file) is False:
#         raise HTTPException(status_code=400, detail="Invalid file type. Only FASTA files are allowed.")
#     content = await file.read()
#     try:
#         fasta_str = content.decode("utf-8")
#         fasta_records = list(SeqIO.parse(StringIO(fasta_str), "fasta"))
#         if not fasta_records:
#             raise HTTPException(status_code=400, detail="FASTA file is empty or invalid.")
#         protein.sequence = str(fasta_records[0].seq)
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=f"Error parsing FASTA file: {str(e)}")
#     return create_protein(db=db, protein=protein)


@router.post("/")
async def create_new_user( protein: ProteinCreate, db: Session = Depends(get_db)):
    existing_protein = get_protein_by_name(db, name=protein.name)
    if existing_protein:
        raise HTTPException(status_code=400, detail="Protein with this name already exists")
    return create_protein(db=db, protein=protein)


@router.post("/add_fasta/{protein_id}")
def upload_fasta_endpoint(protein_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    return add_fasta_file(db=db, protein_id=protein_id, file=file)


@router.delete("/{protein_id}")
def delete_proteins(protein_id: int, db: Session = Depends(get_db)):
    return delete_protein(db, protein_id)
