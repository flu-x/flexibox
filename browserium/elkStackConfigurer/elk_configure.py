#!/usr/bin/env python
from browserium.utility.os_type import OS_type
from browserium.utility.utility import Utility
from subprocess import call

class elkConfigure(OS_type, Utility):

    @staticmethod
    def platform_type():
        platform_val = OS_type.os_name()
        return platform_val

    @staticmethod
    def configure_elkStack():
        os_cat = elkConfigure.platform_type()
        if os_cat == 'macos':
            elkConfigure.install_elkStack_forMac()

    @staticmethod
    def install_elkStack_forMac():
        call(["brew", "install", "elasticsearch"])
        call(["brew", "services", "start", "elasticsearch"])
        call(["brew", "install", "logstash"])
        call(["brew", "services", "start", "logstash"])
        call(["brew", "install", "kibana"])
        elkConfigure.configure_kibana()
        call(["brew", "services", "start", "kibana"])
        elkConfigure.install_logstashAsync()

    def install_elkStack_forLinux(self):
        pass

    @staticmethod
    def configure_kibana():
        file_path = Utility.get_path("elkStackConfigurer/kibana.yml")
        rectified_filePath = file_path.replace("utility/","")
        call(["cp", rectified_filePath, "/usr/local/etc/kibana/"])

    @staticmethod
    def install_logstashAsync():
        call(["pip", "install", "python-logstash-async"])

    @staticmethod
    def main():
        elkConfigure.configure_elkStack()

if __name__ == '__main__':
    elkConfigure.main()

