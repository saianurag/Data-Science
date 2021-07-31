# Import logging module
import logging 

# Configure logger using basicConfig():
#   level   : Severity level.
#   filename: File to which log msg should be written
#   filemode: Filename mode. The default is append.
#   format  : log message format.

logging.basicConfig(filename="02a_logs.log", 
                    format='%(asctime)s %(message)s', 
                    level = logging.ERROR,
                    filemode='w')   
 
# Test messages 
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')