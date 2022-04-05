#!/usr/bin/python3
import base58
import sys
import os.path
key58 = sys.argv[2]
filename = sys.argv[1]
if (os.path.exists(filename)):
    print("Filename already exists, please specify a different filename")
    exit()
byte_array = base58.b58decode(key58)
json_string = "[" + ",".join(map(lambda b: str(b), byte_array)) + "]"
#print(json_string)
textfile = open(filename, 'w')
n = textfile.write(json_string)
textfile.close()

