from flask import Flask, render_template, jsonify, request
import os
import celery
from celery.task.control import revoke
import time

app = Flask(__name__)
# app.config.from_object('config')

from tasks import hello

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/track', methods=['GET'])
def track():
	hashtag = request.args.get('hashtag','')
	# add the hashtag syntax
	if (hashtag[:1] != '#'):
		hashtag = '#' + hashtag
	result = hello.delay(hashtag)
	return result.task_id

@app.route('/kill', methods=['GET'])
def kill():
	taskid = request.args.get('taskid','')
	return revoke(taskid,terminate=True)

if __name__ == '__main__':
	app.run(debug=True)
