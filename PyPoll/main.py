#---------------------------------------------------------------------------------------
# Import modules for working with Operating Systems and Comma-Separated Value files
#---------------------------------------------------------------------------------------
import os
import csv
#------------------
# define variables
#------------------
total_votes = 0 # create variable total_votes to increment and keep track of the Total Count of Votes.
candidate_list = {} # create empty dictionary to store candidate names (as keys) & votes (as values)
listofcandidates = [] # create empty list to store UNIQUE list of candidate names
ElectionDataPath = os.path.join("PyPoll","Resources","ElectionData.csv") # point to Election data csv file
# Loop through rows to find unique candidate list and count votes for each candidate
with open(ElectionDataPath) as csvfile:
    electiondata = csv.reader(csvfile, delimiter=",") # Read in CSV file
    electiondata_header = next(electiondata) # Define Header
   # Read each row of data after the header
    for row in electiondata:
        total_votes += 1 # Increment row-by-row using variable total_votes. This will ultimately provide our Total Vote Count.
        candidate = row[2] # set variable candidate equal to whatever is in the third column of the row we're currently reading 
        if candidate not in candidate_list: # If this is a new candidate name (not in the dictionary) do two things:
            candidate_list.update({candidate:1}) # First add the candidate name as a key in the dictionary and add one vote as the value (in key-value pair) for that candidate
            listofcandidates.append(candidate) # Second add the candidate name to the list of UNIQUE candidate names
        else: candidate_list[candidate] +=1 # If this is NOT a new candidate name (already in the dictionary) add one vote to this candidate's vote count
#------------------------------------------
#Print the Election Results to the Terminal
#------------------------------------------
print('Election Results') 
print(f'Total Votes: ', total_votes) # Print the total number of votes (for all candidates in the data sheet)
print('-------------------------')
print_count = -1 # The print_count variable is used to increment in the below FOR loop. Starting it at -1 because of the "off by one" error.
for row in listofcandidates: # set number of FOR loop iterations equal to number of candidate names in the LISTOFCANDIDATES list
    print_count += 1 # Increment by 1 using print_count variable
    # print the list of UNIQUE candidates with their percentage of total votes and their number of total votes
    print(f'',listofcandidates[print_count],":","{:0.2%}".format((candidate_list[listofcandidates[print_count]]/total_votes)),"(", candidate_list[listofcandidates[print_count]],")")
print('-------------------------')
print(f'Winner:',max(candidate_list, key=candidate_list.get)) # print the name of the winning candidate
#------------------------------------------
#Save the Election Results as a TXT file
#------------------------------------------
with open('ElectionResults.txt', 'w') as text_file:
    print(f'\n',
    'Election Results','\n',
    'Total Votes: ', total_votes,'\n',
    '-------------------------',
    file=text_file)
    kvcount = -1
    for row in listofcandidates:
        kvcount += 1
        print(f'',listofcandidates[kvcount],':',
        '{:0.2%}'.format((candidate_list[listofcandidates[kvcount]]/total_votes)),'(',
        candidate_list[listofcandidates[kvcount]],')',
        file=text_file)
    print(f'-------------------------','\n',
    'Winner:',max(candidate_list, key=candidate_list.get),'\n',
    file=text_file)