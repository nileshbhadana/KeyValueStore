import click
import socketio
import os

socket_client = socketio.Client()


@click.command()
def subscribe():
    """
    Subscribe for key-value updates
    """

    HOST = os.getenv("HOST", "http://localhost:5000/")

    socket_client.connect(HOST)
    socket_client.wait()


@socket_client.event
def connect():
    print('Connected')


@socket_client.event
def disconnect():
    print('Disconnected')


@socket_client.on('Update')
def my_broadcast_event(msg):
    print(msg)
