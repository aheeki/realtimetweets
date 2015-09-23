from flask import Flask, render_template, jsonify, request
import os
import celery
from celery.task.control import revoke

app = Flask(__name__)
# app.config.from_object('config')

from tasks import hello

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/isrunning')
def isrunning():
	try:
		res = hello.AsyncResult('this-id-does-not-exist')
		print('res = app.AsyncResult in isrunning')
	except:
		print('result.id doesnt work')
	try:
		print('res.state in isrunning', res.state)
	except:
		print('result.state doesnt work')
	try:
		print('res.id in isrunning', res.id)
	except:
		print('result.id doesnt work')
	try:
		print('res.tasks in isrunning', res.tasks)
	except:
		print('result.tasks doesnt work')	

	return True

@app.route('/track', methods=['GET'])
def track():
	hashtag = request.args.get('hashtag','')
	# add the hashtag syntax
	if (hashtag[:1] != '#'):
		hashtag = '#' + hashtag
	result = hello.delay(hashtag)
	try:
		print('result.tasks', result.tasks)
	except:
		print('result.tasks doesnt work')
	try:
		print('inspect', inspect())
	except:
		print('inspect didnt work')

	return 'running task ' + result.id

@app.route('/kill', methods=['GET'])
def kill():
	taskid = request.args.get('taskid','')
	revoke(taskid,terminate=True)
	return 'killed task ' + taskid

if __name__ == '__main__':
	app.run(debug=True)
