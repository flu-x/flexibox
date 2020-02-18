# Author: @Corefinder
# Language: Python
# Copyrights: SoumyajitBasu
# Purpose: Factory class generator
from flexibox.core.utility import Utility
from flexibox.standalonedriverobject.chromedriver import Chromedriver
from flexibox.standalonedriverobject.geckodriver import Geckodriver
from flexibox.standalonedriverobject.operadriver import Operadriver
from flexibox.standalonedriverobject.phantomjsdriver import Phantomjs_driver


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
