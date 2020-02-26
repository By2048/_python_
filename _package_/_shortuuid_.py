import uuid
import logging

import shortuuid
import pysnooper


# https://github.com/skorokithakis/shortuuid

@pysnooper.snoop()
def test():
    _1 = shortuuid.uuid()
    _2 = shortuuid.uuid(name="http://example.com")
    _3 = shortuuid.ShortUUID().random(length=9)
    _4 = shortuuid.get_alphabet()

    shortuuid.set_alphabet("abbccc")
    _6 = shortuuid.uuid()
    _7 = shortuuid.get_alphabet()
    shortuuid.set_alphabet('0123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz')


if __name__ == '__main__':
    test()
