import Lottery
import csv
Num_Lottery_Teams = 14
# TeamList is team rankings form worst at index 0 to first at the end
TeamList=[]
LotteryList=[]
with open('teamrank.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        TeamList.append(row[1])

# Pick List is list of picks with 1st pick at index 0 and last pick at index Num_Lottery_Teams-1
PickList = []
i=0
#takes the worst x number of teams(defined by Num_Lottery_Teams) and places them in lottery 
while i<Num_Lottery_Teams:
    LotteryList.append(TeamList[29-i])
    i+=1
Lottery.rankTeams(LotteryList)
#creating a list containing pick order
i=0
while i < Num_Lottery_Teams:
    PickList.append(Lottery.selectPick())
    i+=1

#tells user the lottery results
i = 14
while i > 0:    
    print ('The ' + str(i) + ' pick in the draft goes to the ' + PickList[i-1])
    i-=1