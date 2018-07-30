from browserium.utility.os_type import OS_type
from browserium.utility.utility import Utility
from subprocess import call

class elkConfigure(OS_type, Utility):

    def platform_type(self):
        platform_val = self.os_name()
        return platform_val

    @staticmethod
    def input_user_data():
        print "Would you like to configure elk stack for logging preferences? (Y/N):"
        user_choice = raw_input()
        return user_choice

    def manipulate_userData(self):
        user_choice = self.input_user_data().lower()
        if user_choice == "y" or user_choice == "yes":
            self.configure_elkStack()
        else:
            pass

    def configure_elkStack(self):
        os_cat = self.platform_type()
        if os_cat == 'macos':
            self.install_elkStack_forMac()

    def install_elkStack_forMac(self):
        call(["brew", "install", "elasticsearch"])
        call(["brew", "services", "start", "elasticsearch"])
        call(["brew", "install", "logstash"])
        call(["brew", "services", "start", "logstash"])
        call(["brew", "install", "kibana"])
        self.configure_kibana()
        call(["brew", "services", "start", "kibana"])
        self.install_logstashAsync()

    def install_elkStack_forLinux(self):
        pass

    def configure_kibana(self):
        file_path = self.get_path("elkStackConfigurer/kibana.yml")
        rectified_filePath = file_path.replace("utility/","")
        call(["cp", "-f", rectified_filePath, "/usr/local/etc/kibana/"])

    def install_logstashAsync(self):
        call(["pip", "install", "python-logstash-sync"])