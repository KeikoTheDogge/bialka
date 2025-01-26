from fastapi import APIRouter, UploadFile, HTTPException
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import os


router = APIRouter(
    prefix="/tools",
    tags=["tools"]
)


@router.post("/analyze-protein/")
async def analyze_protein(file: UploadFile):
    """
    Endpoint do analizy białka na podstawie pliku FASTA.
    Zwraca masę cząsteczkową i punkt izoelektryczny.
    """
    if not file.filename.endswith(".fasta"):
        raise HTTPException(status_code=400, detail="File must be .fasta.")

    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as f:
        content = await file.read()
        f.write(content)

    try:
        records = list(SeqIO.parse(file_location, "fasta"))
        if len(records) == 0:
            raise HTTPException(status_code=400, detail="Fasta file is empty.")

        protein_seq = str(records[0].seq)
        analyzed_protein = ProteinAnalysis(protein_seq)
        mw = analyzed_protein.molecular_weight()
        isoelectric_point = analyzed_protein.isoelectric_point()

        return {
            "sequence_id": records[0].id,
            "molecular_weight": f"{mw:.2f} Da",
            "isoelectric_point": f"{isoelectric_point:.2f}"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during analysis: {str(e)}")

    finally:
        if os.path.exists(file_location):
            os.remove(file_location)
