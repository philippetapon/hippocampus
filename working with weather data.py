
# coding: utf-8

# In[37]:

# The purpose of the program is to extract from a CSV spreadsheet the times and weather associated to those times. 
# The times are in GMT and will have to be converted to Chicago time in order to work. 

import csv
with open('weatherdata.csv') as csvfile:
    weather_reader = csv.reader(csvfile)
    
    for row in weather_reader:
        gmt_datetime = row[0]
        gmt_year = gmt_datetime[0:4]
        gmt_month = gmt_datetime[4:6]
        gmt_day = gmt_datetime[6:8]
        gmt_hour = gmt_datetime[8:10]
        gmt_minute = gmt_datetime[10:12]
        
        temperature = row[19]
        pressure = row[23]
        
        date1 = datetime.datetime(gmt_year,gmt_month,gmt_day,gmt_hour,gmt_minute)
        
        print gmt_datetime, gmt_year, gmt_month, gmt_day, gmt_hour, gmt_minute, temperature, pressure
        
        
            
    
import datetime

print 'Now    :', datetime.datetime.now()
print 'Today  :', datetime.datetime.today()
print 'UTC Now:', datetime.datetime.utcnow()

d = datetime.datetime.now()
for attr in [ 'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
    print attr, ':', getattr(d, attr)
    


# In[ ]:



