#!/usr/bin/env python
from browserium.utility.os_type import OS_type
from browserium.utility.utility import Utility
from subprocess import call

class elkConfigure(OS_type, Utility):
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
        os_cat = elkConfigure.platform_type()
        if os_cat == 'macos':
            elkConfigure.install_elkStack_forMac()
        if os_cat == 'linux':
            dist_type = OS_type.distribution_type()
            Utility.log_message("INFO","Dist type is: "+dist_type)
            if 'debian' in dist_type:
                elkConfigure.install_elkStack_forLinuxDebian()
            elif 'rhel fedora':
                elkConfigure.install_elkStack_forLinuxRPM()

    @staticmethod
    def install_elkStack_forMac():
        try:
            file_path = Utility.get_path("elkStackConfigurer/darwin/mac_installation.sh")
            rectified_filePath_forBash = file_path.replace("utility/","")
            call(["chmod", "+x", rectified_filePath_forBash])
            call(rectified_filePath_forBash)
            elkConfigure.configure_kibana_mac()
            call(["brew", "services", "restart", "kibana"])
            elkConfigure.install_logstashAsync()
            Utility.log_message("INFO", "Installing python module for logstash")
            elkConfigure.run_logstash_background()
        except OSError as e:
            Utility.log_message("ERROR", "File not found")
            print e

    @staticmethod
    def install_elkStack_forLinuxDebian():
        try:
            file_path = Utility.get_path("elkStackConfigurer/debian/debian_installation.sh")
            rectified_filePath_forBash = file_path.replace("utility/","")
            call(["chmod", "+x", rectified_filePath_forBash])
            call(rectified_filePath_forBash)
            elkConfigure.configure_kibana_mac()
            call(["sudo", "systemctl",  "restart", "kibana.service"])
            elkConfigure.install_logstashAsync()
            Utility.log_message("INFO", "Installing python module for logstash")
            elkConfigure.run_logstash_background()
        except OSError as e:
            Utility.log_message("ERROR", "File not found")
            print e

    @staticmethod
    def install_elkStack_forLinuxRPM():
        try:
            file_path = Utility.get_path("elkStackConfigurer/rpm/rpm_installation.sh")
            rectified_filePath_forBash = file_path.replace("utility/","")
            call(["chmod", "+x", rectified_filePath_forBash])
            call(rectified_filePath_forBash)
            elkConfigure.configure_kibana_mac()
            call(["sudo", "systemctl", "restart", "kibana.service"])
            elkConfigure.install_logstashAsync()
            Utility.log_message("INFO", "Installing python module for logstash")
            elkConfigure.run_logstash_background()
        except OSError as e:
            Utility.log_message("ERROR", "File not found")
            print e

    @staticmethod
    def configure_kibana_mac():
        file_path = Utility.get_path("elkStackConfigurer/darwin/kibana.yml")
        rectified_filePath_forYML = file_path.replace("utility","")
        dest_path = "/usr/local/etc/kibana/"
        call(["cp",rectified_filePath_forYML,dest_path])
        Utility.log_message("INFO", "kibana configuration file copied to /usr/local/etc/kibana")

    @staticmethod
    def configure_kibana_debian():
        file_path = Utility.get_path("elkStackConfigurer/debian/kibana.yml")
        rectified_filePath_forYML = file_path.replace("utility","")
        dest_path = "/usr/local/etc/kibana/"
        call(["cp",rectified_filePath_forYML,dest_path])
        Utility.log_message("INFO", "kibana configuration file copied to /usr/local/etc/kibana")

    @staticmethod
    def configure_kibana_rpm():
        file_path = Utility.get_path("elkStackConfigurer/rpm/kibana.yml")
        rectified_filePath_forYML = file_path.replace("utility","")
        dest_path = "/usr/local/etc/kibana/"
        call(["cp",rectified_filePath_forYML,dest_path])
        Utility.log_message("INFO", "kibana configuration file copied to /usr/local/etc/kibana")

    @staticmethod
    def install_logstashAsync():
        call(["pip", "install", "python-logstash"])

    @staticmethod
    def run_logstash_background():
        call(['nohup', 'logstash', '-f', 'logstash.conf', '&'])
        Utility.log_message("INFO", "Running logstash process in background")

    @staticmethod
    def main():
        elkConfigure.configure_elkStack()

if __name__ == '__main__':
    elkConfigure.main()