from sqlalchemy import Column, Integer, String, Text, Float, TIMESTAMP
from db import Base

class Protein(Base):
    __tablename__ = "protein"

    id = Column(Integer, primary_key=True)
    name = Column(String(50)) # ograniczam ilosc znakow bo to fancy
    gene_symbol = Column(String(10))
    sequence = Column(Text)
    molecular_weight = Column(Float)
    isoelectric_point = Column(Float)
    organizm = Column(String(50))
    function = Column(Text)
    localization = Column(String(10))
    expression_level = Column(String(50))
    date_added = Column(TIMESTAMP)
