###########################################
#Created By : Mandar R. Gogate
#Created On : 09/13/2019
#Modified On : 09/15/2019
#    ProfileLoss Change derivation logic was not correct.
#            : 09/17/2019
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

outPath = os.path.join("D:/MyWork/GeorgiaTech/ClassesWork/3_HomeWork-Python/python-challenge/PyBank", "budgetDataOutput.txt")
#opening file in write mode
outFile = open(outPath, "w+")

#defining function to write both at console and file
def printOnTerminalAndFile(vLine):
    print(vLine)
    outFile.write(vLine)
    outFile.write("\n")

printOnTerminalAndFile("Financial Analysis")
printOnTerminalAndFile("---------------------------------")
printOnTerminalAndFile("Total Months: {}".format(recdCnt))
printOnTerminalAndFile("Total: ${}".format(totalProfLoss))
printOnTerminalAndFile("Average Change: ${}".format(round(totalChangeInProfNLoss/(recdCnt-1),2)))
printOnTerminalAndFile("Greatest increase in profits: {} (${})".format(maxDate, maxProfit))
printOnTerminalAndFile("Greatest decrease in profiles: {} (${})".format(minDate, minProfit))

#closing file cursor
outFile.close