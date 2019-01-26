from browserium.utility.logger import Logger

class Loggerobject(object):

    def __init__(self):
        self.log = Logger()

    def logInformation(self, info):
        self.log.log_info(info)

    def logError(self, error):
        self.log.log_error(error)

    def logWarning(self, warning):
        self.log.log_warning(warning)

    def logDebug(self, debug):
        self.log.log_debug(debug)

    def logCritical(self, critical):
        self.log.log_critical(critical)