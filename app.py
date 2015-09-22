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

@app.route('/track', methods=['GET'])
def track():
	hashtag = request.args.get('hashtag','')
	# add the hashtag
	if (hashtag[:1] != '#'):
		hashtag = '#' + hashtag
	result = hello.delay(hashtag)
	try:
		print result.task_id
	except:
		print('no result task id')
	try:
		print result.status
	except:
		print('no result status')
	try:
		print result.result
	except:
		print('no result.result')
	return 'track'

@app.route('/kill')
def kill():
	print('imhere')
	try:
		revoke(12345,terminate=True)
		print('revoked')
	except:
		print('didnt revoke')
	return 'kill'

if __name__ == '__main__':
	app.run(debug=True)
