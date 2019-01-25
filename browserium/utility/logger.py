import logging
import logging.config

class Logger(object):
    def __init__(self):
        self.logger = self.configureLogger()

    def configureLogger(self):
        logging.config.fileConfig(fname='logging_config.ini', disable_existing_loggers=False)
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