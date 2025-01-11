from fastapi import APIRouter, HTTPException, Depends
from functions.functions_uniprot import fetch_protein
from typing import Annotated
from schemas.schemas_user import User
from authorization import get_current_active_user


router = APIRouter(
    prefix="/uniprot",
    tags=["uniprot"]
)


@router.get("/{protein_id}")
async def get_uniprot_protein(current_user: Annotated[User, Depends(get_current_active_user)], protein_id: str):
    """
    Fetch data from uniprot API
    - **protein_id**: protein ID (for hemoglobin: P12345)
    - **return**: JSON file with all information from uniprot database
    """
    protein_data = await fetch_protein(protein_id)
    if not protein_data:
        raise HTTPException(status_code=404, detail=f"Protein {protein_id} not found")
    return protein_data
