from sqlalchemy import Column, Integer, String, Text, Float, TIMESTAMP
from db import Base

class Protein(Base):
    __tablename__ = "protein"

    id = Column(Integer, primary_key=True)
    name = Column(String(50)) # ograniczam ilosc znakow bo to fancy
    gene_symbol = Column(String(10))
    sequence = Column(Text)
    amino_acid = Column(Integer)
    organism = Column(String(50))
    function = Column(Text)
    localization = Column(String(10))
