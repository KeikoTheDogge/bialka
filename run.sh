#!/bin/bash
while true; do
    pg_isready -d $POSTGRES_DB -h db -p 5434 -U $POSTGRES_USER
    if [ $? -eq 0 ];then
        break
    fi
    echo "Wait for database..."
    sleep 1
done
echo "Database connected"
echo "Database migration..."
DB_URL="postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db/${POSTGRES_DB}" alembic upgrade heads
echo "Database migrated"
echo "Starting protein server..."
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
