import logging
# https://docs.python.org/3/library/logging.html
# filemode - w will recreate file each and every time
my_format = "%(asctime)s %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, filename="test.log", filemode="w", format=my_format)

logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")