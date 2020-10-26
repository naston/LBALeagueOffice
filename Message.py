class Message(object):
    def __init__(self,team):
        self.messageType=0
        self.team=team

class draftMessage(Message):
    def __init__(self,roster,draftList, draftOrder, team):
        self.roster=roster
        self.draftList=draftList
        self.draftOrder=draftOrder
        self.team=team
        self.messageType=1
        #maybe include a just drafted, or that can be a seperate message for the waiting page

class FAMessage(Message):
    def __init__(self,team,roster,freeAgents):
        self.roster=roster
        self.team=team
        self.freeAgents=freeAgents
        self.messageType=2

class ScheduleMessage(Message):
    def __init__(self,team,schedule):
        self.team=team
        self.messageType=3
        self.schedule=schedule

class tradeMessage(Message):
    def __init__(self,team, roster, picks, team1, roster1, picks1, team2, roster2, picks2, team3, roster3, picks3):
        self.team=team
        self.roster=roster
        self.picks=picks
        self.team=team1
        self.roster=roster1
        self.picks=picks1
        self.team=team2
        self.roster=roster2
        self.picks=picks2
        self.team=team3
        self.roster=roster3
        self.picks=picks3
        self.messageType=4

class notificationMessage(Message):
    def __init__(self,team,mail):
        self.team=team
        self.mail=mail
        #variable for current mail item the user has expanded and their reaction to it? Maybe a mail type for each mail item(respondable = true) maybe it is a trade request

class testMessageOn(Message):
    def __init__(self,user,color,page):
        self.user=user
        self.color=color
        self.page=page

    def setPage(self,page):
        self.page=page

    def setColor(self,color):
        self.color=color
    
    def getColor(self):
        return self.color

    def getPage(self):
        return self.page