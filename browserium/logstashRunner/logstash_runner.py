from browserium.utility.os_type import OS_type
from browserium.utility.utility import Utility
from subprocess import call
import daemon
import os

class Logstash_runner():
    def __init__(self):
        self.ot = OS_type()
        self.ut = Utility()

    def get_path(self, path_param):
        try:
            requiredPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), path_param)
            return requiredPath
        except IOError as e:
            self.ut.log_message("ERROR", "Required Directory / File not found")
            print e

    @staticmethod
    def install_logstashAsync():
        call(["pip", "install", "python-logstash-async"])

    def run_logstash_background(self):
        file_path = self.get_path("logstash.conf")
        call(["logstash", "-f", file_path])

    def run_daemon(self):
        Logstash_runner.install_logstashAsync()
        Utility.log_message("INFO", "Running logstash configuration as a daemon process")
        with daemon.DaemonContext():
            self.run_logstash_background()

    def Elkmain(self):
        self.run_daemon()