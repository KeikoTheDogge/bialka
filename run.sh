sleep 5
echo "Migracji bazy danych..."
DB_URL="postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db/${POSTGRES_DB}" alembic upgrade heads
echo "Migracja zakonczona..."
echo "Start serwera REST..."
uvicorn main:app --host 0.0.0.0 --port 8000
