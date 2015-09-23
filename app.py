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
	print('result task id', result.task_id)
	print('type of id',type(result.task_id))
	taskid = result.task_id
	print('task id in track',taskid)
	return result.task_id

@app.route('/kill', methods=['GET'])
def kill():
	taskid = request.args.get('taskid','')
	print('imhere')
	print('task id in kill',taskid)
	try:
		revoke(taskid,terminate=True)
		print('revoked')
	except:
		print('didnt revoke')
	return 'killed ' + taskid

if __name__ == '__main__':
	app.run(debug=True)
