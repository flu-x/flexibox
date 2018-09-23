from .chromedriver import Chromedriver
from .operadriver import Operadriver
from .geckodriver import Geckodriver
from utility.utility import Utility
from .logstashRunner.logstash_runner import Logstash_runner
class Driver(object):

    @staticmethod
    def get_driver(driver_name):
        return driver_class.get(driver_name)

driver_class = {
    'chromedriver': Chromedriver,
    'operadriver': Operadriver,
    'geckodriver': Geckodriver,
    'all': Utility,
    'logstash_build': Logstash_runner
}