from sqlalchemy.orm import Session
from model import Protein
from schemas.schemas_protein import ProteinCreate
from Bio import SeqIO
from fastapi import HTTPException, \
    UploadFile
from io import StringIO


def get_proteins(db: Session):
    return db.query(Protein).all()


def get_protein(db: Session, protein_id: int):
    return db.query(Protein).filter(Protein.id == protein_id).first()


def get_protein_by_name(db: Session, protein_name: str):
    return db.query(Protein).filter(Protein.name == protein_name).first()


# TODO: add exceptions
def create_protein(db: Session, protein: ProteinCreate):
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


def add_fasta_file(db: Session, protein_id: int, file: UploadFile):
    protein = db.query(Protein).filter(Protein.id == protein_id).first()
    if not protein:
        raise HTTPException(status_code=404, detail="Protein not found")
    # endswith not working with UploadFile, try something else
    # if not (file.endswith('.fasta') or filename.endswith('.fa')):
    #     raise HTTPException(status_code=400, detail="Invalid file type. Only fasta files are allowed.")
    try:
        content = file.file.read().decode("utf-8")
        fasta_records = list(SeqIO.parse(StringIO(content), "fasta"))
        if not fasta_records:
            raise HTTPException(status_code=400, detail="FASTA file is empty or invalid.")
        protein.sequence = str(fasta_records[0].description) + "\n" + str(fasta_records[0].seq)
        db.commit()
        db.refresh(protein)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error parsing FASTA file: {str(e)}")
    return protein


def delete_protein(db: Session, protein_id: int):
    db_protein = get_protein(db, protein_id)
    db.delete(db_protein)
    db.commit()
    return db_protein
