
# coding: utf-8

# In[137]:

import pandas as pd
import numpy as np
from pandas import DataFrame
df = pd.read_csv("/Users/apple/Downloads/qnacc_13_9.csv",sep=",")

df['Unnamed: 1'] = df['Unnamed: 1'].replace('Number of Collisions',0)


# In[138]:

c =0
for i in range(4981):
    if type(df['Motor Vehicle Collision Report Intersections'].str.replace('\n', ' ')[i]) is str:
        k = df['Motor Vehicle Collision Report Intersections'].str.replace('\n', ' ')[i].split('and')
        if len(k)==2:
            if k[0]=='WYCKOFF AVENUE ':
                if k[1]== ' PALMETTO STREET' or k[1]== ' MYRTLE AVENUE':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
                    
            if k[0]=='PALMETTO STREET ':
                if k[1]== ' MYRTLE AVENUE':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
                    
            if k[1]==' WYCKOFF AVENUE':
                if k[0]== 'PALMETTO STREET ' or k[0]== 'MYRTLE AVENUE ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
            if k[1]==' PALMETTO STREET':
                if k[0]== 'MYRTLE AVENUE ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
                    
            if k[0]=='ROCKAWAY BEACH BOULEVARD ':
                if k[1]== ' BEACH 62 STREET'or k[1]== ' BEACH 59 STREET':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
        
            if k[1]==' ROCKAWAY BEACH BOULEVARD':
                if k[0]== 'BEACH 62 STREET 'or k[0]== 'BEACH 59 STREET ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
                         
            if k[0]=='QUEENS BOULEVARD ':
                if k[1]== ' ELIOT AVENUE'or k[1]== ' 74 STREET' or k[1]== ' ALBION AVENUE'or k[1] == ' 55 AVENUE' or k[1] == ' 59 AVENUE' or k[1]==' GRAND AVENUE'or k[1]==' WOODHAVEN BOULEVARD'or k[1]==" BROADWAY":
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i]) 
        
            if k[1]==' QUEENS BOULEVARD':
                if k[0]== 'ELIOT AVENUE 'or k[0]== '74 STREET ' or k[0]== 'ALBION AVENUE 'or k[0] == '55 AVENUE ' or k[0] == '59 AVENUE ' or k[0]=='GRAND AVENUE 'or k[0]=='WOODHAVEN BOULEVARD 'or k[0]=="BROADWAY ":
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
                
            if k[0]=='NORTHERN BOULEVARD ':
                if k[1]== ' 37 STREET'or k[1] == ' 36 AVENUE' or k[1] == ' 38 AVENUE' or k[1]==' 34 AVENUE'or k[1]==' 31 STREET' or k[1]==' 39 STREET' or k[1]==' 48 STREET' or k[1]==' BROADWAY'or k[1]==' HONEYWELL STREET':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
       
            if k[1]==' NORTHERN BOULEVARD':
                if k[0]== '37 STREET 'or k[0] == '36 AVENUE ' or k[0] == '38 AVENUE ' or k[0]=='34 AVENUE 'or k[0]=='31 STREET ' or k[0]=='39 STREET ' or k[0]=='48 STREET ' or k[0]=='BROADWAY 'or k[0]=='HONEYWELL STREET ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
        
            if k[0] == 'BROADWAY ':
                if k[1]==' 41 AVENUE' or k[1] ==' BAXTER AVENUE':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
            if k[1] == ' BROADWAY':
                if k[0]=='41 AVENUE ' or k[0] =='BAXTER AVENUE ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
            if k[0]== '41 AVENUE ':
                if k[1]==' BAXTER AVENUE':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
            if k[1]== ' 41 AVENUE':
                if k[0]=='BAXTER AVENUE ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
                
            if k[0] =='ROCKAWAY BOULEVARD ':
                if k[1]==' 89 STREET' or k[1] ==' 90 STREET'or k[1]==' 102 AVENUE':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
            if k[1] ==' ROCKAWAY BOULEVARD':
                if k[0]=='89 STREET ' or k[0] =='90 STREET 'or k[0]=='102 AVENUE ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
                
            if k[0] =='77 AVENUE ':
                if k[1]==' 81 STREET':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
            if k[1] ==' 77 AVENUE':
                if k[0]=='81 STREET ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
        
            if k[1]==' NORTHERN BOULEVARD':
                for i in range(10):
                    if k[0]==str(i+105)+' '+'STREET ':
                        if df['Unnamed: 1'].isnull()[i]:
                            continue
                        else: 
                            c+= int(df['Unnamed: 1'][i])
          
            if k[0]=='NORTHERN BOULEVARD ':
                for i in range(10):
                    if k[1]==' '+ str(i+105)+' '+'STREET':
                        if df['Unnamed: 1'].isnull()[i]:
                            continue
                        else: 
                            c+= int(df['Unnamed: 1'][i])
                    
            if k[0]=='HILLSIDE AVENUE ':
                if k[1]==' PARSONS BOULEVARD' or k[1] ==' 169 STREET'or k[1] ==' HOMELAWN STREET'or k[1] == ' MERRICK BOULEVARD' or k[1] ==' 166 STREET' or k[1] ==' 172 STREET' :                
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
            if k[1]==' HILLSIDE AVENUE':
                if k[0]=='PARSONS BOULEVARD ' or k[0] =='169 STREET 'or k[0] =='HOMELAWN STREET 'or k[0] == 'MERRICK BOULEVARD ' or k[0] =='166 STREET ' or k[0] =='172 STREET ' :                
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
        
            if k[0]=='MOTT AVENUE ':
                for i in range(4):
                    if k[1]== ' BEACH'+' '+ str(i+19)+' '+'STREET':
                        
                        if df['Unnamed: 1'].isnull()[i]:
                            continue
                        else: 
                            c+= int(df['Unnamed: 1'][i])
                if k[1] == ' CENTRAL AVENUE':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])                   
         
            if k[1]==' MOTT AVENUE':
                for i in range(4):
                    if k[0]== 'BEACH'+' '+ str(i+19)+' '+'STREET ':
                        if df['Unnamed: 1'].isnull()[i]:
                            continue
                        else: 
                            c+= int(df['Unnamed: 1'][i])
                if k[0] == 'CENTRAL AVENUE ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
        
            if k[0]=='138 STREET ':
                if k[1]==' 31 ROAD':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
      
            if k[1]==' 138 STREET':
                if k[0]=='31 ROAD ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i]) 
        
            if k[0]=='GRAND AVENUE ':
                if k[1]==' 69 PLACE' or k[1]==' 69 LANE' or k[1]==' 69 STREET'or k[1]==' 71 STREET'or k[1]==' 74 STREET' or k[1]==' 57 AVENUE' or k[1] ==' BORDEN AVENUE':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
        
            if k[1]==' GRAND AVENUE':
                if k[0]=='69 PLACE ' or k[0]=='69 LANE ' or k[0]=='69 STREET 'or k[0]=='71 STREET 'or k[0]=='74 STREET ' or k[0]=='57 AVENUE ' or k[0] =='BORDEN AVENUE ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
       
            if k[0] =='SHORE BOULEVARD ':
                if df['Unnamed: 1'].isnull()[i]:
                    continue
                else: 
                    c+= int(df['Unnamed: 1'][i])
        
         
            if k[1] ==' SHORE BOULEVARD':
                if df['Unnamed: 1'].isnull()[i]:
                    continue
                else: 
                    c+= int(df['Unnamed: 1'][i])
        
            if k[0]=='HOYT AVENUE NORTH ':
                if k[1]==' 19 STREET':               
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
            if k[1]==' HOYT AVENUE NORTH':
                if k[0]=='19 STREET ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
                       
                
            if k[0]=='20 AVENUE ':
                if k[1] == ' CRESCENT STREET' or k[1]==' 21 STREET':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
            if k[1]==' 20 AVENUE':
                if k[0] == 'CRESCENT STREET ' or k[0]=='21 STREET ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
        
            if k[0]=='111 STREET ':
                for i in range(13):
                    if k[1]==' '+ str(i+43)+' '+'AVENUE':
                        if df['Unnamed: 1'].isnull()[i]:
                            continue
                        else: 
                            c+= int(df['Unnamed: 1'][i])
            if k[1]==' 111 STREET':
                for i in range(13):
                    if k[0]==str(i+43)+' '+'AVENUE ':
                        if df['Unnamed: 1'].isnull()[i]:
                            continue
                        else: 
                            c+= int(df['Unnamed: 1'][i])
        
            if k[0]=="HILLSIDE AVENUE ":
                if k[1]==' METROPOLITAN AVENUE'or k[1]==' KEW GARDENS ROAD' or k[1]== ' 127 STREET':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
        
            if k[1]==" HILLSIDE AVENUE":
                if k[0]=='METROPOLITAN AVENUE 'or k[0]=='KEW GARDENS ROAD ' or k[0]== '127 STREET ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
        
            if k[0]=="77 STREET ":
                if k[1]==" 25 AVENUE" or k[1]==' 30 AVENUE':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
            if k[1]==" 77 STREET":
                if k[0]=="25 AVENUE " or k[0]=='30 AVENUE ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
                
            if k[0]=='29 AVENUE ':
                if k[1]==' 155 STREET'or k[1]==' 159 STREET':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
        
            if k[0]=='32 AVENUE ':
                if k[1]==' 155 STREET'or k[1]==' 159 STREET':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
                
                  
            if k[1]==' 29 AVENUE':
                if k[0]=='155 STREET 'or k[0]=='159 STREET ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
        
            if k[1]==' 32 AVENUE':
                if k[0]=='155 STREET 'or k[0]=='159 STREET ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
      
            if k[0]=='ASTORIA BOULEVARD ':
                for i in range(3):
                    if k[1]==' ' +str(i+77)+' '+'STREET':
                        if df['Unnamed: 1'].isnull()[i]:
                            continue
                        else: 
                            c+= int(df['Unnamed: 1'][i])    
                for i in range(10):
                    if k[1]==' ' +str(i+99)+' '+'STREET':
                        if df['Unnamed: 1'].isnull()[i]:
                            continue
                        else: 
                            c+= int(df['Unnamed: 1'][i])  
                for i in range(6):
                    if k[1]==' ' +str(i+24)+' '+'AVENUE':
                        if df['Unnamed: 1'].isnull()[i]:
                            continue
                        else: 
                            c+= int(df['Unnamed: 1'][i]) 
        
            if k[1]==' ASTORIA BOULEVARD':
                for i in range(3):
                    if k[0]==str(i+77)+' '+'STREET ':
                        if df['Unnamed: 1'].isnull()[i]:
                            continue
                        else: 
                            c+= int(df['Unnamed: 1'][i])    
                for i in range(10):
                    if k[0]==str(i+99)+' '+'STREET ':
                        if df['Unnamed: 1'].isnull()[i]:
                            continue
                        else: 
                            c+= int(df['Unnamed: 1'][i])
                for i in range(6):
                    if k[0]==str(i+24)+' '+'AVENUE ':
                        if df['Unnamed: 1'].isnull()[i]:
                            continue
                        else: 
                            c+= int(df['Unnamed: 1'][i])
       
            if k[0]=='BROADWAY ':
                if k[1]==' 72 STREET'or k[1]==' 73 STREET'or k[1]==' 75 STREET'or k[1] ==' 37 ROAD' or k[1] ==' ROOSEVELT AVENUE':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
        
            if k[1]==' BROADWAY':
                if k[0]=='72 STREET 'or k[0]=='73 STREET 'or k[0]=='75 STREET 'or k[0] =='37 ROAD ' or k[0] =='ROOSEVELT AVENUE ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
       
            if k[0]=='VERNON BOULEVARD ':
                if k[1]==' 50 AVENUE'or k[1]==' 51 AVENUE' or k[1]==' BORDEN AVENUE' or k[1]==' JACKSON AVENUE' or k[1] ==' 10 STREET'or k[1]==' 45 AVENUE':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
          
            if k[1]==' VERNON BOULEVARD':
                if k[0]=='50 AVENUE 'or k[0]=='51 AVENUE ' or k[0]=='BORDEN AVENUE ' or k[0]=='JACKSON AVENUE 'or k[0] =='10 STREET 'or k[0]=='45 AVENUE ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])      
            if k[0]=='BORDEN AVENUE ':
                if k[1]==' 11 STREET':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
                
            if k[1]==' BORDEN AVENUE':
                if k[0]=='11 STREET ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
       
            if k[0]=='JACKSON AVENUE ':
                for i in range(4):
                    if k[1]==' '+str(i+48)+' '+'AVENUE':
                        if df['Unnamed: 1'].isnull()[i]:
                            continue
                        else: 
                            c+= int(df['Unnamed: 1'][i])
                if k[1]==' 11 STREET'or k[1]==' 21 STREET' or k[1]==' 23 STREET':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
         
            if k[1]==' JACKSON AVENUE':
                for i in range(4):
                    if k[0]==str(i+48)+' '+'AVENUE ':
                        if df['Unnamed: 1'].isnull()[i]:
                            continue
                        else: 
                            c+= int(df['Unnamed: 1'][i])
                if k[0]=='11 STREET ' or k[0]=='21 STREET ' or k[0]=='23 STREET ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
   
            if k[0]=='48 AVENUE ':
                if k[1]==' 5 STREET'or k[1]==' VERNON BOULEVARD':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
                
            if k[1]==' 48 AVENUE':
                if k[0]=='5 STREET 'or k[0]=='VERNON BOULEVARD ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i]) 
       
            if k[0]=='44 DRIVE ':
                if k[1]==' JACKSON AVENUE' or k[1]==' THOMSON AVENUE' or k[1]==' VERNON BOULEVARD' or k[1]==' 5 STREET'or k[1]==' 10 STREET'or k[1]==' 11 STREET':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
        
            if k[1]==' 44 DRIVE':
                if k[0]=='JACKSON AVENUE ' or k[0]=='THOMSON AVENUE ' or k[0]=='VERNON BOULEVARD ' or k[0]=='5 STREET 'or k[0]=='10 STREET 'or k[0]=='11 STREET ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
     
            if k[0]=='11 STREET ':
                if k[1]==' 45 AVENUE'or k[1]==' 45 ROAD'or k[1]==' 46 AVENUE'or k[1]==' 46 ROAD':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
        
            if k[1]==' 11 STREET':
                if k[0]=='45 AVENUE 'or k[0]=='45 ROAD 'or k[0]=='46 AVENUE 'or k[0]=='46 ROAD ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
                
        
            if k[0]=='21 STREET ':
                if k[1]==' 49 AVENUE'or k[1]==' 47 ROAD'or k[1]==' 50 AVENUE'or k[1]==' 46 AVENUE' or k[1]==' JACKSON AVENUE':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i]) 
        
            if k[1]==' 21 STREET':
                if k[0]=='49 AVENUE 'or k[0]=='47 ROAD 'or k[0]=='50 AVENUE 'or k[0]=='46 AVENUE ' or k[0]=='JACKSON AVENUE ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
        
            if k[0]=='23 STREET ':
                if k[1]==' 45 AVENUE'or k[1]==' 45 ROAD'or k[1]==' 44 DRIVE'or k[1]==' JACKSON AVENUE':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
        
            if k[1]==' 23 STREET':
                if k[0]=='45 AVENUE 'or k[0]=='45 ROAD 'or k[0]=='44 DRIVE 'or k[0]=='JACKSON AVENUE ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
        
            if k[0]=='5 STREET ':
                if k[1]==' 47 AVENUE'or k[1]==' 47 ROAD'or k[1]==' 46 AVENUE'or k[1]==' 46 ROAD':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
        
            if k[1]==' 5 STREET':
                if k[0]=='47 AVENUE 'or k[0]=='47 ROAD 'or k[0]=='46 AVENUE 'or k[0]=='46 ROAD ':
                    if df['Unnamed: 1'].isnull()[i]:
                        continue
                    else: 
                        c+= int(df['Unnamed: 1'][i])
c

