import logging

class Logger(object):

    def log_info(self, informationMessage):
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
        logging.info(informationMessage)

    def log_error(self, errorMessage):
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.ERROR)
        logging.info(errorMessage)

    def log_debug(self, debugMessage):
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
        logging.info(debugMessage)

    def log_warning(self, warningMessage):
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.WARNING)
        logging.info(warningMessage)