# coding=utf-8
import crc16


def CRC16(s):
    h = '0'
    for i in range(len(s) // 2):
        h = hex(int(h, 16) + int(s[2 * i:2 * i + 2], 16))

    h = h.replace('0x', '')
    if len(h) <= 1:
        h = '00' + h

    return h.upper()[-2:]


print(CRC16('68AAAAAAAAAAAA681300'))
