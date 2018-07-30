from utility import Utility
import json
import os

class BrowserConfiguration(Utility):
    def parse_json_data(self, browser_type, browser_options):
        try:
            json_path = self.get_path("json_builder/browser_objects.json")
            rectified_json_path = json_path.replace("utility/","")
            with open(rectified_json_path) as dataFile:
                json_data = json.loads(dataFile.read())
                for data in json_data[browser_type]:
                    print data[browser_options]
        except(ValueError, KeyError, TypeError) as e:
            self.log_message("ERROR", "There is an exception in the decoding of the json object")
            print e
        except IOError as e:
            self.log_message("ERROR", "File browser_objects.json not found")
            print e

    def chrome_configuration(self, *option_type):
        opt_list = list(option_type)
        for i in opt_list:
            self.parse_json_data("chrome",i)

    def firefox_configuration(self, *option_type):
        opt_list = list(option_type)
        for i in opt_list:
            self.parse_json_data("firefox",i)