from celery import Celery

import tweetlistener

celery = Celery()

@celery.task
def hello():
	twitterStream = Stream(auth, listener())
	twitterStream.filter(track=["#braves"])