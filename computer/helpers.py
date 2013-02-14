import re
import hashlib
import random
from datetime import datetime

random.seed()

def regexp(rexp, value):
    rexp = re.compile(rexp)
    return bool(rexp.match(value))

def md5():
    m = hashlib.md5()
    m.update("{0}{1}".format(datetime.now(), random.randint(1000, 999999999)))
    return m.hexdigest()

