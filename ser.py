from flask import flask
from flask import request
from flask import render_file
import requests

app = Flask(__name__)


@app.route('/')
def index():
	if request.form.get('secret'):
		category = request.form.get('category')
		image = request.files.get('image')
		...
		return jsonify(dict(success=1))
	return render_file('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
