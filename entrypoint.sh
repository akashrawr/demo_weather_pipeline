#!/bin/sh
echo "Running database migrations..."
alembic upgrade head

echo "Starting weather scheduler..."
python -m src.scheduler