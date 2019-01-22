import logging
from logging.config import dictConfig

class Logger():
    def __init__(self):
        self.logger = self.configureLogger()

    def configureLogger(self):
        logger = logging.getLogger()
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger

    def log_info(self, informationMessage):
        self.logger.setLevel(logging.INFO)
        self.logger.info(informationMessage)

    def log_error(self, errorMessage):
        self.logger.setLevel(logging.ERROR)
        self.logger.error(errorMessage)

    def log_debug(self, debugMessage):
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug(debugMessage)

    def log_warning(self, warningMessage):
        self.logger.setLevel(logging.WARNING)
        self.logger.warn(warningMessage)