#-*- coding:utf-8 -*-

import random
import string
import uuid

def generate_uid():
    return uuid.uuid4().hex

def generate_accesskey():
    return ''.join(random.sample(string.letters*50,50))

def generate_temp_id():
    return ''.join(random.sample(string.letters*10,10))

