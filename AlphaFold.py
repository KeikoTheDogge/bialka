from fastapi import APIRouter, HTTPException, Depends
import httpx
from authorization import get_current_active_user
from schemas.schemas_user import User
from typing import Annotated

router = APIRouter(
    prefix="/AlphaFold",
    tags=["AlphaFold"]
)


API_KEY = "AIzaSyCeurAJz7ZGjPQUtEaerUkBZ3TaBkXrY94"


@router.get("/prediction/{qualifier}")
async def get_prediction(current_user: Annotated[User, Depends(get_current_active_user)],
                         qualifier: str):
    url = f"https://alphafold.ebi.ac.uk/api/prediction/{qualifier}?key={API_KEY}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as http_error:
            raise HTTPException(status_code=response.status_code, detail=str(http_error))
        except Exception as err:
            raise HTTPException(status_code=500, detail=str(err))


@router.get("/uniprot_information/summary/{qualifier}")
async def get_prediction(current_user: Annotated[User, Depends(get_current_active_user)],
                         qualifier: str):
    url = f"https://alphafold.ebi.ac.uk/api/uniprot/summary/{qualifier}.json?key={API_KEY}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as http_error:
            raise HTTPException(status_code=response.status_code, detail=str(http_error))
        except Exception as err:
            raise HTTPException(status_code=500, detail=str(err))
