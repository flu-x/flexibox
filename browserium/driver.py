from .chromedriver import Chromedriver
from .operadriver import Operadriver
from .geckodriver import Geckodriver
from browserium.utility.utility import Utility
class Driver(object):

    @staticmethod
    def get_driver(driver_name):
        return driver_class.get(driver_name)

driver_class = {
    'chromedriver': Chromedriver,
    'operadriver': Operadriver,
    'geckodriver': Geckodriver,
    'all': Utility
}