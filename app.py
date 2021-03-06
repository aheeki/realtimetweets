from flask import Flask, render_template, jsonify, request, session
import os
import celery
from celery.task.control import revoke

app = Flask(__name__)
# app.config.from_object('config')

from tasks import hello
#test

SECRET_KEY = os.environ.get('SECRET_KEY')


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
		session['isrunning'] = 'hitest'
		print(session['isrunning'])
		print('saved session in isrunning')
	except:
		print('saved session in isrunning didnt save')
	try:
		print('res.id in isrunning', res.id)
	except:
		print('result.id doesnt work')
	try:
		print('res.tasks in isrunning', res.tasks)
	except:
		print('result.tasks doesnt work')	

	return app.config['ISRUNNING']

@app.route('/track', methods=['GET'])
def track():
	hashtag = request.args.get('hashtag','')
	# add the hashtag syntax
	if (hashtag[:1] != '#'):
		hashtag = '#' + hashtag
	try:
		result = hello.delay(hashtag)
		app.config['ISRUNNING'] = True
	except:
		print('could not start hello.delay()')
	try:
		print('async')
	except:
		print('result.tasks doesnt work')
	try:
		print('async')
	except:
		print('result.tasks doesnt work')
	try:
		print('request', hello.request)
	except:
		print('backend didnt work')

	return 'running task ' + result.id

@app.route('/kill', methods=['GET'])
def kill():
	taskid = request.args.get('taskid','')
	revoke(taskid,terminate=True)
	app.config['ISRUNNING'] = False
	return 'killed task ' + taskid

if __name__ == '__main__':
	app.secret_key = 'lasdkljflaskdj23uh23iu23iu23u32iu3hi23uif'
	app.run(debug=True)
