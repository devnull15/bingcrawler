#!/usr/bin/python

import sys

file = open(sys.argv[1]).read()
#print file

cookies = dict()
for str in file.split(' '):
    str = str.strip(';')
    print str
    split = str.split('=', 1)
#    print split
    cookies[split[0]] = split[1]


print cookies
