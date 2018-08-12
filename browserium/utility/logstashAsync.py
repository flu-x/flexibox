import logging
import logstash
import sys

class LogstashAsync():
    def logstash_configure(self):
        host = 'localhost'
        port = 5959

        test_logger = logging.getLogger('python-logstash-logger')
        test_logger.setLevel(logging.INFO)
        test_logger.addHandler(logstash.LogstashHandler(host, port, version=1))

        test_logger.error('python-logstash-async: test logstash error message.')
        test_logger.info('python-logstash-async: test logstash info message.')
        test_logger.warning('python-logstash-async: test logstash warning message.')

        # add extra field to logstash message
        extra = {
            'test_string': 'python version: ' + repr(sys.version_info),
            'test_boolean': True,
            'test_dict': {'a': 1, 'b': 'c'},
            'test_float': 1.23,
            'test_integer': 123,
            'test_list': [1, 2, '3'],
        }
        test_logger.info('python-logstash: test extra fields', extra=extra)