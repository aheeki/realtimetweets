from flask import Flask, render_template, jsonify, request
from celery.task.control import revoke
import os

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
	print('HEREHEREHEREHERE')
	# print(printme)
	try:
		print('result', result)
	except:
		print('result didnt work')

	try:
		print('asyncresult',AsyncResult(result))
	except:
		print('asyncresult didnt work')
	try:
		print('asyncresultstate',AsyncResult(result).state)
	except:
		print('asyncresultstate didnt work')
	try:
		print('revoking',revoke(result,terminate=True))
	except:
		print('revoking didnt work')
	revoke(result,terminate=True)

	return render_template('track.html', hashtag=hashtag)


if __name__ == '__main__':
	app.run(debug=True)
