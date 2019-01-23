import os
import logging
from logging.config import dictConfig

class Logger(object):
    def __init__(self):
        path = os.path.dirname(os.path.abspath(__file__))
        self.logger = self.configureLogger(path)

    def configureLogger(self, filePath):
        rootLogger = logging.getLogger()
        logFormatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logFormatter)
        rootLogger.addHandler(consoleHandler)
        rootLogger.setLevel(logging.DEBUG)

        fileHandler = logging.FileHandler("{0}/{1}.log".format(filePath, "Logger"))
        fileHandler.setFormatter(logFormatter)
        rootLogger.addHandler(fileHandler)
        rootLogger.setLevel(logging.DEBUG)

        return rootLogger

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