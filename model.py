from sqlalchemy import Column, Integer, String, Text, Boolean
from db import Base


class Protein(Base):
    __tablename__ = "protein"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    gene_symbol = Column(String(10))
    sequence = Column(Text)
    amino_acid = Column(Integer)
    organism = Column(String(50))
    function = Column(Text)
    localization = Column(String(20))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    workstation = Column(String) #change to enum in next iteration
    disabled = Column(Boolean) #user can be active or not
