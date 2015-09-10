import os

CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
# BROKER_URL = 'amqp://rrQkadCQ:yaSEoyIJgavdJ64anAGlRZKJubS5_GSF@black-mallow-55.bigwig.lshift.net:10270/3WpDuxqTptQe'
BROKER_URL = os.environ.get('RABBITMQ_BIGWIG_URL','amqp://localhost:5672')
# BROKER_POOL_LIMIT = 1
# MONGO_URI = os.environ.get('MONGOLAB_URI','mongodb://localhost:27017/')
# CLIENT_KEY="iFxuEMWv8110vLIWWqA54w"
# CLIENT_SECRET="rC0cr1w0heC6swvuDTDIiE98ipNvH6WiEI62YzeC0k"
# ACCESS_TOKEN="991518511-9QlULoonEjUs5G3M7Mhc1m3iAQPISRqYtitXrmHh"
# ACCESS_SECRET="72ggRW5sY7CCAHRaCjSBx6tGcm7fbPrZ9CB7EPc94"