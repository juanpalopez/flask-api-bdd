import json
from flask import Flask, request
from flask.json import jsonify
from .views import USERS

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


@app.route('/users/<username>')
def get_user(username):
    user_details = USERS.get(username)
    if user_details:
        return jsonify(user_details)
    else:
        return not_found()


if __name__ == '__main__':
    app.run()
