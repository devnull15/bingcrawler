#!/usr/bin/python

import sys

file = open(sys.argv[1]).read()
#print file

post = dict()
for str in file.split('&'):
    #str = str.strip(';')
    print str
    split = str.split('=', 1)
#    print split
    post[split[0]] = split[1]


print post
