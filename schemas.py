from pydantic import BaseModel

class ProteinBase(BaseModel):
    name: str
    gene_symbol: str
    sequence: str
    amino_acid: int
    organism: str
    function: str
    localization: str

class ProteinCreate(ProteinBase):
    pass

    class Config:
        json_schema_extra = {
            "example": {
                "name": "hemoglobina",
                "gene_symbol": "HBA",
                "sequence": "hemoglobina.fasta",
                "amino_acid": "142",
                "organism": "homo sapiens",
                "function": "involved in oxygen transport from the lung to the various peripheral tissues",
                "localization": "chromosom 16"
            }
        }

class Protein(ProteinBase):
    id: int

    class Config:
        from_attributes = True
