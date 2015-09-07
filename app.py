from flask import Flask, render_template, jsonify
from tasks import hello

app = Flask(__name__)

@app.route('/')
def index():
	hello.delay()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)