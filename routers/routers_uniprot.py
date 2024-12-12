from fastapi import APIRouter, HTTPException
from functions.functions_uniprot import fetch_protein


router = APIRouter(
    prefix="/uniprot",
    tags=["uniprot"]
)


@router.get("/{protein_id}")
async def get_protein(protein_id: str):
    """
    Fetch data from uniprot API
    - **protein_id**: protein ID (for hemoglobin: P12345)
    - **return**: JSON file with all information from uniprot database
    """
    protein_data = await fetch_protein(protein_id)
    if not protein_data:
        raise HTTPException(status_code=404, detail=f"Protein {protein_id} not found")
    return protein_data
