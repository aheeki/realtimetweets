import os

BROKER_URL = os.environ.get('CLOUDAMQP_URL')
CELERY_TASK_SERIALIZER = 'json'
MONGOLAB_URI = os.environ.get('MONGOLAB_URI')