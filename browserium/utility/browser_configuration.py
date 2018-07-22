from browserium.utility.utility import Utility
import json

class BrowserConfiguration(Utility):
    def parse_json_data(self, browser_type, argument_type):
        try:
            json_path = self.get_path('../json_builder/browser_objects.json')
            print json_path
            # with open(json_path) as data_file:
            #     decoded_json = json.loads(data_file)
            #     print "2"
            #     for x in decoded_json[browser_type]:
            #         print "3"
            #         print "\n" + x[argument_type]
        except(ValueError, KeyError, TypeError) as e:
            self.log_message("ERROR", "There is an exception in the decoding of the json object")
            print e
        except IOError as e:
            self.log_message("ERROR", "File browser_objects.json not found")
            print e
    def chrome_configuration(self, option_type):
        self.parse_json_data("chrome", option_type)