import logging
import logstash
import sys
import platform

class LogstashAsync():
    def logstash_configure(self, log_type, log_message):
        host = 'localhost'
        port = 5959

        test_logger = logging.getLogger('python-logstash-logger')
        test_logger.setLevel(logging.INFO)
        test_logger.addHandler(logstash.LogstashHandler(host, port, version=1))

        if log_type == "ERROR":
            test_logger.error(log_message)

        if log_type == "INFO":
            test_logger.info(log_message)

        if log_type == "WARNING":
            test_logger.warning(log_message)

        if log_type == "EXCEPTION":
            test_logger.exception(log_message)

        # add extra field to logstash message
        extra = {
            'Architecture': 'arch_type: ' + repr(platform.machine()),
            'PlatformVersion': 'platform_version: '+ repr(platform.version()),
            'SystemType': 'sys_type: '+ repr(platform.platform()),
            'OperatingSystem': 'os_type: '+ repr(platform.system()),
            'PlatformProcessor': 'platform_processor: '+ repr(platform.processor()),
            'Python_Version': 'python version: ' + repr(sys.version_info)
        }
        test_logger.info('logstash-system-info: INFORMATION', extra=extra)