import socketio
from resources.helpers import LOGGER

async_mode='threading'

socket_server = socketio.Server(logger=True, async_mode=async_mode)


@socket_server.event
def update(msg):
    try:
        socket_server.emit('Update',msg)
    except Exception as error:
        LOGGER.error("Error while broadcasting {}".format(error))


@socket_server.event
def connect(sid, test):
    """
    The function to establish a connection.
    """
    try:
        socket_server.emit('connected', {'data': 'Connected'}, room=sid)
    except socketio.exceptions.ConnectionError as error:
        LOGGER.error("Connection Failed {}".format(error))


@socket_server.event
def disconnect(sid):
    """
    The function is called when a client disconnects
    """
    LOGGER.info('Client Disconnected')