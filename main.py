import socketio, json
from resources.operations import KeyValueOperations
from resources.stream import socket_server
from resources.helpers import generate_secret, HelperFunction
from flask import Flask, request

app = Flask(__name__)

app.wsgi_app = socketio.WSGIApp(socket_server, app.wsgi_app)
app.config['SECRET_KEY'] = generate_secret()


@app.route('/', methods=['GET'])
def get():
    KVObj=KeyValueOperations()
    return KVObj.getValue(request.args['key'])

@app.route('/all', methods=['GET'])
def get_all():
    return json.dumps(HelperFunction().loaddata(), sort_keys=True, indent=4)

@app.route('/', methods=['PUT'])
def put():
    KVObj=KeyValueOperations()
    data=json.loads(request.data)
    return KVObj.putKeyValue(data['key'],data['value'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)