#!/usr/bin/python

import sys
import numpy as np
import csv
import StringIO

col_bus_sub_year = []
col_bus_sub_month = []
col_bus_sub_day = []
col_bus_sub_lat = []
col_bus_sub_lon = []
wifi_year = []
wifi_month = []
wifi_day = []
wifi_lat = []
wifi_lon = []
col_bus_sub = []
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
		if len(l) == 5:
			if (l[0] == '' or l[1] == '' or l[2] == '' or l[3] == '' or l[3] == '0' or l[4] == '' or l[4] == '0'):
			    pass
			else: 
				wifi_year.append(l[0])
				wifi_month.append(l[1])
				wifi_day.append(l[2])
				wifi_lat.append(l[3])
				wifi_lon.append(l[4])
		elif (len(l) == 13):
			if (l[9] == '' or l[10] == '' or l[9] == '0' or l[10] == '0'):
			    pass
			else:
				col_bus_sub_year.append(l[0].split(',')[0].split('-')[0])
				col_bus_sub_month.append(l[0].split(',')[0].split('-')[1])
				col_bus_sub_day.append(l[0].split(',')[0].split('-')[2])
				col_bus_sub_lat.append(l[9])
				col_bus_sub_lon.append(l[10])
				col_bus_sub.append(','.join(map(str, l)).strip())
		else:
		    pass
            
flag = 0

for lat_col_bus_sub, lon_col_bus_sub in zip(col_bus_sub_lat,col_bus_sub_lon):
    wifi_counter = -1
    counter += 1
    flag = 0

    for lat_wifi, lon_wifi in zip(wifi_lat,wifi_lon):
        wifi_counter += 1
        lat_d = dist(float(lat_col_bus_sub),float(lat_wifi),'lat')
        lon_d = dist(float(lon_col_bus_sub),float(lon_wifi),'lon')
        distance = lat_d + lon_d
        if (distance <= 0.031): # 0.015625
            if (int(col_bus_sub_year[counter]) > int(wifi_year[wifi_counter])):
                flag = 1
            elif (int(col_bus_sub_year[counter]) == int(wifi_year[wifi_counter])):
                if (int(col_bus_sub_month[counter]) > int(wifi_month[wifi_counter])):
                    print '%s' %('ok')
                    flag = 1
                elif (int(col_bus_sub_month[counter]) == int(wifi_month[wifi_counter])):
                    if (int(col_bus_sub_day[counter]) > int(wifi_day[wifi_counter])):
                        flag = 1
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
    if flag == 1:
        print '%s,%d' %(col_bus_sub[counter],1)
    elif flag == 0:
        print '%s,%d' %(col_bus_sub[counter],0)
    else:
        pass