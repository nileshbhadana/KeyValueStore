import click, requests, os

def getFunc(key):
    """
    This function makes GET request to the Flask server to get value for a particular key
    Arguments:
        key: The key for which value is required [String]

    Return:
        value: The value for provided key [String]
    """
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
    """
    This function makes GET request to the Flask server to get all the Key-value pairs stored.
    Arguments:
        None

    Return:
        data: All the key value pairs. [Dictionary]
    """    
    HOST = os.getenv("HOST", "http://localhost:5000/")
    HOST = HOST + "/all"

    try:
        response = requests.get(HOST)
        return response.text
    except requests.exceptions.RequestException as error:
        raise SystemExit(error)

@click.command()
@click.argument('key', required=False)
@click.option('--all', is_flag=True, help="Outputs all the Key Value pairs stored")
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


