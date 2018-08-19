from browserium.utility.os_type import OS_type
from browserium.utility.utility import Utility
from subprocess import call

class Elk_configure(OS_type, Utility):
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
            dist_type = OS_type.distribution_type()
            Utility.log_message("INFO","Dist type is: "+dist_type)
            if 'debian' in dist_type:
                Elk_configure.install_elkStack_forLinuxDebian()
            elif 'rhel fedora':
                Elk_configure.install_elkStack_forLinuxRPM()

    @staticmethod
    def install_elkStack_forMac():
        try:
            file_path = Utility.get_path("elkStackConfigurer/darwin/mac_installation.sh")
            rectified_filePath_forBash = file_path.replace("utility/","")
            call(["chmod", "+x", rectified_filePath_forBash])
            call(rectified_filePath_forBash)
            Elk_configure.configure_kibana_mac()
            call(["brew", "services", "restart", "kibana"])
            Elk_configure.install_logstashAsync()
            Utility.log_message("INFO", "Installing python module for logstash")
            Elk_configure.run_logstash_background()
        except OSError as e:
            Utility.log_message("ERROR", "File not found")
            print e

    @staticmethod
    def install_elkStack_forLinuxDebian():
        try:
            file_path = Utility.get_path("elkStackConfigurer/debian/debian_installation.sh")
            rectified_filePath_forBash = file_path.replace("utility/","")
            call(["chmod", "+x", rectified_filePath_forBash])
            call("sudo", rectified_filePath_forBash)
            Elk_configure.configure_kibana_mac()
            call(["sudo", "systemctl",  "restart", "kibana.service"])
            Elk_configure.install_logstashAsync()
            Utility.log_message("INFO", "Installing python module for logstash")
            Elk_configure.run_logstash_background()
        except OSError as e:
            Utility.log_message("ERROR", "File not found")
            print e

    @staticmethod
    def install_elkStack_forLinuxRPM():
        try:
            file_path = Utility.get_path("elkStackConfigurer/rpm/rpm_installation.sh")
            rectified_filePath_forBash = file_path.replace("utility/","")
            call(["chmod", "+x", rectified_filePath_forBash])
            call("sudo", rectified_filePath_forBash)
            Elk_configure.configure_kibana_mac()
            call(["sudo", "systemctl", "restart", "kibana.service"])
            Elk_configure.install_logstashAsync()
            Utility.log_message("INFO", "Installing python module for logstash")
            Elk_configure.run_logstash_background()
        except OSError as e:
            Utility.log_message("ERROR", "File not found")
            print e

    @staticmethod
    def configure_kibana_mac():
        try:
            file_path = Utility.get_path("elkStackConfigurer/darwin/kibana.yml")
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
            file_path = Utility.get_path("elkStackConfigurer/debian/kibana.yml")
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
            file_path = Utility.get_path("elkStackConfigurer/rpm/kibana.yml")
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
        call(['nohup', 'logstash', '-f', 'logstash.conf', '&'])
        Utility.log_message("INFO", "Running logstash process in background")

    @staticmethod
    def Elkmain():
        Elk_configure.configure_elkStack()