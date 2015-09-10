from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from pymongo import MongoClient
import time
import json

class listener(StreamListener):
	def __init__(self):
		auth = OAuthHandler(CLIENT_KEY, CLIENT_SECRET)
		auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

	def on_data(self, data):
		client = MongoClient(MONGO_URI)
		# db = client['twitter_db']
		db = client['heroku_1dvlnxd7']
		collection = db['twitter_collection']
		tweet = json.loads(data)
		collection.insert(tweet)
		return True

	def on_error(self, status):
		print status