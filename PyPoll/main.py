#Modules
import os
import csv
# define variables
vote_count = 0
vote = 0
electiondatapath = "PyPoll/Resources/ElectionData.csv" # point to Election data csv file
# create empty dictionary to store candidate names & votes
candidatelist = {}
# create empty list to store candidate names
listofcandidates = []
#Open ElectionData.csv
with open(electiondatapath) as csvfile:
    ElectionData = csv.reader(csvfile, delimiter=',')
    csv_header = next(ElectionData)
    for row in ElectionData:
        vote_count = vote_count + 1
        candidate = row[2]
        if candidate not in candidatelist:
            candidatelist.update({candidate : 1})
            listofcandidates.append(candidate)
        else: 
            candidatelist[candidate] += 1
    print(candidatelist)
    print(vote_count)
    print(listofcandidates)

    