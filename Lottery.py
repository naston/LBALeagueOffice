import random
#Import csv of rankings that will list from last to first
LotteryList = []
def createOdds(TeamName, Percentage):
    i=0
    while i<Percentage:
        LotteryList.append(TeamName)
        i += 1

def rankTeams(TeamList):
    createOdds(TeamList[0], 14)
    createOdds(TeamList[1], 14)
    createOdds(TeamList[2], 14)
    createOdds(TeamList[3], 12)
    createOdds(TeamList[4], 11)
    createOdds(TeamList[5], 9)
    createOdds(TeamList[6], 6)
    createOdds(TeamList[7], 6)
    createOdds(TeamList[8], 6)
    createOdds(TeamList[9], 3)
    createOdds(TeamList[10], 2)
    createOdds(TeamList[11], 1)
    createOdds(TeamList[12], 1)
    createOdds(TeamList[13], 1)

def removeTeam(TeamName):
    i=0
    while i<len(LotteryList):
        if LotteryList[i]==TeamName:
                del LotteryList[i]
        else:
                i+=1

def selectPick():
    mult=len(LotteryList)
    number = random.randint(0,mult-1)
    pick = LotteryList[number]
    removeTeam(pick)
    return pick