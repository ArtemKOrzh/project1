from flask import flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route('/api/save-image/')
def add_data_handler():
	if request.form.get('secret'):
		category = request.form.get('category')
		image = request.files.get('image')
		...
		return jsonify(dict(success=1))

	return jsonify(dict(success=0))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', debug=True)
