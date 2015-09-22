from flask import Flask, render_template, jsonify, request
import os
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
	time.sleep(14)
	revoke(12345,terminate=True)
	print('HEREHEREHEREHERE')	
	return render_template('trackme.html', hashtag=hashtag)

@app.route('/kill')
def kill():
	print('imhere')
	revoke(12345,terminate=True)
	return render_template('trackme.html')

if __name__ == '__main__':
	app.run(debug=True)
