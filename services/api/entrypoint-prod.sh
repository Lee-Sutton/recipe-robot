#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z recipes-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

gunicorn -b manage:app
