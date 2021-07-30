from resources.helpers import HelperFunction, LOGGER
from resources.stream import update

class KeyValueOperations():
    def __init__(self) -> None:
        pass

    def getValue(self,key):
        self.key = key 
        helper_obj=HelperFunction()
        self.data=helper_obj.loaddata()
        if helper_obj.checkExistingKey(self.data,self.key):
            return self.data[self.key]
        else:
            return "Key Does Not exists"

    def putKeyValue(self,key,value):
        self.key = key 
        self.value = value 

        helper_obj=HelperFunction()
        self.data=helper_obj.loaddata()

        if helper_obj.checkExistingKey(self.data,self.key):
            try:
                msg="Key: {} Updated with Value: {}".format(self.key,self.value)
                LOGGER.debug(msg)
                self.data[self.key]=self.value
                helper_obj.writetofile(self.data)
                update(msg)
                return msg
            except Exception as e:
                LOGGER.error(e)
                raise e
        else:
            try:
                msg="Key: {} Created with Value: {}".format(self.key,self.value)
                LOGGER.debug(msg)
                self.data[self.key]=self.value
                helper_obj.writetofile(self.data)
                update(msg)
                return msg
            except Exception as e:
                LOGGER.error(e)
                raise e
