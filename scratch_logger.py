import logging
"""
In the logging module there are 6 levels of 'logs'
0~NOTSET
10~DEBUG
20~INFO
30~WARNING
40~ERROR
50~CRITICAL
Loggers will only write messages with level greater
than or equal to our set level
"""
# Create and configure logger
FORMAT = '%(asctime)s %(levelname)s - %(message)s'
logging.basicConfig(filename='C:/users/eiselja/desktop/lumberjack.log',
                    level=logging.DEBUG, format=FORMAT, filemode='w')
logger = logging.getLogger()
# Test the logger
logger.debug('This is a debug statement')
logger.info('Our first message.')
logger.warning('This is a warning')
logger.error('This is an error')
logger.critical('This is a critical message')
# print(logger.level)
