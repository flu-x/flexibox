import logging
import logstash
import sys
import platform
from logstash_async.handler import AsynchronousLogstashHandler

class Logstash():
    def logstash_type(self, log_type, log_message):
        host = 'localhost'
        port = 5959

        test_logger = logging.getLogger('python-logstash-logger')

        test_logger.setLevel(logging.INFO)

        test_logger.addHandler(AsynchronousLogstashHandler(host, port, database_path='logstash.db'))

        if log_type == "ERROR":
            test_logger.error(log_message)

        if log_type == "INFO":
            test_logger.info(log_message)

        if log_type == "WARNING":
            test_logger.warning(log_message)