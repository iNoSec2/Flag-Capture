from base64 import *
from pwn import *


x = "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"


print b64decode(x)