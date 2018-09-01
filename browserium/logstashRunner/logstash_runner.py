from browserium.utility.os_type import OS_type
from browserium.utility.utility import Utility
from subprocess import call
import daemon
import os

class Logstash_runner(OS_type, Utility):
    @staticmethod
    def get_path(path_param):
        try:
            requiredPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), path_param)
            return requiredPath
        except IOError as e:
            Utility.log_message("ERROR", "Required Directory / File not found")
            print e

    @staticmethod
    def install_logstashAsync():
        call(["pip", "install", "python-logstash"])

    @staticmethod
    def run_logstash_background():
        file_path = Logstash_runner.get_path("logstash.conf")
        call(["logstash", "-f", file_path])

    @staticmethod
    def run_daemon():
        Logstash_runner.install_logstashAsync()
        Utility.log_message("INFO", "Running logstash configuration as a daemon process")
        with daemon.DaemonContext():
            Logstash_runner.run_logstash_background()

    @staticmethod
    def Elkmain():
        Logstash_runner.run_daemon()