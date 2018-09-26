# Author: @Corefinder
# Language: Python
# Copyrights: SoumyajitBasu
# Purpose: The purpose of the class Utility is to consist of the generic functions that
# can be used across all the functionalities that would be developed in this project

from datetime import datetime
import json

class Utility():
    # Get the current time stamp
    @staticmethod
    def get_current_time_stamp():
        curr_timestamp = str(datetime.now())
        return curr_timestamp

    # Print the required message
    @staticmethod
    def log_message(log_type, log_message):
        time_stamp = Utility.get_current_time_stamp()
        log_message = "["+time_stamp+"]: "+"["+log_type+"] - "+log_message
        print log_message

    # return json data
    @staticmethod
    def json_file_reader():
        with open("../api.json") as data_file:
            json_data = json.loads(data_file)
            return json_data