
# coding: utf-8

# In[15]:




# In[37]:

# The purpose of the program is to extract from a CSV spreadsheet the times and weather associated to those times. 
# The times are in GMT and will have to be converted to Chicago time in order to work. 

import csv
with open('weatherdata.csv') as csvfile:
    weather_reader = csv.reader(csvfile)
    
    gmt_second = 0
    
    for row in weather_reader:
        gmt_datetime = row[0]
        
        gmt_year = gmt_datetime[0:4]
        year = int(float(gmt_year))
        
        gmt_month = gmt_datetime[4:6]
        month = int(float(gmt_month))
        
        gmt_day = gmt_datetime[6:8]
        day = int(float(gmt_day))
        
        gmt_hour = gmt_datetime[8:10]
        hour = int(float(gmt_hour))
        
        gmt_minute = gmt_datetime[10:12]
        minute = int(float(gmt_minute))
            
        temperature = row[19]
        pressure = row[23]
        
#        date1 = datetime.datetime(year,month,day,hour,minute,gmt_second)

        
        print gmt_datetime, gmt_year, gmt_month, gmt_day, gmt_hour, gmt_minute, temperature, pressure
        
        
            
    
import datetime

print 'Now    :', datetime.datetime.now()
print 'Today  :', datetime.datetime.today()
print 'UTC Now:', datetime.datetime.utcnow()

d = datetime.datetime.now()
for attr in [ 'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
    print attr, ':', getattr(d, attr)
    


# In[ ]:





# In[ ]:




# In[ ]:



