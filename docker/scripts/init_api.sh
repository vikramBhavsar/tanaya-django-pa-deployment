#!/bin/bash

echo "Waiting for postgres..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

pipenv run python manage.py collectstatic --noinput
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
pipenv run daphne -b 0.0.0.0 -p 8000 tanaya_portfolio.asgi:application