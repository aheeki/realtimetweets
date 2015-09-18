from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)
# app.config.from_object('config')

from tasks import hello

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/track/<hashtag>')
def track(hashtag):
	# hello.delay()
	return render_template('index.html', hashtag=hashtag)

if __name__ == '__main__':
	app.run(debug=True)
