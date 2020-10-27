import random
import csv


previousSchedule = []
newSchedule = []
Weeks = []
Games=[]
#set temporary lists to previous year
def start():
    with open('Schedule.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            previousSchedule.append(row)
    i = 1
    while i < len(previousSchedule[0]):
        Weeks.append(i)  
        i+=1
    with open('Schedule.csv') as file1:
        rCSV = csv.reader(file1,delimiter=',')
        for row in rCSV:
            newSchedule.append(row)

#changes values in newSchedule to random weeks from previousSchedule
def setWeeks():
    i=1
    clearSchedule()
    while len(Weeks)>0:
        if len(Weeks)>1:
            lastWeek=len(Weeks)-1
            selectWeek = random.randint(1,lastWeek)
            week = Weeks[selectWeek]
            k=0
        else:
            week = Weeks[0]
        k=0
        while k<len(previousSchedule):
            Games.append(previousSchedule[k][week])
            k+=1
        Weeks.remove(week)
        n=0
        while n<len(newSchedule):
            newSchedule[n][i]=Games[n]
            n+=1
        i+=1
        resetGames()

#resets the list carrying a random week of games to empty
def resetGames():
    while len(Games)>0:
        del Games[0]

#clears last years schedule to take this years schedule        
def clearSchedule():
    f = open("Schedule.csv",'w')
    f.truncate()
    f.close()

#write league schedule to csv
def writeSchedule():
    with open('Schedule.csv','w',newline='') as csvfile:
        writeCSV=csv.writer(csvfile, delimiter=',')
        for row in newSchedule:
            writeCSV.writerow(row)
            print(row)