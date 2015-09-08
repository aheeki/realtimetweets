import os

class BaseConfig(object):
	CELERY_TASK_SERIALIZER = 'json'
	BROKER_URL = os.environ.get('RABBITMQ_BIGWIG_URL','amqp://localhost:5672')
	MONGO_URI = os.environ.get('MONGOLAB_URI','mongodb://localhost:27017/')
	CLIENT_KEY="iFxuEMWv8110vLIWWqA54w"
	CLIENT_SECRET="rC0cr1w0heC6swvuDTDIiE98ipNvH6WiEI62YzeC0k"
	ACCESS_TOKEN="991518511-9QlULoonEjUs5G3M7Mhc1m3iAQPISRqYtitXrmHh"
	ACCESS_SECRET="72ggRW5sY7CCAHRaCjSBx6tGcm7fbPrZ9CB7EPc94"

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False