import logging

import base

# AND 从左到右扫描，返回第一个为假的表达式值，无假值则返回最后一个表达式值。
logging.info('a' and 'b')
logging.info({} and 'b')
logging.info('a' and 'b' and 'c')

# OR 从左到右扫描，返回第一个为真的表达式值，无真值则返回最后一个表达式值。
logging.info('a' or 'b')
logging.info('' or 'b')
logging.info('' or [] or {})

# and or搭配
logging.info(1 and 'a' or 'b')
logging.info(0 and 'a' or 'b')
