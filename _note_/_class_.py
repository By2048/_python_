import logging

import base


class A(object):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        logging.info("__len__")
        return len(self.data)

    def __reversed__(self):
        return list(reversed(self.data)) + ['a', 'b', 'c']

    def __contains__(self, item):
        return item in self.data


a = A([1, 2, 3])

logging.info(len(a))
logging.info(reversed(a))
logging.info(1 in a)
