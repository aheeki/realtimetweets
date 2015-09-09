from flask import Flask, render_template, jsonify

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')

from tasks import hello

@app.route('/')
def index():
	hello.delay()
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
