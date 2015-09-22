from flask import Flask, render_template, jsonify, request
import os
import celery
from celery.task.control import revoke
import time

app = Flask(__name__)
# app.config.from_object('config')

from tasks import hello
TASK = ''

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/track', methods=['GET'])
def track():
	hashtag = request.args.get('hashtag','')
	# add the hashtag
	if (hashtag[:1] != '#'):
		hashtag = '#' + hashtag
	TASK = hello.delay(hashtag)
	return 'track'

@app.route('/kill')
def kill():
	print('imhere')
	print('TASK',TASK)
	try:
		revoke(TASK.task_id,terminate=True)
		print('revoked')
	except:
		print('didnt revoke')
	return 'kill'

if __name__ == '__main__':
	app.run(debug=True)
