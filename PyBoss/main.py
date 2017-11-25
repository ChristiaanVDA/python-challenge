## PyBoss
## Christiaan Van den Akker

# import modules
import os
import csv

# Set the paths for the two csv files
csvpath1 = os.path.join("raw_data","employee_data1.csv")
csvpath2 = os.path.join("raw_data","employee_data2.csv")

# Create lists to store data    
user_id = []
name = []
dob = []
ssn = []
state = []
first = []
last = []

# Open the csv file
with open(csvpath1, newline ='') as csvfile1:
    csvreader1 = csv.reader(csvfile1, delimiter=",")
    
    # Skip the header row
    next(csvreader1)
            
    for row in csvreader1:
        user_id.append(row[0])
        name.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])
        
        
        #Tried popping a name but was getting one letter per row
        #PoppedName=name.pop()
        #(firstname,lastname)=PoppedName.split()
        #firstname=first
        #first.append(row[5])
        
        # Getting errors here, because now the names are strings and I need them in lists
        #firstname.extend(row[5])
        #lastname.extend(row[6])         

            
# zip lists together       
transformedCSV = zip(user_id, firstname, lastname, dob, ssn, state)

# set variable for output file
outputfile = os.path.join("output","bossfinal.csv")

# open the output file and set variable to hold contents
with open(outputfile, 'w', newline='') as datafile:

    # Initialize csvwriter
    writer = csv.writer(datafile, delimiter=',')
    
    # Write the header row
    writer.writerow(["Emp Id", "First Name", "Last Name", "DOB", "SSN", "State"])
    
    #Write the zipped rows
    writer.writerows (transformedCSV)
    


        
        
        





