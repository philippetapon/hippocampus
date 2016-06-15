
# coding: utf-8

# In[87]:

# The purpose of the program is to pull diagnoses from a comma-separated value spreadsheet.
# It needs to have one file.  The file is a list of diagnoses.       

# This imports the diagnoses, all of them, into a file called diagnosis_reader. 

print "Opening the file..."
target = open('diagnosislist', 'w')
print "Emptying the file..."
target.truncate()


import csv
with open('1diagnoses.csv') as csvfile:
    diagnoses_reader = csv.reader(csvfile)
    

    for row in diagnoses_reader:
        concatenated_diagnoses = row

        conc_diag_length = len(concatenated_diagnoses)
# Next we use the .split function to break the string into a list, and put that list into split_diagnoses

        if conc_diag_length > 1:
            split_diagnoses = concatenated_diagnoses[0]
        else: 
            split_diagnoses = concatenated_diagnoses
    
# Then we get the list length, that we will need to number the iterations (the while loop)    

        list_length = len(split_diagnoses)


# We start the while loop.  First we set the counter to 0.  Then while the counter is less than the
# the list length we test, we print the diagnosis.  Then we add one to the counter.  

        counter = 0
        while counter < list_length:
            
            individual_diagnosis = split_diagnoses[counter]
            target.write(individual_diagnosis)
            target.write("\r")

#            print split_diagnoses[counter]
            counter += 1
  
  
print "Mission accomplished..." 

# In[ ]:



