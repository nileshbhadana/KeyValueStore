import sys
import logging

def createLogger():
    """
    Function to create a Logger for logging.
    """
    stdout_handler = logging.StreamHandler(sys.stdout)
    handlers = [stdout_handler]

    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
        handlers=handlers
    )
    LOGGER = logging.getLogger('LOGGER_NAME')
    LOGGER.setLevel(logging.DEBUG)

    return LOGGER