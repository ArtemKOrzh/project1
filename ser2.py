from flask import flask
from flask import request
from flask import render_file
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
	return render_file('index.html')


@app.route('/', methods=['POST'])
def index_post():
	category = request.form.get('category')
	image = request.files.get('image')
	...


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5002', debug=True)
