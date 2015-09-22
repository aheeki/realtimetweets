from flask import Flask, render_template, jsonify, request, session
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
	# add the hashtag
	if (hashtag[:1] != '#'):
		hashtag = '#' + hashtag
	result = hello.delay(hashtag)
	print('result task id', result.task_id)
	print('type of id',type(result.task_id))
	session['taskid'] = result.task_id
	print('session task id in track',session['taskid'])
	return 'track'

@app.route('/kill')
def kill():
	print('imhere')
	print('session task id in kill',session['taskid'])
	try:
		revoke(session['taskid'],terminate=True)
		print('revoked')
	except:
		print('didnt revoke')
	return 'kill'

if __name__ == '__main__':
	app.run(debug=True)
