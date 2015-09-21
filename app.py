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
	result = hello.delay(hashtag)
	print('HEREHEREHEREHERE')
	# print(printme)
	try:
		print('result', result)
	except:
		print('result didnt work')

	try:
		AsyncResult(result)
		print('asyncresult')
	except:
		print('asyncresult didnt work')

	try:
		AsyncResult(result).state
		print('asyncresultstate')
	except:
		print('asyncresultstate didnt work')

	try:
		revoke(result,terminate=True)
		print('revoking')
	except:
		print('revoking didnt work')
	return render_template('track.html', hashtag=hashtag)


@app.route('/status/<task_id>')
def taskstatus(task_id):
    task = long_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        # job did not start yet
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)


if __name__ == '__main__':
	app.run(debug=True)
