###########################################
#Created By : Mandar R. Gogate
#Created On : 09/17/2019
#Combined both scripts in a single file
#Referances : 
#   1. for writing into txt file
#       https://www.geeksforgeeks.org/reading-writing-text-files-python/
#   2. to check key exists or not and validate against value None for dictionary
#       https://www.programiz.com/python-programming/methods/dictionary/get
###########################################

import csv
import os

#defining function to write both at console and file
def printOnTerminalAndFile(vLine, oFile):
    print(vLine)
    oFile.write(vLine)
    oFile.write("\n")

def processBudgetData():
    dBudget = os.path.join("D:/MyWork/GeorgiaTech/ClassesWork/3_HomeWork-Python/python-challenge/PyBank", "budget_data.csv")
    with open(dBudget, newline='', encoding="utf8") as budgetFile:
        budgetReader = csv.reader(budgetFile, delimiter=',')
        recdCnt=0
        oldProfitAndLoss = 0
        changeInProfitAndLoss = 0
        totalChangeInProfNLoss = 0
        totalProfLoss = 0
        maxProfit = 0
        maxDate = ""
        minProfit = 0
        minDate = ""
        #storing headers
        headers = next(budgetReader, None) 
        for myRow in budgetReader:
            #for first row there won't be any chance in profileAndLoss, so its 0
            if(recdCnt == 0):
                changeInProfitAndLoss = 0
            else:
                changeInProfitAndLoss = int(myRow[1]) - oldProfitAndLoss
                
            totalChangeInProfNLoss += changeInProfitAndLoss
            recdCnt += 1
            totalProfLoss += int(myRow[1])
            if(maxProfit < changeInProfitAndLoss):
                maxProfit = changeInProfitAndLoss
                maxDate = myRow[0]
            if(minProfit > changeInProfitAndLoss):
                minProfit = changeInProfitAndLoss
                minDate = myRow[0]
            #storing profileAndLoss value for next comparison
            oldProfitAndLoss = int(myRow[1])

    outPath = os.path.join("D:/MyWork/GeorgiaTech/ClassesWork/3_HomeWork-Python/python-challenge/PyBank", "budgetDataOutput.csv")
    #opening file in write mode
    outFile = open(outPath, "w+")

    printOnTerminalAndFile("Financial Analysis", outFile)
    printOnTerminalAndFile("---------------------------------", outFile)
    printOnTerminalAndFile("Total Months: {}".format(recdCnt), outFile)
    printOnTerminalAndFile("Total: ${}".format(totalProfLoss), outFile)
    printOnTerminalAndFile("Average Change: ${}".format(round(totalChangeInProfNLoss/(recdCnt-1),2)), outFile)
    printOnTerminalAndFile("Greatest increase in profits: {} (${})".format(maxDate, maxProfit), outFile)
    printOnTerminalAndFile("Greatest decrease in profiles: {} (${})".format(minDate, minProfit), outFile)

    #closing file cursor
    outFile.close

def processElectionData():
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

    outPath = os.path.join("D:/MyWork/GeorgiaTech/ClassesWork/3_HomeWork-Python/python-challenge/PyPoll", "electionOutput.csv")

    #opening file in write mode
    outFile = open(outPath, "w+")

    printOnTerminalAndFile("Election Results", outFile)
    printOnTerminalAndFile("---------------------------------", outFile)
    printOnTerminalAndFile("Total Votes: " + str(totalVoteCast), outFile)
    printOnTerminalAndFile("--------------------------------", outFile)
    finalVotes = []
    for n in electionDict:
        printOnTerminalAndFile("{}: {} ({})".format(n, str(round((electionDict[n]/totalVoteCast) * 100)) + ".000%",electionDict[n]), outFile) 
        finalVotes.append(electionDict[n])
    printOnTerminalAndFile("---------------------------------", outFile)
    for key, val in electionDict.items():
        if val == max(finalVotes):
            printOnTerminalAndFile("Winner: {}".format(key), outFile)
    printOnTerminalAndFile("---------------------------------", outFile)

    #closing file cursor
    outFile.close

#calling budget data function
processBudgetData()
#calling election data function
processElectionData()