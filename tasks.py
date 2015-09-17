from celery import Celery
# from tweepy import Stream
# import tweetlistener

import os

app = Celery('tasks', broker=BROKER_URL)

BROKER_URL = os.environ.get('CLOUDAMQP_URL')


# app.config_from_object('config')


@app.task
def hello():
	# print('hello')
	twitterStream = Stream(auth, listener())
	twitterStream.filter(track=["#braves"])