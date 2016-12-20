#!/usr/bin/python

import sys
import numpy as np
import csv
import StringIO

col_bus_sub_wifi_lat = []
col_bus_sub_wifi_lon = []
sub_lat = []
sub_lon = []
col_bus_sub_wifi = []
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

		if len(l) == 4:
		    if l[2] == '' or l[3] == '' or l[2] == '0' or l[3] == '0':
		        pass
		    else: 
			    sub_lat.append(l[2])
			    sub_lon.append(l[3])
		elif len(l) == 14:
		    if l[9] == '' or l[10] == '' or l[9] == '0' or l[10] == '0':
		        pass
		    else:
		        col_bus_sub_wifi_lat.append(l[9])
		        col_bus_sub_wifi_lon.append(l[10])
		        col_bus_sub_wifi.append(','.join(map(str, l)).strip())
		    
		else:
		    pass

flag = 0

for lat_col_bus_sub_wifi, lon_col_bus_sub_wifi in zip(col_bus_sub_wifi_lat,col_bus_sub_wifi_lon):
    counter += 1
    flag = 0

    for lat_sub, lon_sub in zip(sub_lat,sub_lon):
	    lat_d = dist(float(lat_col_bus_sub_wifi),float(lat_sub),'lat')
	    lon_d = dist(float(lon_col_bus_sub_wifi),float(lon_sub),'lon')
	    distance = lat_d + lon_d
	    if (distance <= 0.0621):
	        flag = 1
	    else:
	        pass
    if flag == 1:
        print '%s,%d' %(col_bus_sub_wifi[counter],1)
    elif flag == 0:
        print '%s,%d' %(col_bus_sub_wifi[counter],0)
    else:
        pass