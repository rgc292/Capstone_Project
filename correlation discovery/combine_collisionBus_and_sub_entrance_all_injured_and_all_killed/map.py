#!/usr/bin/python

import sys
import numpy as np
import csv
import StringIO

col_bus_lat = []
col_bus_lon = []
sub_lat = []
sub_lon = []
col_bus = []
counter = -1

def dist(coord1,coord2,_type):
    radius = 6371.0
    if _type == 'lat':
        dlat = np.deg2rad(coord2-coord1)
        dlon = np.deg2rad(0.0)
        a = np.sin(dlat/2.0)**2 + np.cos(np.deg2rad(coord1)) * np.cos(np.deg2rad(coord2)) * np.sin(dlon/2.0) * np.sin(dlon/2.0)
        c = 2.0 * np.arctan2(a**.5, (1.0-a)**.5)
        d = radius * c
        return d/1.6
        
    elif _type == 'lon':
        dlat = np.deg2rad(0.0)
        dlon = np.deg2rad(coord2-coord1)
        a = np.sin(dlat/2.0)**2 + np.cos(np.deg2rad(0.0)) * np.cos(np.deg2rad(0.0)) * np.sin(dlon/2.0) * np.sin(dlon/2.0)
        c = 2.0 * np.arctan2(a**.5, (1.0-a)**.5)
        d = radius * c
        return (d/1.6)/1.311260927412249

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    try:
    #Fill in your map code here. To write to output file, use "print"
    # remove leading and trailing whitespace
        csv_file = StringIO.StringIO(line) 
        csv_reader = csv.reader(csv_file)
        
    except:
        pass
         
    for l in csv_reader:

		if len(l) == 2:
		    if l[0] == '' or l[1] == '' or l[0] == '0' or l[1] == '0':
		        pass
		    else: 
			    sub_lat.append(l[0])
			    sub_lon.append(l[1])
		elif len(l) == 6:
		    if l[3] == '' or l[4] == '' or l[3] == '0' or l[4] == '0':
		        pass
		    else:
		        col_bus_lat.append(l[3])
		        col_bus_lon.append(l[4])
		        col_bus.append(','.join(map(str, l)).strip())
		    
		else:
		    pass

flag = 0

for lat_col_bus, lon_col_bus in zip(col_bus_lat,col_bus_lon):
    counter += 1
    flag = 0

    for lat_sub, lon_sub in zip(sub_lat,sub_lon):
	    lat_d = dist(float(lat_col_bus),float(lat_sub),'lat')
	    lon_d = dist(float(lon_col_bus),float(lon_sub),'lon')
	    distance = lat_d + lon_d
	    if (distance <= 0.015625):
	        flag = 1
	    else:
	        pass
    if flag == 1:
        print '%s,%d' %(col_bus[counter],1)
    elif flag == 0:
        print '%s,%d' %(col_bus[counter],0)
    else:
        pass