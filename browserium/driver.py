from browserium.core.utility import Utility
from browserium.standalonedriverobject.chromedriver import Chromedriver
from browserium.standalonedriverobject.geckodriver import Geckodriver
from browserium.standalonedriverobject.operadriver import Operadriver
from browserium.standalonedriverobject.phantomjsdriver import Phantomjs_driver


class Driver(object):
    @staticmethod
    def get_driver(driver_name):
        return driver_class.get(driver_name)


driver_class = {
    'chromedriver': Chromedriver,
    'operadriver': Operadriver,
    'geckodriver': Geckodriver,
    'phantomjsdriver': Phantomjs_driver,
    'all': Utility
}
