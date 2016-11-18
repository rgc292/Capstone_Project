#!/usr/bin/python

import sys

current_date = None
current_sum = 0
current_speed_sum = 0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    date, count_speed = line.split("\t")
    count, speed = count_speed.split(",")
    #print "%s,%s,%s" %(date,str(count),str(speed))

    try:
        count = int(count)
        speed = float(speed)
        #print '%s,%d,%0.10f' %(date,count,speed)
    except ValueError:
        continue

    if date == current_date:
        current_sum += count
        current_speed_sum += speed
        
    else:
        if current_date:
            avg = float(current_speed_sum)/float(current_sum)
            #print '%0.10f' %(avg)
            # output goes to STDOUT (stream data that the program writes)
            print "%s,%0.10f" %(current_date,avg)
        current_date = date
        current_sum = count
        current_speed_sum = speed