from pydantic import BaseModel

class ProteinCreate(BaseModel):
    name: str
    gene_symbol: str
    sequence: str
    molecular_weight: float
    isoelectric_point: float
    organizm: str
    function: str
    localization: str
    expression_level: str
