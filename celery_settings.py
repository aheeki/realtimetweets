import os

CELERY_TASK_SERIALIZER = 'json'
BROKER_URL = os.environ.get('RABBITMQ_BIGWIG_URL','amqp://localhost:5672')