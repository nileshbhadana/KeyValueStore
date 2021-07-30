import click, requests, json, os

def putFunc(key, value):
    HOST = os.getenv("HOST", "http://localhost:5000/")

    # Can be taken from ENV
    params = {
        'key': key,
        'value': value
    }
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