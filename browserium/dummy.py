from utility.browser_configuration import BrowserConfiguration
from elkStackConfigurer.elk_configure import elkConfigure

class Dummy(BrowserConfiguration, elkConfigure):
    def check_func(self):
    #     self.chrome_configuration("disable_extension","ignore_certificate_errors","sandbox")
    #     self.firefox_configuration("headless","accept_untrusted_certs","private_browsing","disable_popup_blocking")
        self.manipulate_userData()

d = Dummy()
d.check_func()