###########################################
#Created By : Mandar R. Gogate
#Created On : 09/13/2019
#Modified On : 09/17/2019
#     Changed script name to main.py
#            : 09/17/2019
#     Changed out file from csv to txt
#Referances : 
#   1. for writing into txt file
#       https://www.geeksforgeeks.org/reading-writing-text-files-python/
#   2. to check key exists or not and validate against value None for dictionary
#       https://www.programiz.com/python-programming/methods/dictionary/get
###########################################
import csv
import os
dElection = os.path.join("D:/MyWork/GeorgiaTech/ClassesWork/3_HomeWork-Python/python-challenge/PyPoll", "election_data.csv")
with open(dElection, newline='', encoding="utf8") as electionFile:
    totalVoteCast = 0
    #defining Set to store unique values of candidates
    candidateSet = set()
    #defining Dictionary to store candidates and their respective votes
    electionDict = {}
    electionReader = csv.reader(electionFile, delimiter=',')
    #storing headers
    headers = next(electionReader, None) 
    for myRow in electionReader:
        totalVoteCast += 1
        candidateSet.add(myRow[2])
        myKey = myRow[2]        
        #checking if key exists in dictionary
        myVal = electionDict.get(myKey)
        #if key doesnt exists, add it and initialize vote count as 1
        #here None is not a string, its a separate data type
        if(myVal == None):
            electionDict[myKey] = 1    
        else:
        #if key exists, increment the vote count 
            electionDict[myKey] = electionDict.get(myKey) + 1

outPath = os.path.join("D:/MyWork/GeorgiaTech/ClassesWork/3_HomeWork-Python/python-challenge/PyPoll", "electionOutput.txt")

#opening file in write mode
outFile = open(outPath, "w+")

#defining function to write both at console and file
def printOnTerminalAndFile(vLine):
    print(vLine)
    outFile.write(vLine)
    outFile.write("\n")


printOnTerminalAndFile("Election Results")
printOnTerminalAndFile("---------------------------------")
printOnTerminalAndFile("Total Votes: " + str(totalVoteCast))
printOnTerminalAndFile("--------------------------------")
finalVotes = []
for n in electionDict:
    printOnTerminalAndFile("{}: {} ({})".format(n, str(round((electionDict[n]/totalVoteCast) * 100)) + ".000%",electionDict[n])) 
    finalVotes.append(electionDict[n])
printOnTerminalAndFile("---------------------------------")
for key, val in electionDict.items():
    if val == max(finalVotes):
        printOnTerminalAndFile("Winner: {}".format(key))
printOnTerminalAndFile("---------------------------------")

#closing file cursor
outFile.close