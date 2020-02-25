# Author: @Corefinder
# Language: Python
# Copyrights: SoumyajitBasu
# Purpose: The purpose of the class Logger is to have all the generic functionality for logging
# Can be used to generate logs for all the required functions carried out in the project
import logging

import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration

sentry_logging = LoggingIntegration(level=logging.INFO, event_level=logging.ERROR, logging.INFO)
sentry_sdk.init(dsn="https://bc26766d1b0c464f80a60d18394c1585@sentry.io/2844244", integrations=[sentry_logging])


class Logger(object):
    @classmethod
    def log_info(self, informationMessage):
        logging.info(informationMessage)

    @classmethod
    def log_error(self, errorMessage):
        logging.error(errorMessage)

    @classmethod
    def log_debug(self, debugMessage):
        logging.debug(debugMessage)

    @classmethod
    def log_warning(self, warningMessage):
        logging.warning(warningMessage)

    @classmethod
    def log_critical(self, criticalMessage):
        logging.critical(criticalMessage)
