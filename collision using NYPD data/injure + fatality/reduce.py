#!/usr/bin/python

import sys
c =0 
for line in sys.stdin:
    k,v = line.strip().split('\t')
    c = c + int(v)
print c

