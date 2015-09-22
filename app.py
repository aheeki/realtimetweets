from flask import Flask, render_template, jsonify, request
import os
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
	return 'track'

@app.route('/kill')
def kill():
	print('imhere')
	revoke(12345,terminate=True)
	return 'kill'

if __name__ == '__main__':
	app.run(debug=True)
