from resources.helpers import HelperFunction, LOGGER
from resources.stream import update


class KeyValueOperations():
    """
    This class returns the values and update keys.

    This class contains geValue() and putKeyValue() functions. 
    getValue() function returns the value of provided Key.
    putKeyValue() function creates/updates the provide key value pair.
    """  
    def __init__(self) -> None:
        """
        Contructor for KeyValueOperations class.
        """
        pass

    def getValue(self,key):
        """
        Function to get the value for provided key

        Arguments:
            key: The key for which value to be returned [String]

        Return:
            value: The value for provided key [String]
        """
        self.key = key 
        helper_obj=HelperFunction()

        # Loading data from the storage file.
        self.data=helper_obj.loaddata()

        # Check if key exists, return value if true otherwise return message
        if helper_obj.checkExistingKey(self.data,self.key):
            return self.data[self.key]
        else:
            # Return 401 status code if key does not exists
            return "Key Does Not exists", 404


    def putKeyValue(self,key,value):
        """
        Function to put the value for provided key

        Arguments:
            key: The key for which value to be set. [String]
            value: The value to be set. [String]

        Return:
            msg: The message about the update or create operation. [String]
        """        
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
