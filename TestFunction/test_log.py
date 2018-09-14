from browserium.generic_functions.chrome_object import ChromeDriverObject
from browserium.generic_functions.browser_controller import Browser_controller
from browserium.generic_functions.logger import Logstash
from time import sleep

class Test_1():
    def test_log_type1(self):
        log = Logstash()
        log.logstash_type("INFO","Test")
        log.logstash_type("ERROR","Test")
        log.logstash_type("WARNING","Test")

    def test_log_type2(self):
        log = Logstash()
        log.logstash_type("INFO","Test")
        log.logstash_type("ERROR","Test")
        log.logstash_type("WARNING","Test")

t = Test_1()
t.test_log_type1()
t.test_log_type2()