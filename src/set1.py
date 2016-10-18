#!/usr/bin/python

import binascii
import base64

ENDIANNESS = "big"

def hex2base64(s):
    raw_bytes = binascii.unhexlify(s)
    return base64.encodebytes(raw_bytes)

def fixedXOR(first,second):
    first_bytes = binascii.unhexlify(first)
    second_bytes = binascii.unhexlify(second)
    first_int = int.from_bytes(first_bytes,ENDIANNESS)
    second_int = int.from_bytes(second_bytes,ENDIANNESS)
    hex(first_int ^ second_int)


