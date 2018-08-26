# Author: @Corefinder
# Language: Python
# Copyrights: SoumyajitBasu
# Purpose: The agenda for this documentation is to explain the utility for the class "OS_type".
# This class is used mainly to get the details of the respective environment based on your system.
# This information would help getting the required driver package or binaries based on your preferences.

import sys
import platform
import subprocess
import os
from browserium.utility.utility import Utility
from subprocess import call

class OS_type(Utility):
    LINUX = "linux"
    MAC = "macos"
    WIN = "windows"

    # Get the required OS name
    @staticmethod
    def os_name():
        pl = sys.platform
        if "linux" in pl:
            return OS_type.LINUX
        if pl == "darwin":
            return OS_type.MAC
        if pl == "windows":
            return OS_type.WIN

    # Get OS architecture type
    @staticmethod
    def os_architecture():
        arch = platform.machine()
        if arch.endswith('64'):
            return 64
        else:
            return 32

    # Get the required OS type
    @staticmethod
    def os_type():
        return OS_type.os_name() + str(OS_type.os_architecture)

    # Get platform distribution type
    @staticmethod
    def distribution_type():
        try:
            file_path = Utility.get_path("distType.sh")
            print file_path
            call(["chmod", "+x", file_path])
            print "check1"
            # id_like = subprocess.check_output("./%s" % file_path)
            cmd = "./%s" % file_path
            id_like = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT, env=os.environ, stdout=subprocess.PIPE, close_fds=True)
            print "check2"
            return str(id_like)
        except OSError as e:
            Utility.log_message("ERROR", "No such file or directory")
            print e