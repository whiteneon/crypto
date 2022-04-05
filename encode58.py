#!/usr/bin/python3
#import binascii
import base58
import sys
keyfile = sys.argv[1]
file = open(keyfile, 'r')
data = file.read().replace('\n', '').replace('[', '').replace(']', '')
file.close
key = b''
for x in data.split(','):
    w = int(x).to_bytes(1,'big')
    key = b"".join([key, w])
enc_key = base58.b58encode(key)
print(enc_key)
exit()


