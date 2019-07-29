import uuid
import logging

import shortuuid  # https://github.com/skorokithakis/shortuuid

import base

logging.info(shortuuid.uuid())

logging.info(shortuuid.uuid(name="example.com"))  # 'wpsWLdLt9nscn2jbTD3uxe'
logging.info(shortuuid.uuid(name="http://example.com"))  # 'c8sh5y9hdSMS6zVnrvf53T'

logging.info(shortuuid.ShortUUID().random(length=9))

logging.info(shortuuid.get_alphabet())  # '23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

shortuuid.set_alphabet("abbccc")
logging.info(shortuuid.uuid())
logging.info(shortuuid.get_alphabet())

u = uuid.uuid4()
logging.info(u)

s = shortuuid.encode(u)
logging.info(s)

logging.info(shortuuid.decode(s) == u)

short = s[:7]
logging.info(short)

h = shortuuid.decode(short)
logging.info(h)

logging.info(shortuuid.decode(shortuuid.encode(h)) == h)

su = shortuuid.ShortUUID(alphabet="01345678")
logging.info(su)
logging.info(su.uuid())
logging.info(su.get_alphabet())
su.set_alphabet("21345687654123456")
logging.info(su.get_alphabet())
