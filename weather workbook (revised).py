
# coding: utf-8

# In[25]:




# In[37]:

# The purpose of the program is to extract from a CSV spreadsheet the times and weather associated to those times. 
# The times are in GMT and will have to be converted to Chicago time in order to work. 

# Import the datetime library that we will use later    
import datetime

# This incredible one-line command creates an array, instantly, of the entire CSV file.  
stringed_array_weather = tuple(open('weatherdata.csv', 'r'))

# Set up constants 
second = 0
GMT_offset = datetime.timedelta(hours=-5)

counter = 0
array = []

# The maximum number of observations has to be set to some number fewer than the
# rows of the weatherdata.csv 
# 4500 will cover everything
# smaller numbers like 5 or 50 make testing easier
maximum_number_of_observations = 500


# Start the first while loop, using the counter.  Initially we pull the first row
# as a string named current string. 
while counter < maximum_number_of_observations:
    current_string = stringed_array_weather[counter]

# We make the current string into a list with split(), using comma as a delimiter 
    current_data_as_list = current_string.split(",")

    
# Let's get the temperature and pressures using the list functions, 
# and use the integer and float commands to ensure the variables are numerical.  
    string_temperature = current_data_as_list[20]
    temperature = int(float(string_temperature))

    string_pressure = current_data_as_list[23]
    pressure = int(float(string_pressure))

# Let's get the elements of date-time by getting the strings      
 
    gmt_year = current_string[0:4]
    year = int(float(gmt_year))
        
    gmt_month = current_string[4:6]
    month = int(float(gmt_month))
        
    gmt_day = current_string[6:8]
    day = int(float(gmt_day))  
        
    gmt_hour = current_string[8:10]
    hour = int(float(gmt_hour))
        
    gmt_minute = current_string[10:12]
    minute = int(float(gmt_minute))

# create the array    
    current_datetime = datetime.datetime(year, month, day, hour, minute, second)
    
# substract the GMT offset to get it to local Chicago time    
    current_datetime = current_datetime + GMT_offset
    
# Now create the line of the array containing all the elements, "in the hopper"  
    array_in_the_hopper = [counter,current_datetime,temperature,pressure]
#   print array_in_the_hopper[0],array_in_the_hopper[1],array_in_the_hopper[2],array_in_the_hopper[3]
    print array_in_the_hopper[0],",",array_in_the_hopper[1],",",array_in_the_hopper[2],",",array_in_the_hopper[3]

# Now add that line in the hopper to the array. This array consists of a list of lists. 
    array.append(array_in_the_hopper)
    
# And advance the counter
    counter = counter + 1
    





# In[26]:

#This next section of code pulls out parts of what we want to work with. 

# Two counters are set up: an outer counter going through rows, 
# and an inner counter moving within the row 

inner_counter = 0
outer_counter = 0

# We will call the "base" the extracted line.  I like the idea of bases 
# because there are four bases in baseball and four elements to the list:
# the line number, the date-time, the temperature, and the pressure 

# the maximum number of observations was set by the previous cell. 

while outer_counter < maximum_number_of_observations:
    base = array[outer_counter]
#   print base
    while inner_counter < 4:
        man_on_base = base[inner_counter]
        if inner_counter == 1:
            print man_on_base
            
        inner_counter = inner_counter + 1
    inner_counter = 0
    print ""
    outer_counter = outer_counter + 1 


# In[27]:

starting_block = 0
offset = 1

# the datetime is within offset of 1
within_offset = 1

start_line_of_array = array[starting_block]
print start_line_of_array
next_line_of_array = array[offset]
print next_line_of_array

first_datetime = start_line_of_array[within_offset]
print first_datetime

second_datetime = next_line_of_array[within_offset]
print second_datetime

delta = second_datetime - first_datetime
print delta 

one_day = datetime.timedelta(days=1)

if delta < one_day:
    print "less than a day"
        


# In[34]:

outer_counter = 0
inner_counter = 0
date_place = 1
delta = datetime.timedelta(seconds=1)

while delta < one_day:
    print delta
    array_in_the_hopper = array[outer_counter]
    anchor_date_time = array_in_the_hopper[date_place]

    inner_counter = inner_counter + 1
    further_array = array[inner_counter] 
    aweigh_date_time = further_array[date_place]

    print anchor_date_time
    print aweigh_date_time
    delta = aweigh_date_time - anchor_date_time
    print "not quite a day"
else: 
    print anchor_date_time
    print aweigh_date_time    
    print "that's a day"
    outer_counter = outer_counter + 1
    if outer_counter < maximum_number_of_observations:
        delta = datetime.timedelta(seconds=1)
    
    


# In[ ]:



