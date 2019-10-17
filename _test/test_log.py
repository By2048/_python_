import logging

temp_logger = logging.getLogger('temp')
temp_logger.setLevel(logging.DEBUG)

temp_file_handle = logging.StreamHandler()
temp_formatter = logging.Formatter("[%(levelname)1.1s %(asctime)s %(module)10s:%(lineno)3d] %(message)s")
temp_file_handle.setFormatter(temp_formatter)

temp_logger.addHandler(temp_file_handle)
temp_logger.propagate = False

logging.getLogger('none').info(1)
logging.getLogger('temp').info(2)

logging.getLogger('temp').addHandler(logging.NullHandler())
logging.getLogger('temp').info(3)

temp_logger.addHandler(temp_file_handle)
temp_logger.propagate = False
logging.getLogger('temp').info(4)
