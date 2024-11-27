from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# tymczasowa baza danych w pamieci, potem sie zamieni jak firebase bedzie wspolpracowal
engine = create_engine('sqlite:///:memory:', echo=True)

# sesja z baza danych
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)