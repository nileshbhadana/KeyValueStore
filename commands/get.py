import click, requests, os

def getFunc(key):
    HOST = os.getenv("HOST", "http://localhost:5000/")

    params = {
        'key': key
    }

    try:
        response = requests.get(HOST, params=params)
        return response.text
    except requests.exceptions.RequestException as error:
        raise SystemExit(error)

def getAllFunc():
    HOST = os.getenv("HOST", "http://localhost:5000/")
    HOST = HOST + "/all"

    try:
        response = requests.get(HOST)
        return response.text
    except requests.exceptions.RequestException as error:
        raise SystemExit(error)

@click.command()
@click.argument('key', required=False)
@click.option('--all', is_flag=True, help="Outputs all the Key Value pairs")
def get(key,all):
    """ 
    Get the value for a particular Key
    """
    if all:
        try:
            response = getAllFunc()
            click.echo(response)
        except Exception as error:
            raise SystemExit(error)        

    elif key:
        try:
            response = getFunc(key)
            click.echo(response)
        except Exception as error:
            raise SystemExit(error)

    else:
        msg="""
Usage: key-value get [OPTIONS] KEY
Try 'key-value get --help' for help.

Error: Missing argument 'KEY'
        """
        click.echo(msg)


