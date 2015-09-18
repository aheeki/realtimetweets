from celery import Celery
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from pymongo import MongoClient
import json, os
from flask import current_app

celeryapp = Celery('tasks', broker=current_app.config['BROKER_URL'])

auth = OAuthHandler(current_app.config['CLIENT_KEY'], current_app.config['CLIENT_SECRET'])
auth.set_access_token(current_app.config['ACCESS_TOKEN'], current_app.config['ACCESS_SECRET'])


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
def hello():
	# print('hello')
	twitterStream = Stream(auth, listener())
	twitterStream.filter(track=["#trump"])