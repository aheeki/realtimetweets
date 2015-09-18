from celery import Celery
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from pymongo import MongoClient
import json, os

app = Celery('tasks', broker=BROKER_URL)
app.config_from_object('config')


ckey="iFxuEMWv8110vLIWWqA54w"
csecret="rC0cr1w0heC6swvuDTDIiE98ipNvH6WiEI62YzeC0k"
atoken="991518511-9QlULoonEjUs5G3M7Mhc1m3iAQPISRqYtitXrmHh"
asecret="72ggRW5sY7CCAHRaCjSBx6tGcm7fbPrZ9CB7EPc94"

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)


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


@app.task
def hello():
	# print('hello')
	twitterStream = Stream(auth, listener())
	twitterStream.filter(track=["#trump"])