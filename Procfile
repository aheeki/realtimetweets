web: gunicorn app:app
worker: celery worker -A tasks.celery -l INFO