from celery import Celery

import tweetlistener

app = Celery()

@app.task
def hello():
	twitterStream = Stream(auth, listener())
	twitterStream.filter(track=["#braves"])