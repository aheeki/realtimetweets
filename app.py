from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)
# app.config.from_object('config')

from tasks import hello

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/track/<string:hashtag>')
def track(hashtag):
	# add the hashtag
	if (hashtag[:1] != '#'):
		hashtag = '#' + hashtag
	# hello.revoke()
	result = hello.delay(hashtag)
	return render_template('index.html', hashtag=hashtag)

if __name__ == '__main__':
	app.run(debug=True)
