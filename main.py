from operations import KeyValueOperations
import json
from flask_restful import Api
from flask import request
import flask
from logger import createLogger

LOGGER=createLogger()

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api', methods=['GET'])
def get():
    KVObj=KeyValueOperations()
    LOGGER.info("GET REQUEST")
    return KVObj.getValue(request.args['key'])

@app.route('/api', methods=['PUT'])
def put():
    KVObj=KeyValueOperations()
    data=json.loads(request.data.decode('utf8').replace("=", ':'))
    LOGGER.info("PUT REQUEST")
    return KVObj.putKeyValue(data['key'],data['value'])

app.run()