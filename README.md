# Backend aplikacji do sekwencjonowania białek

## Instalacja

1. Zainstalowanie wszystkich potrzebnych bibliotek poprzez konsolę - pip install requirements.txt
2. Stworzenie za pomocą konsoli lub w pgAdminie bazy danych protein_db
3. Nałożenie migracji na bazę danych - alembic upgrade head (nakłada migrację oznaczoną jako head)
4. Uruchomienie aplikacji z poziomu pycharma lub konsoli - -m uvicorn main:app --reload 

W konsoli w pycharmie będą pojawiały się opisy błędów - będę wdzięczna na zwrócenie na nie uwagi i 
wystawienie krótkiego raportu z działania aplikacji.

## Użycie

* Strona localhost:8000/ - "message: Application alive and healthy"
* Strona localhost:8000/docs - interaktywna dokumentacja za pomocą której możena testować endpointy

## Ważne

W budowie jest grupa postmanowa która również będzie zezwalała na testowanie endpointów. 
