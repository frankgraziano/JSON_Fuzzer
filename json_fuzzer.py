#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Simple JSON Generator
# --FG
# @iamreallyfrank

import random
import math
import sys
import json
import time

NONE = 'None'
TRUE = 'True'
FALSE = 'False'
d = random.randint(0, 5)					    #array dimension rand
n = random.randint(10, 30)                                          #number of objects rand
l = random.randint(0,200)                                           #number of chars rand (length)

def get_misc_stuff():
    misc_stuff = ['\x00','%s%x','%p%u','%@','\u0000','-1','00000000','65537','262143','2147483649','4294967297']
    return random.choice(misc_stuff)*l

def get_random_array():
    array_fuzz = {}
    n = random.randint(0, 10)
    for i in range(n):
        array_fuzz[d] = (i,get_random_payload(random.randint(0,9)))
    return array_fuzz

def get_nested_array(d):
    nested_fuzz = {}
    n = random.randint(0, 10)
    for i in range(n):
         nested_fuzz[d]= [(i, get_random_payload(i))]
    return nested_fuzz

def get_random_payload(p):
    ret = ""

    if d > 4 and p > 5:
            p = p % 5

    if False: pass
    elif p is 0: ret = FALSE
    elif p is 1: ret = TRUE
    elif p is 2: ret = NONE
    elif p is 3: ret = get_random_int(l)
    elif p is 4: ret = get_random_float()
    elif p is 5: ret = get_random_string(l)
    elif p is 6: ret = get_random_hexstring(l)
    elif p is 7: ret = get_random_utf8(l)
    elif p is 8: ret = get_random_array()
    elif p is 9: ret = get_nested_array(d)
    elif p is 10: ret = get_misc_stuff()
    return ret

def get_random_int(l):
    i = random.randint(0,0xffffffff)
    return i

def get_random_string(length):
    s = ''.join([ chr(random.randint(0,127)) for x in range(length) ])
    return s

def get_random_hexstring(length):
    h = ''.join(hex(ord(x))[2:] for x in get_random_string(length))
    return h

def get_random_float():
    f = random.random()
    return f

#Modified Version of: http://stackoverflow.com/questions/1477294/generate-random-utf-8-string-in-python
def get_random_utf8(length):

    try:
        get_char = unichr
    except NameError:
        get_char = chr

    include_ranges = [ ( 0x0020, 0xFFFF ) ]

    alphabet = [
        get_char(code_point) for current_range in include_ranges
            for code_point in range(current_range[0], current_range[1] + 1)
    ]
    return ''.join(random.choice(alphabet) for i in range(length))

def main():

    random.seed()							#seed rand

    fuzz = {}								#empty JSON blob

    for i in range(n):
	ret = ""
	fuzz[i] = get_random_payload(random.randint(0,10))
	#DEBUG Single Payload Test Mode
	#fuzz[i] = get_random_payload(10)

    print json.dumps(fuzz)

    try:
        sys.stdout.close()
    except:
        pass
    try:
        sys.stderr.close()
    except:
        pass

if __name__ == '__main__':
    main()
