#written by openai
import os
import hashlib

size = int(input('Enter the size of the keyfile: '))
name = input('Enter the name of the keyfile: ')

def gen():
    with open('/tmp/keyfile', 'wb') as f:
        f.write(os.urandom(size))

def hasher():
    with open('/tmp/keyfile', 'rb') as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            yield hashlib.sha512(chunk).hexdigest()

gen()
with open(name, 'w') as f:
    for h in hasher():
        f.write(h)

os.truncate(name, size)
