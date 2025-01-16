#!/bin/bash
while true; do
    psql -h db -U $POSTGRES_USER -d $POSTGRES_DB -p 5432 -c "SELECT 1;" > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        break
    fi
    echo "Wait for database..."
    sleep 1
done
echo "Database connected"
echo "Database migration..."
DB_URL="postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}" alembic upgrade heads
echo "Database migrated"
echo "Starting protein server..."
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
