from UnitTest.utility.utility import Utility
import unittest

class TestOpera(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.utility=Utility()

    def parseJSONOpera(self):
        dict_data = {}
        jsonData = self.utility.json_file_reader()
        for item in jsonData:
            dict_data = {
                "mac" : item['assets']['operadriver']['mac_v_64'],
                "linux" : item['assets']['operadriver']['linux_v_64']
            }
        return dict_data

    def testOperaDriverMac(self):
        driverAPI = self.parseJSONOpera()
        data = driverAPI.get('mac')
        print data

    def testOperaDriverLinux(self):
        driverAPI = self.parseJSONOpera()
        data = driverAPI.get('linux')
        print data