from flask import Flask, render_template, jsonify
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from pymongo import MongoClient
import time
import json
import os
import pika
import urlparse

app = Flask(__name__)

from tasks import hello

CELERY_TASK_SERIALIZER = 'json'
BROKER_URL = os.environ.get('CLOUDAMQP_URL')



MONGOLAB_URI = os.environ.get('MONGOLAB_URI')

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



@app.route('/')
def index():
	# twitterStream = Stream(auth, listener())
	# twitterStream.filter(track=["#braves"])
	hello.delay()
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)




