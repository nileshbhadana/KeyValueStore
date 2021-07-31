import json
import socketio
from werkzeug.exceptions import BadRequestKeyError
from resources.operations import KeyValueOperations
from resources.stream import socket_server
from resources.helpers import generate_secret, HelperFunction
from flask import Flask, request


app = Flask(__name__)

# Adding socket to flask as WSGI App
app.wsgi_app = socketio.WSGIApp(socket_server, app.wsgi_app)

# Setting secret key
app.config['SECRET_KEY'] = generate_secret()


# Get Value request
@app.route('/', methods=['GET'])
def get():
    """
    This function return the value for provided key in the request args.
    """
    try:
        KVObj = KeyValueOperations()
        return KVObj.getValue(request.args['key'])
    except BadRequestKeyError:
        return "Error: Missing argument 'KEY'", 400


# Get All value request
@app.route('/all', methods=['GET'])
def get_all():
    """
    This function returns all the key value pairs stored.
    """
    try:
        return json.dumps(HelperFunction().loaddata(), sort_keys=True, indent=4)
    except Exception as error:
        return format(error), 502


# Put key value request
@app.route('/', methods=['PUT'])
def put():
    """
    This function creates/updates the key value pair provided.
    """
    try:
        KVObj = KeyValueOperations()
        data = json.loads(request.data)
        return KVObj.putKeyValue(data['key'], data['value'])
    except Exception as error:
        raise SystemExit(error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
