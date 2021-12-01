from loguru import logger

_list_ = [1, '2', [3, 4]]
_tuple_ = (1, 2, '3', (4, 5))
_dict_ = {'key1': 1, 'key2': '2', }
_set_ = {1, 2, 3}

logger.info(_list_)
logger.info(_tuple_)
logger.info(_dict_)
logger.info(_set_)
logger.info(type(_set_))
