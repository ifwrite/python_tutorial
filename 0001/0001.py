#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-

import random, string

forSelect = string.ascii_letters + '0123456789'
def generate(count, length):
    for x in range(count):
        Re = ''
        for y in range(length):
            Re += random.choice(forSelect)
        print(Re)

generate(200, 20)