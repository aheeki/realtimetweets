import os

BROKER_URL = os.environ.get('CLOUDAMQP_URL')
CELERY_TASK_SERIALIZER = 'json'
MONGOLAB_URI = os.environ.get('MONGOLAB_URI')

CLIENT_KEY="iFxuEMWv8110vLIWWqA54w"
CLIENT_SECRET="rC0cr1w0heC6swvuDTDIiE98ipNvH6WiEI62YzeC0k"
ACCESS_TOKEN="991518511-9QlULoonEjUs5G3M7Mhc1m3iAQPISRqYtitXrmHh"
ACCESS_SECRET="72ggRW5sY7CCAHRaCjSBx6tGcm7fbPrZ9CB7EPc94"

# CELERY_TASK_SERIALIZER = 'json'
# BROKER_POOL_LIMIT = 1