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



# app.config_from_object('config')


@app.task
def hello():
	# print('hello')
	twitterStream = Stream(auth, listener())
	twitterStream.filter(track=["#braves"])