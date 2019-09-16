###########################################
#Created By : Mandar R. Gogate
#Created On : 09/13/2019
#Modified On : 09/15/2019
#    ProfileLoss Change derivation logic was not correct.
#Referances : 
#   1. for writing into txt file
#       https://www.geeksforgeeks.org/reading-writing-text-files-python/
#   2. to check key exists or not and validate against value None for dictionary
#       https://www.programiz.com/python-programming/methods/dictionary/get
###########################################
import csv
import os
dBudget = os.path.join("D:/MyWork/GeorgiaTech/ClassesWork/3_HomeWork-Python", "budget_data.csv")
with open(dBudget, newline='', encoding="utf8") as budgetFile:
    budgetReader = csv.reader(budgetFile, delimiter=',')
    recdCnt=0
    oldProfileAndLoss = 0
    changeInProfitAndLoss = 0
    totalChangeInProfNLoss = 0
    totalProfLoss = 0
    maxProfit = 0
    maxDate = ""
    minProfit = 0
    minDate = ""
    headers = next(budgetReader, None) 
    for myRow in budgetReader:
        if(recdCnt == 0):
            changeInProfitAndLoss = 0
        else:
            changeInProfitAndLoss = int(myRow[1]) - oldProfileAndLoss
            
        totalChangeInProfNLoss += changeInProfitAndLoss
        recdCnt += 1
        totalProfLoss += int(myRow[1])
        if(maxProfit < changeInProfitAndLoss):
            maxProfit = changeInProfitAndLoss
            maxDate = myRow[0]
        if(minProfit > changeInProfitAndLoss):
            minProfit = changeInProfitAndLoss
            minDate = myRow[0]
        oldProfileAndLoss = int(myRow[1])

outPath = os.path.join("D:/MyWork/GeorgiaTech/ClassesWork/3_HomeWork-Python", "budgetDataOutput.csv")
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