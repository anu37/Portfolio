#!/bin/sh
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput 
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'sample@example.com', 'admin123')"
gunicorn portfolio.wsgi --bind 0.0.0.0:8000
# python manage.py runserver
