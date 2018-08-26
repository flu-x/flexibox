from browserium.utility.os_type import OS_type
from browserium.utility.utility import Utility
from subprocess import call
import daemon
import os

class Elk_configure(OS_type, Utility):
    @staticmethod
    def get_path(path_param):
        try:
            requiredPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), path_param)
            return requiredPath
        except IOError as e:
            Utility.log_message("ERROR", "Required Directory / File not found")
            print e

    @staticmethod
    def evaluate_package_type_debian():
        pckg = OS_type.distribution_type()
        return pckg

    @staticmethod
    def platform_type():
        platform_val = OS_type.os_name()
        return platform_val

    @staticmethod
    def configure_elkStack():
        os_cat = Elk_configure.platform_type()
        if os_cat == 'macos':
            Elk_configure.install_elkStack_forMac()
        if os_cat == 'linux':
            OS_type.distribution_type()
            # print dist_type
            # Utility.log_message("INFO","Dist type is: "+str(dist_type))
            # if 'debian' in dist_type:
            #     Elk_configure.install_elkStack_forLinuxDebian()
            # elif 'rhel fedora':
            #     Elk_configure.install_elkStack_forLinuxRPM()

    @staticmethod
    def install_elkStack_forMac():
        try:
            file_path = Elk_configure.get_path("darwin/mac_installation.sh")
            call(["chmod", "+x", file_path])
            call(file_path)
            Elk_configure.configure_kibana_mac()
            call(["brew", "services", "restart", "kibana"])
            Elk_configure.install_logstashAsync()
            Utility.log_message("INFO", "Installed python module for logstash")
            # Elk_configure.run_logstash_background()
            Elk_configure.run_daemon()
        except OSError as e:
            Utility.log_message("ERROR", "File not found")
            print e

    @staticmethod
    def install_elkStack_forLinuxDebian():
        try:
            file_path = Elk_configure.get_path("debian/debian_installation.sh")
            call(["chmod", "+x", file_path])
            call("sudo", file_path)
            Elk_configure.configure_kibana_mac()
            call(["sudo", "systemctl",  "restart", "kibana.service"])
            Elk_configure.install_logstashAsync()
            Utility.log_message("INFO", "Installed python module for logstash")
            # Elk_configure.run_logstash_background()
            Elk_configure.run_daemon()
        except OSError as e:
            Utility.log_message("ERROR", "File not found")
            print e

    @staticmethod
    def install_elkStack_forLinuxRPM():
        try:
            file_path = Elk_configure.get_path("rpm/rpm_installation.sh")
            call(["chmod", "+x", file_path])
            call("sudo", file_path)
            Elk_configure.configure_kibana_mac()
            call(["sudo", "systemctl", "restart", "kibana.service"])
            Elk_configure.install_logstashAsync()
            Utility.log_message("INFO", "Installing python module for logstash")
            # Elk_configure.run_logstash_background()
            Elk_configure.run_daemon()
        except OSError as e:
            Utility.log_message("ERROR", "File not found")
            print e

    @staticmethod
    def configure_kibana_mac():
        try:
            file_path = Elk_configure.get_path("darwin/kibana.yml")
            rectified_filePath_forYML = file_path.replace("utility","")
            dest_path = "/usr/local/etc/kibana/"
            call(["cp",rectified_filePath_forYML,dest_path])
            Utility.log_message("INFO", "kibana configuration file copied to /usr/local/etc/kibana")
        except OSError as e:
            Utility.log_message("ERROR", "File not found")
            print e

    @staticmethod
    def configure_kibana_debian():
        try:
            file_path = Elk_configure.get_path("debian/kibana.yml")
            rectified_filePath_forYML = file_path.replace("utility","")
            dest_path = "/usr/local/etc/kibana/"
            call(["cp",rectified_filePath_forYML,dest_path])
            Utility.log_message("INFO", "kibana configuration file copied to /usr/local/etc/kibana")
        except OSError as e:
            Utility.log_message("ERROR", "File not found")
            print e

    @staticmethod
    def configure_kibana_rpm():
        try:
            file_path = Elk_configure.get_path("rpm/kibana.yml")
            rectified_filePath_forYML = file_path.replace("utility","")
            dest_path = "/usr/local/etc/kibana/"
            call(["cp",rectified_filePath_forYML,dest_path])
            Utility.log_message("INFO", "kibana configuration file copied to /usr/local/etc/kibana")
        except OSError as e:
            Utility.log_message("ERROR", "File not found")
            print e

    @staticmethod
    def install_logstashAsync():
        call(["pip", "install", "python-logstash"])

    @staticmethod
    def run_logstash_background():
        file_path = Elk_configure.get_path("logstash.conf")
        call(["logstash", "-f", file_path])
        Utility.log_message("INFO", "Running logstash configuration as a daemon process")

    @staticmethod
    def run_daemon():
        with daemon.DaemonContext():
            Elk_configure.run_logstash_background()

    @staticmethod
    def Elkmain():
        Elk_configure.configure_elkStack()