## PyPoll
## Christiaan Van den Akker

# import modules
import os
import csv
from collections import Counter

# Create lists to store column data
Voter_ID = []
County = []
Candidate = []

# Ask user which file to open and transform
user_input = input("Which polling results would you like to open? 1 or 2 ? " )

# Set the paths for the two csv files
csvpath1 = os.path.join("raw_data","election_data_1.csv")
csvpath2 = os.path.join("raw_data","election_data_2.csv")

# Tie the user's choice to the file to be opened.
if user_input=="1":
    file_choice = csvpath1
    print("You have chosen election_data_1")
elif user_input=="2":
    file_choice = csvpath2
    print("You have chosen election_data_2")
else:
    file_choice = csvpath2
    print("You have not made a valid choice. Opening election_data_2")
   
# Open the csv file
with open(file_choice, newline ='') as csvfile1:
    csvreader1 = csv.reader(csvfile1, delimiter=",")
  
    # Skip the header row
    next(csvreader1)

    # Create lists for each column
    for row in csvreader1:
        Voter_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
        
    # Count the total voters
    voter_count = len(Voter_ID) 
    print("Voter Count: " + str(voter_count))
    
    # Get a count of the unique candidates through collection.Counter
    candidates = Candidate         
    c = Counter(candidates)
    
    print("Candidates and votes = " + str(c.items()))
 



    # Write to the text file
with open("Output.txt", "w") as text_file:
    text_file.write("Election Results" + "\n")
    text_file.write("-------------------------" + "\n")
    text_file.write("Total Votes: " + str(voter_count) + "\n")
    text_file.write("-------------------------" + "\n")

    





