import httpx


UNIPROT_API_URL = "https://rest.uniprot.org/uniprotkb/"


async def fetch_protein(protein_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{UNIPROT_API_URL}{protein_id}")
        if response.status_code == 200:
            return response.json()
        return None
