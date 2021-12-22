import sys
import logging
import os

if len(sys.argv) == 1: pass
elif sys.argv[1] == 'debug':
    logging.basicConfig(level=logging.DEBUG)
elif sys.argv[1] == 'info':
    logging.basicConfig(level=logging.INFO)
elif sys.argv[1] == 'warn':
    logging.basicConfig(level=logging.WARNING)
elif sys.argv[1] == 'error':
    logging.basicConfig(level=logging.ERROR)
elif sys.argv[1] == 'critical':
    logging.basicConfig(level=logging.CRITICAL)
logging.info('Try importing colored')
try:
    from colored import fg, bg
    logging.info('Success')

except ImportError:
    logging.info('Failure')
    print("Missing library or module. Please run this command and try again.\npip install -r requirements.txt")
