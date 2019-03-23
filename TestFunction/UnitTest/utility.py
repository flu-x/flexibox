# Author: @Corefinder
# Language: Python
# Copyrights: SoumyajitBasu
# Purpose: The purpose of the class Utility is to consist of the generic functions that
# can be used across all the functionalities that would be developed in this project

from datetime import datetime
import json
import os

class Utility_object(object):

    @classmethod
    def get_path(self, path_param):
        try:
            requiredPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), path_param)
            return requiredPath
        except IOError as e:
            print(e)

    # Get the current time stamp
    @classmethod
    def get_current_time_stamp(self):
        curr_timestamp = str(datetime.now())
        return curr_timestamp

    # Print the required message
    def log_message(self, log_type, log_message):
        time_stamp = self.get_current_time_stamp()
        log_message = "["+time_stamp+"]: "+"["+log_type+"] - "+log_message
        print(log_message)

    # return json data
    def json_file_reader(self):
        file_path = self.get_path("api.json")
        with open(file_path,'r') as data_file:
            json_data = json.load(data_file)
            return json_data

    # delete file
    def delete_file(self, file_name):
        file_path = self.get_path(file_name)
        os.remove(file_path)