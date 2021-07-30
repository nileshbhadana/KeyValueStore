import json, random, string
from os.path import exists
from resources.logger import createLogger

file_path="/tmp/KeyValue.json"
LOGGER=createLogger()

class HelperFunction:
    def __init__(self) -> None:
        pass
    
    def checkExistingKey(self,data,key):
        if key in data.keys():
            LOGGER.debug("Key: {} exists".format(key))
            return True
        else:
            return False

    def loaddata(self):
        data={}
        if exists(file_path):
            try:
                with open(file_path) as file:
                    data = json.load(file)
            except Exception as e:
                LOGGER.debug(e)
        else:
            data={}

        return data

    def writetofile(self,data):
        try:
            file = open(file_path, "w")
            json.dump(data, file, indent = 4)
            file.close()
        except Exception as e:
            LOGGER.debug(e)


def generate_secret():
    secret = ''.join(random.choice(string.ascii_letters) for i in range(10))
    return str(secret)
