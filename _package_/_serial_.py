import string
import binascii
import time

import serial

s = serial.Serial()

s.baudrate = 9600
s.port = 'COM4'
s.open()

# 接收
n = s.inWaiting()
if n:
    print(s.read(n))
    print(binascii.b2a_hex(s.read(n)))

# 发送
d = bytes.fromhex('A5 00 01 00 00 00 80 D2 6A')
s.write(d)
time.sleep(3)

d = bytes.fromhex('A5 00 01 00 00 00 10 D2 06')
s.write(d)
s.close()
