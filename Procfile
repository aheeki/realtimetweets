web: gunicorn app:app
worker: celery -A tasks.celery worker -l INFO