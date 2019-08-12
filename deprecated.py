#all functions and variabes below are deprecated
Schedule =[]

#take the list of matchups and randomly order them
#deprectaed
def scheduleChanger(matchupsList,currentTeam):
    i=0
    while i<len(Schedule):
        if Schedule[i][0]==currentTeam:
            tempSchedule=Schedule[i]
            matchupsList=deleteDuplicates(matchupsList,tempSchedule)    
            while len(matchupsList)>0:
                #print('matchup')
                maxGame=len(matchupsList)-1
                game = random.randint(0,maxGame)     
                k=1
                while k<len(Schedule[i]):
                    available = weekFree(matchupsList[game],k)
                    #print(available)
                    # and available==True
                    if Schedule[i][k]=='empty' and available==True:
                        Schedule[i][k]=matchupsList[game]
                        del matchupsList[game]
                        k=len(Schedule[i])
                    else:
                        #print('failed if')
                        k+=1
            i=len(Schedule)
        i+=1

#checks if opponent already has a game scheduled
#deprecated
def weekFree(team,week):
    i=0
    while i<len(Schedule):
        if Schedule[i][0]==team:
            #tempSchedule=Schedule[i]
            if Schedule[i][week]=='empty':
                return True
            else:
                return False
            i=len(Schedule)
        i+=1

#take out matchups for already scheduled games
#deprecated
def deleteDuplicates(matchupsList,Schedule):
    i=0
    while i<len(Schedule):
        if Schedule[i]=='empty':
            i+=1
        else:
            k=0
            while k<len(matchupsList):
                if matchupsList[k]==Schedule[i]:
                    del matchupsList[k]
                else:
                    k+=1
            i+=1
    return matchupsList

#get the current schedule of a team
#deprecated
def getCurrentSchedule(team):
    currentSchedule =[]
    for row in Schedule:
        if team == row[0]:
            currentSchedule=row
    return currentSchedule

#fill in games known with opponent and leave unknown games as empty
#deprecated
def writeDuplicates(opponent):
    i=0
    while i<len(Schedule):
        if Schedule[i][0]==opponent:
            k=1
            while k<len(Schedule[i]):
                if Schedule[i][k]!='empty':
                    team = Schedule[i][k]
                    week=k
                    n=0
                    while n<len(Schedule):
                        if Schedule[n][0]==team:
                            if Schedule[n][week]=='empty':
                                Schedule[n][week]=opponent
                        n+=1
                k+=1
        i+=1

def addRoster(player,overall,position):
        i=0
        while i<len(roster[0]):
            if roster[0][i]=='empty':
                roster[0][i]=player
                roster[1][i]=overall
                roster[2][i]=position
                i=len(roster[0])
            elif i == len(roster[0])-1:
                print('max roster size')
            i+=1
        changeRoster()
        hideEmpty()