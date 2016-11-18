#!/usr/bin/python
import sys

for line in sys.stdin:
    k = line.strip().split(',')
    if len(k)>8:        
        if k[6]=='BROADWAY':
            for i in range(19):
                if k[5]=='WEST'+' '+str(i+135)+' '+'STREET':
                    print '%s\t%s' %(k[6], k[8])
                    
        if k[5]=='BROADWAY':
            for i in range(19):
                if k[6]=='WEST'+' '+str(i+135)+' '+'STREET':
                    print '%s\t%s' %(k[5], k[8])
                   

