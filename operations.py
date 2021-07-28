#from helpers import HelperFunction
from flask import helpers
from flask_restful import Resource, reqparse
from helpers import HelperFunction
from logger import createLogger


LOGGER=createLogger()

class KeyValueOperations(Resource):
    def __init__(self) -> None:
        self.req_args = reqparse.RequestParser()
        self.req_args.add_argument('key', type=str, required=True)
        self.req_args.add_argument('value', type=str)

    def getValue(self,key):
        self.key=key
        self.data=HelperFunction.loaddata()
        helper_obj=HelperFunction()
        LOGGER.info(self.key)
        if helper_obj.checkExistingKey(self.data,self.key):
            return self.data[self.key]
        else:
            return "Key Does Not exists"

    def putKeyValue(self,key,value):
        self.key=key
        self.value=value
        self.data=HelperFunction.loaddata()
        helper_obj=HelperFunction()        
        if helper_obj.checkExistingKey(self.data,self.key):
            try:
                LOGGER.debug("Key: {} updated with value {}".format(self.key,self.value))
                self.data[self.key]=self.value
                HelperFunction.writetofile(self.data)
                return "Key: {} updated with value {}".format(self.key,self.value)
            except Exception as e:
                LOGGER.error(e)
                raise e
        else:
            try:
                LOGGER.debug("Key: {} created with value {}".format(self.key,self.value))
                self.data[self.key]=self.value
                HelperFunction.writetofile(self.data)
                return "Key: {} created with value {}".format(self.key,self.value)
            except Exception as e:
                LOGGER.error(e)
                raise e
