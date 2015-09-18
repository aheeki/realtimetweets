from celery import Celery
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from pymongo import MongoClient
import json, os
# from flask import current_app

BROKER_URL = os.environ.get('CLOUDAMQP_URL')
CELERY_TASK_SERIALIZER = 'json'
MONGOLAB_URI = os.environ.get('MONGOLAB_URI')

CLIENT_KEY="iFxuEMWv8110vLIWWqA54w"
CLIENT_SECRET="rC0cr1w0heC6swvuDTDIiE98ipNvH6WiEI62YzeC0k"
ACCESS_TOKEN="991518511-9QlULoonEjUs5G3M7Mhc1m3iAQPISRqYtitXrmHh"
ACCESS_SECRET="72ggRW5sY7CCAHRaCjSBx6tGcm7fbPrZ9CB7EPc94"

celeryapp = Celery('tasks', broker=BROKER_URL)

auth = OAuthHandler(CLIENT_KEY, CLIENT_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)


class listener(StreamListener):

	def on_data(self, data):
		# client = MongoClient('localhost', 27017)
		client = MongoClient(MONGOLAB_URI)
		db = client.get_default_database()
		# db = client['twitter_db']
		collection = db['twitter_collection']
		tweet = json.loads(data)

		collection.insert(tweet)

		return True

	def on_error(self, status):
		print status


@celeryapp.task
def hello(hashtag):
	# print('hello')
	twitterStream = Stream(auth, listener())
	twitterStream.filter(track=[hashtag])