import logging

class Logger(object):

    @classmethod
    def log_info(self, informationMessage):
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
        logging.info(informationMessage)

    @classmethod
    def log_error(self, errorMessage):
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.ERROR)
        logging.error(errorMessage)

    @classmethod
    def log_debug(self, debugMessage):
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
        logging.debug(debugMessage)

    @classmethod
    def log_warning(self, warningMessage):
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.WARNING)
        logging.warning(warningMessage)

    @classmethod
    def log_critical(self, criticalMessage):
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.CRITICAL)
        logging.critical(criticalMessage)