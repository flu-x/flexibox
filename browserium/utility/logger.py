import logging
import logging.config
import os

class Logger(object):
    def __init__(self):
        self.logger = self.configureLogger()

    def configureLogger(self):
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../browserium/configurations/logging_config.ini')
        logging.config.fileConfig(fname=path, disable_existing_loggers=False)
        rootLogger = logging.getLogger(__name__)
        return rootLogger

    def log_info(self, informationMessage):
        self.logger.info(informationMessage)

    def log_error(self, errorMessage):
        self.logger.error(errorMessage)

    def log_debug(self, debugMessage):
        self.logger.debug(debugMessage)

    def log_warning(self, warningMessage):
        self.logger.warn(warningMessage)