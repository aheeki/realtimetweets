from flask import Flask, render_template, jsonify, request
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
	# hello.revoke()
	hello.delay(hashtag)
	return render_template('track.html', hashtag=hashtag)

if __name__ == '__main__':
	app.run(debug=True)
