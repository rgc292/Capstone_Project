#!/usr/bin/python

import sys

current_date = None
current_sum = 0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    date, count = line.split("\t")

    #print "%s,%s,%s" %(date,str(count))

    try:
        count = int(count)

    except ValueError:
        continue

    if date == current_date:
        current_sum += count

    else:
        if current_date:

            # output goes to STDOUT (stream data that the program writes)
            print "%s,%d" %(current_date,current_sum)
        current_date = date
        current_sum = count

