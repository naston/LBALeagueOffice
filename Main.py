import Lottery
import csv

TeamList=[]
LotteryList=[]
with open('teamrank.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        TeamList.append(row[1])
# TeamList is team rankings form worst at 0 to first at end
# Pick List is list of picks with 1st pick at 0 and last pick at 13
PickList = []
i=0
while i<14:
    LotteryList.append(TeamList[29-i])
    i+=1
Lottery.rankTeams(LotteryList)
#while this for all 14 picks
i=0
while i < 14:
    PickList.append(Lottery.selectPick())
    i+=1

# while through PickList backwards
i = 14
while i > 0:    
    print ('The ' + str(i) + ' pick in the draft goes to the ' + PickList[i-1])
    i-=1