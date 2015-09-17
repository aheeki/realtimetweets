from celery import Celery
# from tweepy import Stream
# import tweetlistener

app = Celery('tasks', broker=BROKER_URL)

# app.config_from_object('config')


@app.task
def hello():
	# print('hello')
	twitterStream = Stream(auth, listener())
	twitterStream.filter(track=["#braves"])