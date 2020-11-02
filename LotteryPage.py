import tkinter as tk
import pandas as pd
import numpy as np
import random

lottery_num=14
class Lottery(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        self.homeButton = tk.Button(self,text='Home',command=lambda:self.home())#controller.show_frame("StartPage"))
        self.homeButton.place(relx=0,rely=0,relwidth=0.05,relheight=0.1)
        self.lottery = tk.Frame(self)
        self.lottery.place(relx=0.05,rely=0,relwidth=0.95,relheight=1)

        self.title = tk.Label(self.lottery, text='Lottery')
        self.title.place(relx=0,rely=0,relwidth=1,relheight=0.1)

        self.standings = self.getStandings()
        self.lottery_teams = self.standings.iloc[len(self.standings)-lottery_num:len(self.standings)+1]
        #self.lottery_teams.sort_values(by=['Wins'], ascending=True)
        self.regular_teams = self.standings.iloc[0:len(self.standings)-lottery_num]
        self.lotteryList = []

        self.allocateBallots()
        self.runLottery()
        self.lotteryWindow()

    def allocateBallots(self):
        print(self.lottery_teams['Rank'].max())
        self.createOdds(self.lottery_teams.iloc[0]['Team'], 14)
        self.createOdds(self.lottery_teams.iloc[1]['Team'], 14)
        self.createOdds(self.lottery_teams.iloc[2]['Team'], 14)
        self.createOdds(self.lottery_teams.iloc[3]['Team'], 12)
        self.createOdds(self.lottery_teams.iloc[4]['Team'], 11)
        self.createOdds(self.lottery_teams.iloc[5]['Team'], 9)
        self.createOdds(self.lottery_teams.iloc[6]['Team'], 6)
        self.createOdds(self.lottery_teams.iloc[7]['Team'], 6)
        self.createOdds(self.lottery_teams.iloc[8]['Team'], 6)
        self.createOdds(self.lottery_teams.iloc[9]['Team'], 3)
        self.createOdds(self.lottery_teams.iloc[10]['Team'], 2)
        self.createOdds(self.lottery_teams.iloc[11]['Team'], 1)
        self.createOdds(self.lottery_teams.iloc[12]['Team'], 1)
        self.createOdds(self.lottery_teams.iloc[13]['Team'], 1)
    
    def createOdds(self, teamName, ballots):
        for i in range(0,ballots):
            self.lotteryList.append(teamName)

    def selectPick(self):
        mult=len(self.lotteryList)
        number = random.randint(0,mult-1)
        pick = self.lotteryList[number]
        self.removeTeam(pick)
        return pick

    def removeTeam(self, teamName):
        i=0
        while i<len(self.lotteryList):
            if self.lotteryList[i]==teamName:
                    del self.lotteryList[i]
            else:
                    i+=1

    def runLottery(self):
        self.picks = pd.DataFrame(columns=['Pick', 'Team'])
        for i in range(len(self.lottery_teams)):
            pick = self.selectPick()
            p = pd.Series(data=[i+1, pick],index= self.picks.columns)
            self.picks = self.picks.append(p,ignore_index=True)
        for i in range(len(self.regular_teams)):
            pick = self.regular_teams.iloc[i]['Team']
            p = pd.Series(data=[i+1+lottery_num, pick],index= self.picks.columns)
            self.picks = self.picks.append(p,ignore_index=True) 
        self.picks=self.picks.sort_values(by=['Pick'],ascending=True)   
        self.picks.to_csv('Lottery.csv', index=False)  

    def lotteryWindow(self):
        p1 = tk.Label(self.lottery, text=self.picks.iloc[0]['Team'])
        p2 = tk.Label(self.lottery, text=self.picks.iloc[1]['Team'])
        p3 = tk.Label(self.lottery, text=self.picks.iloc[2]['Team'])
        p4 = tk.Label(self.lottery, text=self.picks.iloc[3]['Team'])
        p5 = tk.Label(self.lottery, text=self.picks.iloc[4]['Team'])
        p6 = tk.Label(self.lottery, text=self.picks.iloc[5]['Team'])
        p7 = tk.Label(self.lottery, text=self.picks.iloc[6]['Team'])
        p8 = tk.Label(self.lottery, text=self.picks.iloc[7]['Team'])
        p9 = tk.Label(self.lottery, text=self.picks.iloc[8]['Team'])
        p10 = tk.Label(self.lottery, text=self.picks.iloc[9]['Team'])
        p11 = tk.Label(self.lottery, text=self.picks.iloc[10]['Team'])
        p12 = tk.Label(self.lottery, text=self.picks.iloc[11]['Team'])
        p13 = tk.Label(self.lottery, text=self.picks.iloc[12]['Team'])
        p14 = tk.Label(self.lottery, text=self.picks.iloc[13]['Team'])
        p15 = tk.Label(self.lottery, text=self.picks.iloc[14]['Team'])
        p16 = tk.Label(self.lottery, text=self.picks.iloc[15]['Team'])
        p17 = tk.Label(self.lottery, text=self.picks.iloc[16]['Team'])
        p18 = tk.Label(self.lottery, text=self.picks.iloc[17]['Team'])
        p19 = tk.Label(self.lottery, text=self.picks.iloc[18]['Team'])
        p20 = tk.Label(self.lottery, text=self.picks.iloc[19]['Team'])
        p21 = tk.Label(self.lottery, text=self.picks.iloc[20]['Team'])
        p22 = tk.Label(self.lottery, text=self.picks.iloc[21]['Team'])
        p23 = tk.Label(self.lottery, text=self.picks.iloc[22]['Team'])
        p24 = tk.Label(self.lottery, text=self.picks.iloc[23]['Team'])
        p25 = tk.Label(self.lottery, text=self.picks.iloc[24]['Team'])
        p26 = tk.Label(self.lottery, text=self.picks.iloc[25]['Team'])
        p27 = tk.Label(self.lottery, text=self.picks.iloc[26]['Team'])
        p28 = tk.Label(self.lottery, text=self.picks.iloc[27]['Team'])
        p29 = tk.Label(self.lottery, text=self.picks.iloc[28]['Team'])
        p30 = tk.Label(self.lottery, text=self.picks.iloc[29]['Team'])

        r1 = tk.Label(self.lottery, text='1')
        r2 = tk.Label(self.lottery, text='2')
        r3 = tk.Label(self.lottery, text='3')
        r4 = tk.Label(self.lottery, text='4')
        r5 = tk.Label(self.lottery, text='5')
        r6 = tk.Label(self.lottery, text='6')
        r7 = tk.Label(self.lottery, text='7')
        r8 = tk.Label(self.lottery, text='8')
        r9 = tk.Label(self.lottery, text='9')
        r10 = tk.Label(self.lottery, text='10')
        r11 = tk.Label(self.lottery, text='11')
        r12 = tk.Label(self.lottery, text='12')
        r13 = tk.Label(self.lottery, text='13')
        r14 = tk.Label(self.lottery, text='14')
        r15 = tk.Label(self.lottery, text='15')
        r16 = tk.Label(self.lottery, text='16')
        r17 = tk.Label(self.lottery, text='17')
        r18 = tk.Label(self.lottery, text='18')
        r19 = tk.Label(self.lottery, text='19')
        r20 = tk.Label(self.lottery, text='20')
        r21 = tk.Label(self.lottery, text='21')
        r22 = tk.Label(self.lottery, text='22')
        r23 = tk.Label(self.lottery, text='23')
        r24 = tk.Label(self.lottery, text='24')
        r25 = tk.Label(self.lottery, text='25')
        r26 = tk.Label(self.lottery, text='26')
        r27 = tk.Label(self.lottery, text='27')
        r28 = tk.Label(self.lottery, text='28')
        r29 = tk.Label(self.lottery, text='29')
        r30 = tk.Label(self.lottery, text='30')

        p1.place(relx=0.2,rely=0.1,relwidth=0.8,relheight=0.03)
        p2.place(relx=0.2,rely=0.13,relwidth=0.8,relheight=0.03)
        p3.place(relx=0.2,rely=0.16,relwidth=0.8,relheight=0.03)
        p4.place(relx=0.2,rely=0.19,relwidth=0.8,relheight=0.03)
        p5.place(relx=0.2,rely=0.22,relwidth=0.8,relheight=0.03)
        p6.place(relx=0.2,rely=0.25,relwidth=0.8,relheight=0.03)
        p7.place(relx=0.2,rely=0.28,relwidth=0.8,relheight=0.03)
        p8.place(relx=0.2,rely=0.31,relwidth=0.8,relheight=0.03)
        p9.place(relx=0.2,rely=0.34,relwidth=0.8,relheight=0.03)
        p10.place(relx=0.2,rely=0.37,relwidth=0.8,relheight=0.03)
        p11.place(relx=0.2,rely=0.4,relwidth=0.8,relheight=0.03)
        p12.place(relx=0.2,rely=0.43,relwidth=0.8,relheight=0.03)
        p13.place(relx=0.2,rely=0.46,relwidth=0.8,relheight=0.03)
        p14.place(relx=0.2,rely=0.49,relwidth=0.8,relheight=0.03)
        p15.place(relx=0.2,rely=0.52,relwidth=0.8,relheight=0.03)
        p16.place(relx=0.2,rely=0.55,relwidth=0.8,relheight=0.03)
        p17.place(relx=0.2,rely=0.58,relwidth=0.8,relheight=0.03)
        p18.place(relx=0.2,rely=0.61,relwidth=0.8,relheight=0.03)
        p19.place(relx=0.2,rely=0.64,relwidth=0.8,relheight=0.03)
        p20.place(relx=0.2,rely=0.67,relwidth=0.8,relheight=0.03)
        p21.place(relx=0.2,rely=0.70,relwidth=0.8,relheight=0.03)
        p22.place(relx=0.2,rely=0.73,relwidth=0.8,relheight=0.03)
        p23.place(relx=0.2,rely=0.76,relwidth=0.8,relheight=0.03)
        p24.place(relx=0.2,rely=0.79,relwidth=0.8,relheight=0.03)
        p25.place(relx=0.2,rely=0.82,relwidth=0.8,relheight=0.03)
        p26.place(relx=0.2,rely=0.85,relwidth=0.8,relheight=0.03)
        p27.place(relx=0.2,rely=0.88,relwidth=0.8,relheight=0.03)
        p28.place(relx=0.2,rely=0.91,relwidth=0.8,relheight=0.03)
        p29.place(relx=0.2,rely=0.94,relwidth=0.8,relheight=0.03)
        p30.place(relx=0.2,rely=0.97,relwidth=0.8,relheight=0.03)

        r1.place(relx=0,rely=0.1,relwidth=0.2,relheight=0.03)
        r2.place(relx=0,rely=0.13,relwidth=0.2,relheight=0.03)
        r3.place(relx=0,rely=0.16,relwidth=0.2,relheight=0.03)
        r4.place(relx=0,rely=0.19,relwidth=0.2,relheight=0.03)
        r5.place(relx=0,rely=0.22,relwidth=0.2,relheight=0.03)
        r6.place(relx=0,rely=0.25,relwidth=0.2,relheight=0.03)
        r7.place(relx=0,rely=0.28,relwidth=0.2,relheight=0.03)
        r8.place(relx=0,rely=0.31,relwidth=0.2,relheight=0.03)
        r9.place(relx=0,rely=0.34,relwidth=0.2,relheight=0.03)
        r10.place(relx=0,rely=0.37,relwidth=0.2,relheight=0.03)
        r11.place(relx=0,rely=0.4,relwidth=0.2,relheight=0.03)
        r12.place(relx=0,rely=0.43,relwidth=0.2,relheight=0.03)
        r13.place(relx=0,rely=0.46,relwidth=0.2,relheight=0.03)
        r14.place(relx=0,rely=0.49,relwidth=0.2,relheight=0.03)
        r15.place(relx=0,rely=0.52,relwidth=0.2,relheight=0.03)
        r16.place(relx=0,rely=0.55,relwidth=0.2,relheight=0.03)
        r17.place(relx=0,rely=0.58,relwidth=0.2,relheight=0.03)
        r18.place(relx=0,rely=0.61,relwidth=0.2,relheight=0.03)
        r19.place(relx=0,rely=0.64,relwidth=0.2,relheight=0.03)
        r20.place(relx=0,rely=0.67,relwidth=0.2,relheight=0.03)
        r21.place(relx=0,rely=0.70,relwidth=0.2,relheight=0.03)
        r22.place(relx=0,rely=0.73,relwidth=0.2,relheight=0.03)
        r23.place(relx=0,rely=0.76,relwidth=0.2,relheight=0.03)
        r24.place(relx=0,rely=0.79,relwidth=0.2,relheight=0.03)
        r25.place(relx=0,rely=0.82,relwidth=0.2,relheight=0.03)
        r26.place(relx=0,rely=0.85,relwidth=0.2,relheight=0.03)
        r27.place(relx=0,rely=0.88,relwidth=0.2,relheight=0.03)
        r28.place(relx=0,rely=0.91,relwidth=0.2,relheight=0.03)
        r29.place(relx=0,rely=0.94,relwidth=0.2,relheight=0.03)
        r30.place(relx=0,rely=0.97,relwidth=0.2,relheight=0.03)

    def getStandings(self):
        standings = pd.read_csv('teamrank.csv')
        return standings

"""
-This will redo the lottery every time I open the app at this point
-I will probably need to do a create lottery instead of this and have a seperate page for showing lottery
"""