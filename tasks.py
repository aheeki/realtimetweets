from celery import Celery
# from tweepy import Stream
# import tweetlistener

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from pymongo import MongoClient
import time
import json

import os
BROKER_URL = os.environ.get('CLOUDAMQP_URL')


app = Celery('tasks', broker=BROKER_URL)


ckey="iFxuEMWv8110vLIWWqA54w"
csecret="rC0cr1w0heC6swvuDTDIiE98ipNvH6WiEI62YzeC0k"
atoken="991518511-9QlULoonEjUs5G3M7Mhc1m3iAQPISRqYtitXrmHh"
asecret="72ggRW5sY7CCAHRaCjSBx6tGcm7fbPrZ9CB7EPc94"

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)




# app.config_from_object('config')


@app.task
def hello():
	# print('hello')
	twitterStream = Stream(auth, listener())
	twitterStream.filter(track=["#braves"])