
# coding: utf-8

# In[9]:

import sys
f = open('/Users/apple/Downloads/qnacc_14_5.csv')
c = 0
for line in f:
    k = line.strip().split(',')
    if len(k)>8:        
        if k[6]=='WYCKOFF AVENUE':
            if k[5]== 'PALMETTO STREET' or k[5]== 'MYRTLE AVENUE':
                c+= 1
                print '%s,%s\t%s, %d' %(k[6],k[5], k[3], int(k[8])+int(k[9]))
        if k[6]=='PALMETTO STREET':
            if k[5]== 'MYRTLE AVENUE':
                c+= 1
                print '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9]))
        if k[5]=='WYCKOFF AVENUE':
            if k[6]== 'PALMETTO STREET' or k[6]== 'MYRTLE AVENUE':
                c+= 1
                print '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))
        if k[5]=='PALMETTO STREET':
            if k[6]== 'MYRTLE AVENUE':
                c+= 1
                print '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))
                    
        if k[5]=='ROCKAWAY BEACH BOULEVARD':
            if k[6]== 'BEACH 62 STREET'or k[6]== 'BEACH 59 STREET':
                c+= 1
                print '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))
        
        if k[6]=='ROCKAWAY BEACH BOULEVARD':
            if k[5]== 'BEACH 62 STREET'or k[5]== 'BEACH 59 STREET':
                c+= 1
                print '%s,%s\t%s,%s' %(k[6],k[5], k[3], int(k[8])+int(k[9]))
                
        if k[6]=='QUEENS BOULEVARD':
            if k[5]== 'ELIOT AVENUE'or k[5]== '74 STREET' or k[5]== 'ALBION AVENUE'or k[5] == '55 AVENUE' or k[5] == '59 AVENUE' or k[5]=='GRAND AVENUE'or k[5]=='WOODHAVEN BOULEVARD'or k[5]=="BROADWAY":
                c+= 1
                print '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9])) 
        
        if k[5]=='QUEENS BOULEVARD':
            if k[6]== 'ELIOT AVENUE'or k[6]== '74 STREET' or k[6]== 'ALBION AVENUE'or k[6] == '55 AVENUE' or k[6] == '59 AVENUE' or k[6]=='GRAND AVENUE'or k[6]=='WOODHAVEN BOULEVARD'or k[6]=="BROADWAY":
                c+= 1
                print '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9])) 
                
        if k[5]=='NORTHERN BOULEVARD':
            if k[6]== '37 STREET'or k[6] == '36 AVENUE' or k[6] == '38 AVENUE' or k[6]=='34 AVENUE'or k[6]=='31 STREET' or k[6]=='39 STREET' or k[6]=='48 STREET' or k[6]=='BROADWAY'or k[6]=='HONEYWELL STREET':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9])) 
        if k[6]=='NORTHERN BOULEVARD':
            if k[5]== '37 STREET'or k[5] == '36 AVENUE' or k[5] == '38 AVENUE' or k[5]=='34 AVENUE'or k[5]=='31 STREET' or k[5]=='39 STREET' or k[5]=='48 STREET' or k[5]=='BROADWAY'or k[5]=='HONEYWELL STREET':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9])) 
        
        if k[5] == 'BROADWAY':
            if k[6]=='41 AVENUE' or k[6] =='BAXTER AVENUE':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9])) 
        if k[6] == 'BROADWAY':
            if k[5]=='41 AVENUE' or k[5] =='BAXTER AVENUE':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9])) 
        if k[5]== '41 AVENUE':
            if k[6]=='BAXTER AVENUE':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9])) 
        if k[6]== '41 AVENUE':
            if k[5]=='BAXTER AVENUE':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9])) 
                
        if k[5] =='ROCKAWAY BOULEVARD':
            if k[6]=='89 STREET' or k[6] =='90 STREET'or k[6]=='102 AVENUE':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))
        if k[6] =='ROCKAWAY BOULEVARD':
            if k[5]=='89 STREET' or k[5] =='90 STREET'or k[5]=='102 AVENUE':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9]))
                
        if k[5] =='77 AVENUE':
            if k[6]=='81 STREET':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))
        if k[6] =='77 AVENUE':
            if k[5]=='81 STREET':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9]))
        
        if k[6]=='NORTHERN BOULEVARD':
            for i in range(10):
                if k[5]==str(i+105)+' '+'STREET':
                    c+= 1
                    print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9]))
          
        if k[5]=='NORTHERN BOULEVARD':
            for i in range(10):
                if k[6]==str(i+105)+' '+'STREET':
                    c+= 1
                    print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))
                    
        if k[5]=='HILLSIDE AVENUE':
            if k[6]=='PARSONS BOULEVARD' or k[6] =='169 STREET'or k[6] =='HOMELAWN STREET'or k[6] == 'MERRICK BOULEVARD' or k[6] =='166 STREET' or k[6] =='172 STREET' :                
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))
        if k[6]=='HILLSIDE AVENUE':
            if k[5]=='PARSONS BOULEVARD' or k[5] =='169 STREET'or k[5] =='HOMELAWN STREET'or k[5] == 'MERRICK BOULEVARD' or k[5] =='166 STREET' or k[5] =='172 STREET' :                
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9]))
        
        if k[5]=='MOTT AVENUE':
            for i in range(4):
                if k[6]== 'BEACH'+' '+ str(i+19)+' '+'STREET':
                    c+= 1
                    print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))
            if k[6] == 'CENTRAL AVENUE':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))                    
         
        if k[6]=='MOTT AVENUE':
            for i in range(4):
                if k[5]== 'BEACH'+' '+ str(i+19)+' '+'STREET':
                    c+= 1
                    print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9]))
            if k[5] == 'CENTRAL AVENUE':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9]))
        
        if k[5]=='138 STREET':
            if k[6]=='31 ROAD':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9])) 
      
        if k[6]=='138 STREET':
            if k[5]=='31 ROAD':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9])) 
        
        if k[5]=='GRAND AVENUE':
            if k[6]=='69 PLACE' or k[6]=='69 LANE' or k[6]=='69 STREET'or k[6]=='71 STREET'or k[6]=='74 STREET' or k[6]=='57 AVENUE' or k[6] =='BORDEN AVENUE':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))
        
        if k[6]=='GRAND AVENUE':
            if k[5]=='69 PLACE' or k[5]=='69 LANE' or k[5]=='69 STREET'or k[5]=='71 STREET'or k[5]=='74 STREET' or k[5]=='57 AVENUE' or k[5] =='BORDEN AVENUE':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9]))
       
        if k[5] =='SHORE BOULEVARD':
            c+= 1
            print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))
        
         
        if k[6] =='SHORE BOULEVARD':
            c+= 1
            print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9]))
        
        if k[5]=='HOYT AVENUE NORTH':
            if k[6]=='19 STREET':               
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))
        if k[6]=='HOYT AVENUE NORTH':
            if k[5]=='19 STREET':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9]))
                       
                
        if k[5]=='20 AVENUE':
            if k[6] == 'CRESCENT STREET' or k[6]=='21 STREET':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))
        if k[6]=='20 AVENUE':
            if k[5] == 'CRESCENT STREET' or k[6]=='21 STREET':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9]))
        
        if k[5]=='111 STREET':
            for i in range(13):
                if k[6]==str(i+43)+' '+'AVENUE':
                    c+= 1
                    print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))
        if k[6]=='111 STREET':
            for i in range(13):
                if k[5]==str(i+43)+' '+'AVENUE':
                    c+= 1
                    print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9]))
        
        if k[5]=="HILLSIDE AVENUE":
            if k[6]=='METROPOLITAN AVENUE'or k[6]=='KEW GARDENS ROAD' or k[6]== '127 STREET':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))
        
        if k[6]=="HILLSIDE AVENUE":
            if k[5]=='METROPOLITAN AVENUE'or k[5]=='KEW GARDENS ROAD' or k[5]== '127 STREET':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9]))
        
        if k[5]=="77 STREET":
            if k[6]=="25 AVENUE" or k[6]=='30 AVENUE':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))
           
        if k[6]=="77 STREET":
            if k[5]=="25 AVENUE" or k[5]=='30 AVENUE':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9]))
                
        if k[5]=='29 AVENUE':
            if k[6]=='155 STREET'or k[6]=='159 STREET':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))
        
        if k[5]=='32 AVENUE':
            if k[6]=='155 STREET'or k[6]=='159 STREET':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))
                
                  
        if k[6]=='29 AVENUE':
            if k[5]=='155 STREET'or k[5]=='159 STREET':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9]))
        
        if k[6]=='32 AVENUE':
            if k[5]=='155 STREET'or k[5]=='159 STREET':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9]))
      
        if k[5]=='ASTORIA BOULEVARD':
            for i in range(3):
                if k[6]==str(i+77)+' '+'STREET':
                    c+= 1
                    print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))     
            for i in range(10):
                if k[6]==str(i+99)+' '+'STREET':
                    c+= 1
                    print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))   
            for i in range(6):
                if k[6]==str(i+24)+' '+'AVENUE':
                    c+= 1
                    print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))  
        
        if k[6]=='ASTORIA BOULEVARD':
            for i in range(3):
                if k[5]==str(i+77)+' '+'STREET':
                    c+= 1
                    print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9]))     
            for i in range(10):
                if k[5]==str(i+99)+' '+'STREET':
                    c+= 1
                    print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9]))   
            for i in range(6):
                if k[5]==str(i+24)+' '+'AVENUE':
                    c+= 1
                    print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9]))  
       
        if k[5]=='BROADWAY':
            if k[6]=='72 STREET'or k[6]=='73 STREET'or k[6]=='75 STREET'or k[6] =='37 ROAD' or k[6] =='ROOSEVELT AVENUE':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))  
        
        if k[6]=='BROADWAY':
            if k[5]=='72 STREET'or k[5]=='73 STREET'or k[5]=='75 STREET'or k[5] =='37 ROAD' or k[5] =='ROOSEVELT AVENUE':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9]))  
       
        if k[5]=='VERNON BOULEVARD':
            if k[6]=='50 AVENUE'or k[6]=='51 AVENUE' or k[6]=='BORDEN AVENUE' or k[6]=='JACKSON AVENUE' or k[6] =='10 STREET'or k[6]=='45 AVENUE':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9]))  
          
        if k[6]=='VERNON BOULEVARD':
            if k[5]=='50 AVENUE'or k[5]=='51 AVENUE' or k[5]=='BORDEN AVENUE' or k[5]=='JACKSON AVENUE'or k[5] =='10 STREET'or k[5]=='45 AVENUE':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9]))       
        if k[5]=='BORDEN AVENUE':
            if k[6]=='11 STREET':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9])) 
                
        if k[6]=='BORDEN AVENUE':
            if k[5]=='11 STREET':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9])) 
       
        if k[5]=='JACKSON AVENUE':
            for i in range(4):
                if k[6]==str(i+48)+' '+'AVENUE':
                    c+= 1
                    print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9])) 
            if k[6]=='11 STREET'or k[6]=='21 STREET' or k[6]=='23 STREET':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9])) 
         
        if k[6]=='JACKSON AVENUE':
            for i in range(4):
                if k[5]==str(i+48)+' '+'AVENUE':
                    c+= 1
                    print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9])) 
            if k[5]=='11 STREET' or k[5]=='21 STREET' or k[5]=='23 STREET':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9])) 
   
        if k[5]=='48 AVENUE':
            if k[6]=='5 STREET'or k[6]=='VERNON BOULEVARD':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9])) 
                
        if k[6]=='48 AVENUE':
            if k[5]=='5 STREET'or k[5]=='VERNON BOULEVARD':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9])) 
       
        if k[5]=='44 DRIVE':
            if k[6]=='JACKSON AVENUE' or k[6]=='THOMSON AVENUE' or k[6]=='VERNON BOULEVARD' or k[6]=='5 STREET'or k[6]=='10 STREET'or k[6]=='11 STREET':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9])) 
        
        if k[6]=='44 DRIVE':
            if k[5]=='JACKSON AVENUE' or k[5]=='THOMSON AVENUE' or k[5]=='VERNON BOULEVARD' or k[5]=='5 STREET'or k[5]=='10 STREET'or k[5]=='11 STREET':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9])) 
     
        if k[5]=='11 STREET':
            if k[6]=='45 AVENUE'or k[6]=='45 ROAD'or k[6]=='46 AVENUE'or k[6]=='46 ROAD':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9])) 
        
        if k[6]=='11 STREET':
            if k[5]=='45 AVENUE'or k[5]=='45 ROAD'or k[5]=='46 AVENUE'or k[5]=='46 ROAD':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9])) 
                
        
        if k[5]=='21 STREET':
            if k[6]=='49 AVENUE'or k[6]=='47 ROAD'or k[6]=='50 AVENUE'or k[6]=='46 AVENUE' or k[6]=='JACKSON AVENUE':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9])) 
        
        if k[6]=='21 STREET':
            if k[5]=='49 AVENUE'or k[5]=='47 ROAD'or k[5]=='50 AVENUE'or k[5]=='46 AVENUE' or k[5]=='JACKSON AVENUE':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9])) 
        
        if k[5]=='23 STREET':
            if k[6]=='45 AVENUE'or k[6]=='45 ROAD'or k[6]=='44 DRIVE'or k[6]=='JACKSON AVENUE':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9])) 
        
        if k[6]=='23 STREET':
            if k[5]=='45 AVENUE'or k[5]=='45 ROAD'or k[5]=='44 DRIVE'or k[5]=='JACKSON AVENUE':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9])) 
        
        if k[5]=='5 STREET':
            if k[6]=='47 AVENUE'or k[6]=='47 ROAD'or k[6]=='46 AVENUE'or k[6]=='46 ROAD':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[5],k[6], k[3], int(k[8])+int(k[9])) 
        
        if k[6]=='5 STREET':
            if k[5]=='47 AVENUE'or k[5]=='47 ROAD'or k[5]=='46 AVENUE'or k[5]=='46 ROAD':
                c+= 1
                print  '%s,%s\t%s, %s' %(k[6],k[5], k[3], int(k[8])+int(k[9])) 
                


# In[10]:

c

