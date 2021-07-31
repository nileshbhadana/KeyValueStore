import json
import random
import string
from os.path import exists
from resources.logger import createLogger

# File where the key-value pairs will be stored for persistence
file_path = "/app/store/KeyValue.json"

# Creating logger
LOGGER = createLogger()


class HelperFunction:
    """
    This class contains multiple helper functions.

    These functions are being used in operations.  
    """
    def __init__(self) -> None:
        """
        Constructor for Helper class.
        """
        pass
   
    def checkExistingKey(self, data, key):
        """
        This function checks if the KEY exists or not.
       
        Arguments:
            key: The key to check if exists or not. [String]

        Return:
            This functions returns True or False [Boolean]
        """
        if key in data.keys():
            LOGGER.info("Key: {} exists".format(key))
            return True
        else:
            return False

    def loaddata(self):
        """
        This function reads the file where the key pairs are stored
       
        Arguments:
            None

        Return:
            data: Dictionary containing all the key-value pairs [Dictionary]
        """

        data = {}
        if exists(file_path):
            try:
                with open(file_path) as file:
                    data = json.load(file)
            except Exception as error:
                LOGGER.error(error)
                raise SystemExit(error)
                
        else:
            data = {}

        return data

    def writetofile(self, data):
        """
        This function writes data to the storage file
       
        Arguments:
            data: Dictionary containing all the key-value pairs [Dictionary]

        Return:
            None
        """

        try:
            with open(file_path, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as error:
            LOGGER.error(error)


def generate_secret():
    """
    This function generates a random string of 10 characters
   
    Arguments:
        None

    Return:
        secret: String of 10 characters. [String]
    """  
    secret = ''.join(random.choice(string.ascii_letters) for i in range(10))
    return str(secret)
