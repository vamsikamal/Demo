import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

print('Logging started')
logging.debug('Debug info')
logging.info('Basic info')
logging.warning('a Warning message')
logging.error('DB Connection error')
logging.critical('Value error')