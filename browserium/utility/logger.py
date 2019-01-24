import os
import logging

class Logger(object):
    def __init__(self):
        self.logger = self.configureLogger()

    def configureLogger(self):
        rootLogger = logging.getLogger()
        logFormatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logFormatter)
        rootLogger.addHandler(consoleHandler)
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