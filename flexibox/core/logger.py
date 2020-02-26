# Author: @Corefinder
# Language: Python
# Copyrights: SoumyajitBasu
# Purpose: The purpose of the class Logger is to have all the generic functionality for logging
# Can be used to generate logs for all the required functions carried out in the project
import logging
from time import sleep

import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration


class Logger(object):
    sentry_logging = LoggingIntegration(level=logging.INFO, event_level=logging.ERROR)
    sentry_sdk.init(dsn="https://5b823e3b2d184f829b8ec52bfcd40a84@sentry.io/2944174", integrations=[sentry_logging])

    @classmethod
    def log_info(self, informationMessage):
        logging.info(informationMessage)
        sleep(2)

    @classmethod
    def log_error(self, errorMessage):
        logging.error(errorMessage)
        sleep(2)

    @classmethod
    def log_debug(self, debugMessage):
        logging.debug(debugMessage)
        sleep(2)

    @classmethod
    def log_warning(self, warningMessage):
        logging.warning(warningMessage)
        sleep(2)

    @classmethod
    def log_critical(self, criticalMessage):
        logging.critical(criticalMessage)
        sleep(2)
