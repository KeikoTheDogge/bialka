# Protein server

## Instalacja

Do uruchomienia dockera w systemie Windows niezbędna jest aplikacji docker desktop,
którą można pobrać ze strony docker.com. Aplikacja musi być cały czas aktywna w tle. 

Następnie należy stworzyć plik .env zgodnie ze wzorem: 

```.dotenv
DB_URL=postgresql://docker:password@db/db_name
POSTGRES_USER=docker
POSTGRES_PASSWORD=password
POSTGRES_DB=db_name
SECRET_KEY=sekret_value
ALGORITHM="HS256"
```

Następnie wystarczy: 
1. Sklonować repozytorium
2. Zabudować docker-compose 
3. Uruchomić docker-compose

Komendy do wpisania w terminal: 

```bash
git clone
docker-compose build
docker-compose up
```

## Dostępne strony

* Strona localhost:8000/ - "message: App is alive and healthy"
* Strona localhost:8000/docs - interaktywna dokumentacja za pomocą której możena testować endpointy
