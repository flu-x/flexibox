from .chromedriver import Chromedriver
from .operadriver import Operadriver
from .geckodriver import Geckodriver
from .phantomjsdriver import Phantomjs_driver
from utility.utility import Utility
from .elkStackConfigurer.elk_configure import Elk_configure
class Driver(object):

    @staticmethod
    def get_driver(driver_name):
        return driver_class.get(driver_name)

driver_class = {
    'chromedriver': Chromedriver,
    'operadriver': Operadriver,
    'geckodriver': Geckodriver,
    'phantomjsdriver': Phantomjs_driver,
    'all': Utility,
    'elk_configure': Elk_configure
}