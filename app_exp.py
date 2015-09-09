from flask import Flask, render_template, jsonify
from celery import Celery
import os

app = Flask(__name__)
celery = Celery()

CELERY_TASK_SERIALIZER = 'json'
BROKER_URL = os.environ.get('RABBITMQ_BIGWIG_URL','amqp://localhost:5672')
BROKER_POOL_LIMIT = 1
MONGO_URI = os.environ.get('MONGOLAB_URI','mongodb://localhost:27017/')
CLIENT_KEY="iFxuEMWv8110vLIWWqA54w"
CLIENT_SECRET="rC0cr1w0heC6swvuDTDIiE98ipNvH6WiEI62YzeC0k"
ACCESS_TOKEN="991518511-9QlULoonEjUs5G3M7Mhc1m3iAQPISRqYtitXrmHh"
ACCESS_SECRET="72ggRW5sY7CCAHRaCjSBx6tGcm7fbPrZ9CB7EPc94"

from tasks import hello

@app.route('/')
def index():
	hello.delay()
	return render_template('index.html')

@celery.task
def hello():
	twitterStream = Stream(auth, listener())
	twitterStream.filter(track=["#braves"])

if __name__ == '__main__':
	app.run(debug=True)
