import requests
import json
import os
import click

def putFunc(key, value):
    """
    This function makes PUT request to server to create/update Key value pairs.

    Arguments:
        key: The key for which value to be set. [String]
        value: The value to be set. [String]

    Return:
        msg: The message about the update or create operation. [String]
    """     
    HOST = os.getenv("HOST", "http://localhost:5000/")

    params = {
        'key': key,
        'value': value
    }

    # Setting headers for the request.
    Headers = {'Content-type': 'application/json'}
    try:
        response = requests.put(HOST, data=json.dumps(params), headers=Headers)
        return response.text
    except requests.exceptions.RequestException as error:
        raise SystemExit(error)


@click.command()
@click.argument('key')
@click.argument('value')
def put(key, value):
    """
    Create / Update Key with Value
    """
    response = putFunc(key, value)
    click.echo(response)
