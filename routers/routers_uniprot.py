from fastapi import APIRouter, HTTPException, Depends
import httpx
from typing import Annotated
from authorization import get_current_active_user
from schemas.schemas_user import User

router = APIRouter(
    prefix="/uniprot",
    tags=["uniprot"]
)

UNIPROT_API_URL = "https://rest.uniprot.org/uniprotkb/"


@router.get("/id/{protein_id}")
async def get_uniprot_protein_by_id(current_user: Annotated[User, Depends(get_current_active_user)],
                                    protein_id: str):
    """
    Fetch data from uniprot API by protein ID
    - **protein_id**: protein ID (e.g., P68871)
    - **return**: JSON file with all information from uniprot database
    """
    protein_data = await fetch_protein_by_id(protein_id)
    if not protein_data:
        raise HTTPException(status_code=404, detail=f"Protein {protein_id} not found")
    return extract_basic_info(protein_data)


@router.get("/name/{protein_name}")
async def get_uniprot_protein_by_name(current_user: Annotated[User, Depends(get_current_active_user)],
                                      protein_name: str):
    """
    Fetch data from uniprot API by protein name
    - **protein_name**: protein name (e.g., HBB_HUMAN)
    - **return**: JSON file with all information from uniprot database
    """
    protein_data = await fetch_protein_by_name(protein_name)
    if not protein_data:
        raise HTTPException(status_code=404, detail=f"Protein {protein_name} not found")
    return extract_basic_info(protein_data)


async def fetch_protein_by_id(protein_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{UNIPROT_API_URL}{protein_id}")
        if response.status_code == 200:
            return response.json()
        return None


async def fetch_protein_by_name(protein_name: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{UNIPROT_API_URL}search?query={protein_name}&format=json")
        if response.status_code == 200:
            data = response.json()
            if data['results']:
                return data['results'][0]
        return None


def extract_basic_info(protein_data):
    """
    Extract basic information from protein data
    """
    basic_info = {}

    if 'proteinDescription' in protein_data:
        basic_info['protein_name'] = protein_data['proteinDescription']['recommendedName']['fullName']['value']

    if 'organism' in protein_data:
        basic_info['organism'] = protein_data['organism']['scientificName']

    if 'primaryAccession' in protein_data:
        basic_info['primaryAccession'] = protein_data['primaryAccession']

    if 'uniProtkbId' in protein_data:
        basic_info['uniProtkbId'] = protein_data['uniProtkbId']

    if 'entryAudit' in protein_data:
        basic_info['firstPublicDate'] = protein_data['entryAudit']['firstPublicDate']

    if 'entryAudit' in protein_data:
        basic_info['lastSequenceUpdateDate'] = protein_data['entryAudit']['lastSequenceUpdateDate']

    if 'sequence' in protein_data:
        basic_info['sequence_value'] = protein_data['sequence']['value']

    return basic_info
