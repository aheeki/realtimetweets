from celery import Celery
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from pymongo import MongoClient
import time
import json

import app
import tweetlistener

app = Celery()

@app.task
def hello():
	twitterStream = Stream(auth, listener())
	twitterStream.filter(track=["#braves"])