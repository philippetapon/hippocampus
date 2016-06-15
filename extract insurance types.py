
# coding: utf-8

# In[2]:




# In[87]:

# The purpose of the program is assign a diagnosis class to each one of a spreadsheet of patients.  In order to do this
# it needs to have two files.  The first file is the list of insurances.  The second file is the list of diagnoses assigned to each patient.  
# The output are the list of diagnosis class, separated by commas, for each patient.    

import csv
with open('insurances.csv') as csvfile:
    insurance_reader = csv.reader(csvfile)
    

    list_of_insurance_classes = ["MEDICARE", "MEDICAID", "HMO", "PPO", "SELF"]
    
# Get the length of the list of diagnosis classes, that we will need for the loop     
    length_of_insurance_class = len(list_of_insurance_classes)

# Here starts the loop, as a for statement.  It goes through each row in the insurance reader, 
# so that the first column, the insurance, gets put into row[0]
# We set the counter to 0.  
    
    edited_insurance = ""
    
    for row in insurance_reader:
        insurance = row[0]

        counter = 0
        
        
# A while loop starts.   
# 
        while counter < length_of_insurance_class:
            insurance_class = list_of_insurance_classes[counter]
            if  insurance_class in insurance:
                print insurance_class
            counter += 1        
        



        
        


# In[ ]:





# In[ ]:



