import tkinter as tk
import pandas as pd
import numpy as np
#scheduler needs to be changed to be in column form team1, team2, week

class Results(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.weekStatus = self.getWeekStatus()
        self.standings = self.getCurrentStandings()
        week = int((self.standings['Wins'].sum() + self.standings['Losses'].sum()) / len(self.standings)) + 1
        if week!=self.weekStatus['Week'].iloc[0]:
           self.newWeek(week)
        self.games = self.getThisWeek(week)

        #I may want to add getting the currents weeks status from a csv so that I can add games mid week and not worry about over adding games

        self.homeButton = tk.Button(self,text='Home',command=lambda:self.home())#controller.show_frame("StartPage"))
        self.homeButton.place(relx=0,rely=0,relwidth=0.05,relheight=0.1)
        self.thisWeek = tk.Frame(self)
        self.thisWeek.place(relx=0.05,rely=0,relwidth=0.95,relheight=1)
        self.titlelabel=tk.Label(self.thisWeek,text='This Weeks Games')
        self.titlelabel.place(relx=0,rely=0,relwidth=1,relheight=0.1)

        self.resultsWindow()

    def home(self):
        self.weekStatus.to_csv('weekStatus.csv', index=False)
        self.controller.show_frame("StartPage")

    def newWeek(self,week):
        #I want to go here if the week calculated above does not equal the week in the first column of the current week status
        #here i overwrite with a clean week status csv
        data = {
            'Week':week,
            'G1':[0],
            'G2':[0],
            'G3':[0]
        }
        """    ,
            'G4':0,
            'G5':0,
            'G6':0,
            'G7':0,
            'G8':0,
            'G9':0,
            'G10':0,
            'G11':0,
            'G12':0,
            'G13':0,
            'G14':0,
            'G15':0
        }
        """
        self.weekStatus = pd.DataFrame(data)
        self.weekStatus.to_csv('weekStatus.csv', index=False)

    def getCurrentStandings(self):
        standings = pd.read_csv('Standings.csv')
        return standings

    def getThisWeek(self, week):
        games = pd.read_csv('Schedule.csv')
        games = games[games['Week']==week]
        return games

    def getWeekStatus(self):
        #here I grab the week status df and return it
        weekStatus = pd.read_csv('WeekStatus.csv')
        return weekStatus

    def setResults(self, game_num, winner):
        #i think that we should pass on a game number and a 0 or 1 for which team won
        #then we want to hide both buttons for the game passed
        if winner==1:
            winning_team=self.games.iloc[game_num]['Team2']
            losing_team=self.games.iloc[game_num]['Team1']
        else:
            winning_team=self.games.iloc[game_num]['Team1']
            losing_team=self.games.iloc[game_num]['Team2']
        #test to make sure that I can just add one like this
        self.standings.loc[self.standings['Team']==winning_team,'Wins'] += 1
        self.standings.loc[self.standings['Team']==losing_team,'Losses'] += 1

        #switch case for hiding buttons
        if game_num == 0:
            self.g1t1.place_forget()
            self.g1t2.place_forget()
            self.weekStatus['G1'].iloc[0] = 1
        elif game_num == 1:
            self.g2t1.place_forget()
            self.g2t2.place_forget()
            self.weekStatus['G2'].iloc[0] = 1
        elif game_num == 2:
            self.g3t1.place_forget()
            self.g3t2.place_forget()
            self.weekStatus['G3'].iloc[0] = 1
        """
        elif game_num == 3:
            self.g4t1.place_forget()
            self.g4t2.place_forget()
            self.weekStatus['G4'] = 1
        elif game_num == 4:
            self.g5t1.place_forget()
            self.g5t2.place_forget()
            self.weekStatus['G5'] = 1
        elif game_num == 5:
            self.g6t1.place_forget()
            self.g6t2.place_forget()
            self.weekStatus['G6'] = 1
        elif game_num == 6:
            self.g7t1.place_forget()
            self.g7t2.place_forget()
            self.weekStatus['G7'] = 1
        elif game_num == 7:
            self.g8t1.place_forget()
            self.g8t2.place_forget()
            self.weekStatus['G8'] = 1
        elif game_num == 8:
            self.g9t1.place_forget()
            self.g9t2.place_forget()
            self.weekStatus['G9'] = 1
        elif game_num == 9:
            self.g10t1.place_forget()
            self.g10t2.place_forget()
            self.weekStatus['G10'] = 1
        elif game_num == 10:
            self.g11t1.place_forget()
            self.g11t2.place_forget()
            self.weekStatus['G11'] = 1
        elif game_num == 11:
            self.g12t1.place_forget()
            self.g12t2.place_forget()
            self.weekStatus['G12'] = 1
        elif game_num == 12:
            self.g13t1.place_forget()
            self.g13t2.place_forget()
            self.weekStatus['G13'] = 1
        elif game_num == 13:
            self.g14t1.place_forget()
            self.g14t2.place_forget()
            self.weekStatus['G14'] = 1
        elif game_num == 14:
            self.g15t1.place_forget()
            self.g15t2.place_forget()
            self.weekStatus['G15'] = 1
        """
        self.weekStatus.to_csv('weekStatus.csv', index=False)
        self.writeStandings()

    def resultsWindow(self):
        self.g1 = tk.Label(self.thisWeek, text = self.games.iloc[0]['Team1'] + ' .vs ' + self.games.iloc[0]['Team2'])
        self.g2 = tk.Label(self.thisWeek, text = self.games.iloc[1]['Team1'] + ' .vs ' + self.games.iloc[1]['Team2'])
        self.g3 = tk.Label(self.thisWeek, text = self.games.iloc[2]['Team1'] + ' .vs ' + self.games.iloc[2]['Team2'])
        """
        self.g4 = tk.Label(self.thisWeek, text = self.games.iloc[3]['Team1'] + ' .vs ' + self.games.iloc[3]['Team2'])
        self.g5 = tk.Label(self.thisWeek, text = self.games.iloc[4]['Team1'] + ' .vs ' + self.games.iloc[4]['Team2'])
        self.g6 = tk.Label(self.thisWeek, text = self.games.iloc[5]['Team1'] + ' .vs ' + self.games.iloc[5]['Team2'])
        self.g7 = tk.Label(self.thisWeek, text = self.games.iloc[6]['Team1'] + ' .vs ' + self.games.iloc[6]['Team2'])
        self.g8 = tk.Label(self.thisWeek, text = self.games.iloc[7]['Team1'] + ' .vs ' + self.games.iloc[7]['Team2'])
        self.g9 = tk.Label(self.thisWeek, text = self.games.iloc[8]['Team1'] + ' .vs ' + self.games.iloc[8]['Team2'])
        self.g10 = tk.Label(self.thisWeek, text = self.games.iloc[9]['Team1'] + ' .vs ' + self.games.iloc[9]['Team2'])
        self.g11 = tk.Label(self.thisWeek, text = self.games.iloc[10]['Team1'] + ' .vs ' + self.games.iloc[10]['Team2'])
        self.g12 = tk.Label(self.thisWeek, text = self.games.iloc[11]['Team1'] + ' .vs ' + self.games.iloc[11]['Team2'])
        self.g13 = tk.Label(self.thisWeek, text = self.games.iloc[12]['Team1'] + ' .vs ' + self.games.iloc[12]['Team2'])
        self.g14 = tk.Label(self.thisWeek, text = self.games.iloc[13]['Team1'] + ' .vs ' + self.games.iloc[13]['Team2'])
        self.g15 = tk.Label(self.thisWeek, text = self.games.iloc[14]['Team1'] + ' .vs ' + self.games.iloc[14]['Team2'])
        """

        self.g1.place(relx=0,rely=0.1,relwidth=1,relheight=0.06)
        self.g2.place(relx=0,rely=0.16,relwidth=1,relheight=0.06)
        self.g3.place(relx=0,rely=0.22,relwidth=1,relheight=0.06)

        """
        self.g4.place(relx=0,rely=0.28,relwidth=1,relheight=0.06)
        self.g5.place(relx=0,rely=0.34,relwidth=1,relheight=0.06)
        self.g6.place(relx=0,rely=0.4,relwidth=1,relheight=0.06)
        self.g7.place(relx=0,rely=0.46,relwidth=1,relheight=0.06)
        self.g8.place(relx=0,rely=0.52,relwidth=1,relheight=0.06)
        self.g9.place(relx=0,rely=0.58,relwidth=1,relheight=0.06)
        self.g10.place(relx=0,rely=0.64,relwidth=1,relheight=0.06)
        self.g11.place(relx=0,rely=0.70,relwidth=1,relheight=0.06)
        self.g12.place(relx=0,rely=0.76,relwidth=1,relheight=0.06)
        self.g13.place(relx=0,rely=0.82,relwidth=1,relheight=0.06)
        self.g14.place(relx=0,rely=0.88,relwidth=1,relheight=0.06)
        self.g15.place(relx=0,rely=0.94,relwidth=1,relheight=0.06)
        """

        self.g1t1 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(0,0))
        self.g2t1 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(1,0))
        self.g3t1 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(2,0))

        """
        self.g4t1 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(3,0))
        self.g5t1 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(4,0))
        self.g6t1 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(5,0))
        self.g7t1 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(6,0))
        self.g8t1 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(7,0))
        self.g9t1 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(8,0))
        self.g10t1 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(9,0))
        self.g11t1 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(10,0))
        self.g12t1 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(11,0))
        self.g13t1 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(12,0))
        self.g14t1 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(13,0))
        self.g15t1 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(14,0))
        """

        self.g1t2 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(0,1))
        self.g2t2 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(1,1))
        self.g3t2 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(2,1))

        """
        self.g4t2 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(3,1))
        self.g5t2 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(4,1))
        self.g6t2 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(5,1))
        self.g7t2 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(6,1))
        self.g8t2 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(7,1))
        self.g9t2 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(8,1))
        self.g10t2 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(9,1))
        self.g11t2 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(10,1))
        self.g12t2 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(11,1))
        self.g13t2 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(12,1))
        self.g14t2 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(13,1))
        self.g15t2 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(14,1))
        """
        
        if self.weekStatus['G1'].iloc[0] == 0:
            self.g1t1.place(relx=0,rely=0.1,relwidth=0.1,relheight=0.06)
            self.g1t2.place(relx=0.9,rely=0.1,relwidth=0.1,relheight=0.06)
        if self.weekStatus['G2'].iloc[0] == 0:  
            self.g2t1.place(relx=0,rely=0.16,relwidth=0.1,relheight=0.06)
            self.g2t2.place(relx=0.9,rely=0.16,relwidth=0.1,relheight=0.06)
        if self.weekStatus['G3'].iloc[0] == 0:  
            self.g3t1.place(relx=0,rely=0.22,relwidth=0.1,relheight=0.06)
            self.g3t2.place(relx=0.9,rely=0.22,relwidth=0.1,relheight=0.06)
        """
        if self.weekStatus['G4'] == 0:  
            self.g4t1.place(relx=0,rely=0.28,relwidth=0.1,relheight=0.06)
            self.g4t2.place(relx=0.9,rely=0.28,relwidth=0.1,relheight=0.06)
        if self.weekStatus['G5'] == 0:  
            self.g5t1.place(relx=0,rely=0.34,relwidth=0.1,relheight=0.06)
            self.g5t2.place(relx=0.9,rely=0.34,relwidth=0.1,relheight=0.06)
        if self.weekStatus['G6'] == 0:  
            self.g6t1.place(relx=0,rely=0.4,relwidth=0.1,relheight=0.06)
            self.g6t2.place(relx=0.9,rely=0.4,relwidth=0.1,relheight=0.06)
        if self.weekStatus['G7'] == 0:  
            self.g7t1.place(relx=0,rely=0.46,relwidth=0.1,relheight=0.06)
            self.g7t2.place(relx=0.9,rely=0.46,relwidth=0.1,relheight=0.06)
        if self.weekStatus['G8'] == 0:  
            self.g8t1.place(relx=0,rely=0.52,relwidth=0.1,relheight=0.06)
            self.g8t2.place(relx=0.9,rely=0.52,relwidth=0.1,relheight=0.06)
        if self.weekStatus['G9'] == 0:  
            self.g9t1.place(relx=0,rely=0.58,relwidth=0.1,relheight=0.06)
            self.g9t2.place(relx=0.9,rely=0.58,relwidth=0.1,relheight=0.06)
        if self.weekStatus['G10'] == 0:  
            self.g10t1.place(relx=0,rely=0.64,relwidth=0.1,relheight=0.06)
            self.g10t2.place(relx=0.9,rely=0.64,relwidth=0.1,relheight=0.06)
        if self.weekStatus['G11'] == 0:  
            self.g11t1.place(relx=0,rely=0.70,relwidth=0.1,relheight=0.06)
            self.g11t2.place(relx=0.9,rely=0.70,relwidth=0.1,relheight=0.06)
        if self.weekStatus['G12'] == 0:  
            self.g12t1.place(relx=0,rely=0.76,relwidth=0.1,relheight=0.06)
            self.g12t2.place(relx=0.9,rely=0.76,relwidth=0.1,relheight=0.06)
        if self.weekStatus['G13'] == 0:  
            self.g13t1.place(relx=0,rely=0.82,relwidth=0.1,relheight=0.06)
            self.g13t2.place(relx=0.9,rely=0.82,relwidth=0.1,relheight=0.06)
        if self.weekStatus['G14'] == 0:  
            self.g14t1.place(relx=0,rely=0.88,relwidth=0.1,relheight=0.06)
            self.g14t2.place(relx=0.9,rely=0.88,relwidth=0.1,relheight=0.06)
        if self.weekStatus['G15'] == 0:  
            self.g15t1.place(relx=0,rely=0.94,relwidth=0.1,relheight=0.06)
            self.g15t2.place(relx=0.9,rely=0.94,relwidth=0.1,relheight=0.06)
        """

    def  writeStandings(self):
        #invert this sort pls
        self.standings = self.standings.sort_values(by=['Wins'],ascending=False)
        self.standings.to_csv('Standings.csv', index=False)
        week = int((self.standings['Wins'].sum() + self.standings['Losses'].sum()) / len(self.standings)) + 1
        if week!=self.weekStatus['Week'].iloc[0]:
            self.newWeek(week)
            self.resultsWindow()

class PlayoffResults(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        self.homeButton = tk.Button(self,text='Home',command=lambda:controller.show_frame("StartPage"))
        self.homeButton.place(relx=0,rely=0,relwidth=0.05,relheight=0.1)
        self.bracket = tk.Frame(self)
        self.bracket.place(relx=0.05,rely=0.1,relwidth=0.95,relheight=1)
        self.titlelabel=tk.Label(self,text='Playoff Bracket')
        self.titlelabel.place(relx=0.05,rely=0,relwidth=0.95,relheight=0.1)
        self.matchups = self.getMatchups()
        self.bracketWindow()
    
    def bracketWindow(self):
        self.round1=tk.Frame(self.bracket)
        self.round1.place(relx=0,rely=0,relwidth=0.33,relheight=1)
        self.round2=tk.Frame(self.bracket)
        self.round2.place(relx=0.33,rely=0,relwidth=0.33,relheight=1)
        self.round3=tk.Frame(self.bracket)
        self.round3.place(relx=0.66,rely=0,relwidth=0.33,relheight=1)

        self.r1g1=tk.Frame(self.round1)
        self.r1g2=tk.Frame(self.round1)
        self.r1g3=tk.Frame(self.round1)
        self.r1g4=tk.Frame(self.round1)

        self.r1g1.place(relx=0.1,rely=0.04,relwidth=0.8,relheight=0.2)
        self.r1g2.place(relx=0.1,rely=0.28,relwidth=0.8,relheight=0.2)
        self.r1g3.place(relx=0.1,rely=0.52,relwidth=0.8,relheight=0.2)
        self.r1g4.place(relx=0.1,rely=0.76,relwidth=0.8,relheight=0.2)

        self.r2g1=tk.Frame(self.round2)
        self.r2g2=tk.Frame(self.round2)

        self.r2g1.place(relx=0.1,rely=0.16,relwidth=0.8, relheight=0.2)
        self.r2g2.place(relx=0.1,rely=0.64,relwidth=0.8, relheight=0.2)
        
        self.r3g1=tk.Frame(self.round3)
        self.r3g1.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.2)

        self.setCurrentRound()

    def setCurrentRound(self):
        self.r1g1t1 = tk.Label(self.r1g1,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==1)].iloc[0]['Team1'])
        self.r1g1t2 = tk.Label(self.r1g1,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==1)].iloc[0]['Team2'])
        self.r1g1r1 = tk.Label(self.r1g1,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==1)].iloc[0]['Rank1'])
        self.r1g1r2 = tk.Label(self.r1g1,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==1)].iloc[0]['Rank2'])
        self.r1g1w1 = tk.Label(self.r1g1,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==1)].iloc[0]['Win1'])
        self.r1g1w2 = tk.Label(self.r1g1,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==1)].iloc[0]['Win2'])

        self.r1g2t1 = tk.Label(self.r1g2,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==2)].iloc[0]['Team1'])
        self.r1g2t2 = tk.Label(self.r1g2,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==2)].iloc[0]['Team2'])
        self.r1g2r1 = tk.Label(self.r1g2,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==2)].iloc[0]['Rank1'])
        self.r1g2r2 = tk.Label(self.r1g2,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==2)].iloc[0]['Rank2'])
        self.r1g2w1 = tk.Label(self.r1g2,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==2)].iloc[0]['Win1'])
        self.r1g2w2 = tk.Label(self.r1g2,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==2)].iloc[0]['Win2'])

        self.r1g3t1 = tk.Label(self.r1g3,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==3)].iloc[0]['Team1'])
        self.r1g3t2 = tk.Label(self.r1g3,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==3)].iloc[0]['Team2'])
        self.r1g3r1 = tk.Label(self.r1g3,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==3)].iloc[0]['Rank1'])
        self.r1g3r2 = tk.Label(self.r1g3,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==3)].iloc[0]['Rank2'])
        self.r1g3w1 = tk.Label(self.r1g3,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==3)].iloc[0]['Win1'])
        self.r1g3w2 = tk.Label(self.r1g3,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==3)].iloc[0]['Win2'])

        self.r1g4t1 = tk.Label(self.r1g4,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==4)].iloc[0]['Team1'])
        self.r1g4t2 = tk.Label(self.r1g4,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==4)].iloc[0]['Team2'])
        self.r1g4r1 = tk.Label(self.r1g4,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==4)].iloc[0]['Rank1'])
        self.r1g4r2 = tk.Label(self.r1g4,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==4)].iloc[0]['Rank2'])
        self.r1g4w1 = tk.Label(self.r1g4,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==4)].iloc[0]['Win1'])
        self.r1g4w2 = tk.Label(self.r1g4,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==4)].iloc[0]['Win2'])

        self.r2g1t1 = tk.Label(self.r2g1,text=self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==1)].iloc[0]['Team1'])
        self.r2g1t2 = tk.Label(self.r2g1,text=self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==1)].iloc[0]['Team2'])
        self.r2g1r1 = tk.Label(self.r2g1,text=self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==1)].iloc[0]['Rank1'])
        self.r2g1r2 = tk.Label(self.r2g1,text=self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==1)].iloc[0]['Rank2'])
        self.r2g1w1 = tk.Label(self.r2g1,text=self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==1)].iloc[0]['Win1'])
        self.r2g1w2 = tk.Label(self.r2g1,text=self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==1)].iloc[0]['Win2'])

        self.r2g2t1 = tk.Label(self.r2g2,text=self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==2)].iloc[0]['Team1'])
        self.r2g2t2 = tk.Label(self.r2g2,text=self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==2)].iloc[0]['Team2'])
        self.r2g2r1 = tk.Label(self.r2g2,text=self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==2)].iloc[0]['Rank1'])
        self.r2g2r2 = tk.Label(self.r2g2,text=self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==2)].iloc[0]['Rank2'])
        self.r2g2w1 = tk.Label(self.r2g2,text=self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==2)].iloc[0]['Win1'])
        self.r2g2w2 = tk.Label(self.r2g2,text=self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==2)].iloc[0]['Win2'])


        self.r3g1t1 = tk.Label(self.r3g1,text=self.matchups[(self.matchups['Round']==3) & (self.matchups['Game']==1)].iloc[0]['Team1'])
        self.r3g1t2 = tk.Label(self.r3g1,text=self.matchups[(self.matchups['Round']==3) & (self.matchups['Game']==1)].iloc[0]['Team2'])
        self.r3g1r1 = tk.Label(self.r3g1,text=self.matchups[(self.matchups['Round']==3) & (self.matchups['Game']==1)].iloc[0]['Rank1'])
        self.r3g1r2 = tk.Label(self.r3g1,text=self.matchups[(self.matchups['Round']==3) & (self.matchups['Game']==1)].iloc[0]['Rank2'])
        self.r3g1w1 = tk.Label(self.r3g1,text=self.matchups[(self.matchups['Round']==3) & (self.matchups['Game']==1)].iloc[0]['Win1'])
        self.r3g1w2 = tk.Label(self.r3g1,text=self.matchups[(self.matchups['Round']==3) & (self.matchups['Game']==1)].iloc[0]['Win2'])


        self.r1g1t1.place(relx=0.1,rely=0,relwidth=0.7,relheight=0.5)
        self.r1g1t2.place(relx=0.1,rely=0.5,relwidth=0.7,relheight=0.5)
        self.r1g1r1.place(relx=0,rely=0,relwidth=0.1,relheight=0.5)
        self.r1g1r2.place(relx=0,rely=0.5,relwidth=0.1,relheight=0.5)
        self.r1g1w1.place(relx=0.8,rely=0,relwidth=0.2,relheight=0.5)
        self.r1g1w2.place(relx=0.8,rely=0.5,relwidth=0.2,relheight=0.5)

        self.r1g2t1.place(relx=0.1,rely=0,relwidth=0.7,relheight=0.5)
        self.r1g2t2.place(relx=0.1,rely=0.5,relwidth=0.7,relheight=0.5)
        self.r1g2r1.place(relx=0,rely=0,relwidth=0.1,relheight=0.5)
        self.r1g2r2.place(relx=0,rely=0.5,relwidth=0.1,relheight=0.5)
        self.r1g2w1.place(relx=0.8,rely=0,relwidth=0.2,relheight=0.5)
        self.r1g2w2.place(relx=0.8,rely=0.5,relwidth=0.2,relheight=0.5)

        self.r1g3t1.place(relx=0.1,rely=0,relwidth=0.7,relheight=0.5)
        self.r1g3t2.place(relx=0.1,rely=0.5,relwidth=0.7,relheight=0.5)
        self.r1g3r1.place(relx=0,rely=0,relwidth=0.1,relheight=0.5)
        self.r1g3r2.place(relx=0,rely=0.5,relwidth=0.1,relheight=0.5)
        self.r1g3w1.place(relx=0.8,rely=0,relwidth=0.2,relheight=0.5)
        self.r1g3w2.place(relx=0.8,rely=0.5,relwidth=0.2,relheight=0.5)

        self.r1g4t1.place(relx=0.1,rely=0,relwidth=0.7,relheight=0.5)
        self.r1g4t2.place(relx=0.1,rely=0.5,relwidth=0.7,relheight=0.5)
        self.r1g4r1.place(relx=0,rely=0,relwidth=0.1,relheight=0.5)
        self.r1g4r2.place(relx=0,rely=0.5,relwidth=0.1,relheight=0.5)
        self.r1g4w1.place(relx=0.8,rely=0,relwidth=0.2,relheight=0.5)
        self.r1g4w2.place(relx=0.8,rely=0.5,relwidth=0.2,relheight=0.5)


        self.r2g1t1.place(relx=0.1,rely=0,relwidth=0.7,relheight=0.5)
        self.r2g1t2.place(relx=0.1,rely=0.5,relwidth=0.7,relheight=0.5)
        self.r2g1r1.place(relx=0,rely=0,relwidth=0.1,relheight=0.5)
        self.r2g1r2.place(relx=0,rely=0.5,relwidth=0.1,relheight=0.5)
        self.r2g1w1.place(relx=0.8,rely=0,relwidth=0.2,relheight=0.5)
        self.r2g1w2.place(relx=0.8,rely=0.5,relwidth=0.2,relheight=0.5)

        self.r2g2t1.place(relx=0.1,rely=0,relwidth=0.7,relheight=0.5)
        self.r2g2t2.place(relx=0.1,rely=0.5,relwidth=0.7,relheight=0.5)
        self.r2g2r1.place(relx=0,rely=0,relwidth=0.1,relheight=0.5)
        self.r2g2r2.place(relx=0,rely=0.5,relwidth=0.1,relheight=0.5)
        self.r2g2w1.place(relx=0.8,rely=0,relwidth=0.2,relheight=0.5)
        self.r2g2w2.place(relx=0.8,rely=0.5,relwidth=0.2,relheight=0.5)


        self.r3g1t1.place(relx=0.1,rely=0,relwidth=0.7,relheight=0.5)
        self.r3g1t2.place(relx=0.1,rely=0.5,relwidth=0.7,relheight=0.5)
        self.r3g1r1.place(relx=0,rely=0,relwidth=0.1,relheight=0.5)
        self.r3g1r2.place(relx=0,rely=0.5,relwidth=0.1,relheight=0.5)
        self.r3g1w1.place(relx=0.8,rely=0,relwidth=0.2,relheight=0.5)
        self.r3g1w2.place(relx=0.8,rely=0.5,relwidth=0.2,relheight=0.5)
        #instantiate buttons here
        self.r1g1b1 = tk.Button(self.r1g1,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==1)].iloc[0]['Win1'],command=lambda:self.setResults(1,1,1))
        self.r1g1b2 = tk.Button(self.r1g1,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==1)].iloc[0]['Win2'],command=lambda:self.setResults(1,1,2))
        self.r1g2b1 = tk.Button(self.r1g2,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==2)].iloc[0]['Win1'],command=lambda:self.setResults(1,2,1))
        self.r1g2b2 = tk.Button(self.r1g2,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==2)].iloc[0]['Win2'],command=lambda:self.setResults(1,2,2))
        self.r1g3b1 = tk.Button(self.r1g3,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==3)].iloc[0]['Win1'],command=lambda:self.setResults(1,3,1))
        self.r1g3b2 = tk.Button(self.r1g3,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==3)].iloc[0]['Win2'],command=lambda:self.setResults(1,3,2))
        self.r1g4b1 = tk.Button(self.r1g4,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==4)].iloc[0]['Win1'],command=lambda:self.setResults(1,4,1))
        self.r1g4b2 = tk.Button(self.r1g4,text=self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==4)].iloc[0]['Win2'],command=lambda:self.setResults(1,4,2))
        self.r2g1b1 = tk.Button(self.r2g1,text=self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==1)].iloc[0]['Win1'],command=lambda:self.setResults(2,1,1))
        self.r2g1b2 = tk.Button(self.r2g1,text=self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==1)].iloc[0]['Win2'],command=lambda:self.setResults(2,1,2))
        self.r2g2b1 = tk.Button(self.r2g2,text=self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==2)].iloc[0]['Win1'],command=lambda:self.setResults(2,2,1))
        self.r2g2b2 = tk.Button(self.r2g2,text=self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==2)].iloc[0]['Win2'],command=lambda:self.setResults(2,2,2))
        self.r3g1b1 = tk.Button(self.r3g1,text=self.matchups[(self.matchups['Round']==3) & (self.matchups['Game']==1)].iloc[0]['Win1'],command=lambda:self.setResults(3,1,1))
        self.r3g1b2 = tk.Button(self.r3g1,text=self.matchups[(self.matchups['Round']==3) & (self.matchups['Game']==1)].iloc[0]['Win2'],command=lambda:self.setResults(3,1,2))

        self.createButtons()

    def createButtons(self):
        if ((self.r1g1t1['text']!='TBD') & (self.r1g1t2['text']!='TBD') & (self.r1g1w1['text'] != '4') & (self.r1g1w2['text'] != '4')):
            self.r1g1b1.place(relx=0.8,rely=0,relwidth=0.2,relheight=0.5)
            self.r1g1b2.place(relx=0.8,rely=0.5,relwidth=0.2,relheight=0.5)
        if ((self.r1g2t1['text']!='TBD') & (self.r1g2t2['text']!='TBD') & (self.r1g2w1['text'] != '4') & (self.r1g2w2['text'] != '4')):
            self.r1g2b1.place(relx=0.8,rely=0,relwidth=0.2,relheight=0.5)
            self.r1g2b2.place(relx=0.8,rely=0.5,relwidth=0.2,relheight=0.5)
        if ((self.r1g3t1['text']!='TBD') & (self.r1g3t2['text']!='TBD') & (self.r1g3w1['text'] != '4') & (self.r1g3w2['text'] != '4')):
            self.r1g3b1.place(relx=0.8,rely=0,relwidth=0.2,relheight=0.5)
            self.r1g3b2.place(relx=0.8,rely=0.5,relwidth=0.2,relheight=0.5)
        if ((self.r1g4t1['text']!='TBD') & (self.r1g4t2['text']!='TBD') & (self.r1g4w1['text'] != '4') & (self.r1g4w2['text'] != '4')):
            self.r1g4b1.place(relx=0.8,rely=0,relwidth=0.2,relheight=0.5)
            self.r1g4b2.place(relx=0.8,rely=0.5,relwidth=0.2,relheight=0.5)

        if ((self.r2g1t1['text']!='TBD') & (self.r2g1t2['text']!='TBD') & (self.r2g1w1['text'] != '4') & (self.r2g1w2['text'] != '4')):
            self.r2g1b1.place(relx=0.8,rely=0,relwidth=0.2,relheight=0.5)
            self.r2g1b2.place(relx=0.8,rely=0.5,relwidth=0.2,relheight=0.5)
        if ((self.r2g2t1['text']!='TBD') & (self.r2g2t2['text']!='TBD') & (self.r2g2w1['text'] != '4') & (self.r2g2w2['text'] != '4')):
            self.r2g2b1.place(relx=0.8,rely=0,relwidth=0.2,relheight=0.5)
            self.r2g2b2.place(relx=0.8,rely=0.5,relwidth=0.2,relheight=0.5)

        if ((self.r3g1t1['text']!='TBD') & (self.r3g1t2['text']!='TBD') & (self.r3g1w1['text'] != '4') & (self.r3g1w2['text'] != '4')):
            self.r3g1b1.place(relx=0.8,rely=0,relwidth=0.2,relheight=0.5)
            self.r3g1b2.place(relx=0.8,rely=0.5,relwidth=0.2,relheight=0.5)

    def advanceRound(self):
        if ((self.r1g1w1['text']=='4') & (self.r2g1t1['text']=='TBD')):
            self.r2g1t1['text'] = self.r1g1t1['text']
            self.matchups.loc[(self.matchups['Round']==2) & (self.matchups['Game']==1),'Team1'] = self.r1g1t1['text']
            self.r2g1r1['text'] = self.r1g1r1['text']
            self.matchups.loc[(self.matchups['Round']==2) & (self.matchups['Game']==1),'Rank1'] = self.r1g1r1['text']
        elif ((self.r1g1w2['text']=='4') & (self.r2g1t1['text']=='TBD')):
            self.r2g1t1['text'] = self.r1g1t2['text']
            self.matchups.loc[(self.matchups['Round']==2) & (self.matchups['Game']==1),'Team1'] = self.r1g1t2['text']
            self.r2g1r1['text'] = self.r1g1r2['text']
            self.matchups.loc[(self.matchups['Round']==2) & (self.matchups['Game']==1),'Rank1'] = self.r1g1r2['text']
        elif ((self.r1g2w1['text']=='4') & (self.r2g1t2['text']=='TBD')):
            self.r2g1t2['text'] = self.r1g2t1['text']
            self.matchups.loc[(self.matchups['Round']==2) & (self.matchups['Game']==1),'Team2'] = self.r1g2t1['text']
            self.r2g1r2['text'] = self.r1g2r1['text']
            self.matchups.loc[(self.matchups['Round']==2) & (self.matchups['Game']==1),'Rank2'] = self.r1g2r1['text']
        elif ((self.r1g2w2['text']=='4') & (self.r2g1t2['text']=='TBD')):
            self.r2g1t2['text'] = self.r1g2t2['text']
            self.matchups.loc[(self.matchups['Round']==2) & (self.matchups['Game']==1),'Team2'] = self.r1g2t2['text']
            self.r2g1r2['text'] = self.r1g2r2['text']
            self.matchups.loc[(self.matchups['Round']==2) & (self.matchups['Game']==1),'Rank2'] = self.r1g2r2['text']
        elif ((self.r1g3w1['text']=='4') & (self.r2g2t1['text']=='TBD')):
            self.r2g2t1['text'] = self.r1g3t1['text']
            self.matchups.loc[(self.matchups['Round']==2) & (self.matchups['Game']==2),'Team1'] = self.r1g3t1['text']
            self.r2g2r1['text'] = self.r1g3r1['text']
            self.matchups.loc[(self.matchups['Round']==2) & (self.matchups['Game']==2),'Rank1'] = self.r1g3r1['text']
        elif ((self.r1g3w2['text']=='4') & (self.r2g2t1['text']=='TBD')):
            self.r2g2t1['text'] = self.r1g3t2['text']
            self.matchups.loc[(self.matchups['Round']==2) & (self.matchups['Game']==2),'Team1'] = self.r1g3t2['text']
            self.r2g2r1['text'] = self.r1g3r2['text']
            self.matchups.loc[(self.matchups['Round']==2) & (self.matchups['Game']==2),'Rank1'] = self.r1g3r2['text']
        elif ((self.r1g4w1['text']=='4') & (self.r2g2t2['text']=='TBD')):
            self.r2g2t2['text'] = self.r1g4t1['text']
            self.matchups.loc[(self.matchups['Round']==2) & (self.matchups['Game']==2),'Team2'] = self.r1g4t1['text']
            self.r2g2r2['text'] = self.r1g4r1['text']
            self.matchups.loc[(self.matchups['Round']==2) & (self.matchups['Game']==2),'Rank2'] = self.r1g4r1['text']
        elif ((self.r1g4w2['text']=='4') & (self.r2g2t2['text']=='TBD')):
            self.r2g2t2['text'] = self.r1g4t2['text']
            self.matchups.loc[(self.matchups['Round']==2) & (self.matchups['Game']==2),'Team2'] = self.r1g4t2['text']
            self.r2g2r2['text'] = self.r1g4r2['text']
            self.matchups.loc[(self.matchups['Round']==2) & (self.matchups['Game']==2),'Rank2'] = self.r1g4r2['text']

        elif ((self.r2g1w1['text']=='4') & (self.r3g1t1['text']=='TBD')):
            self.r3g1t1['text'] = self.r2g1t1['text']
            self.matchups.loc[(self.matchups['Round']==3) & (self.matchups['Game']==1),'Team1'] = self.r2g1t1['text']
            self.r3g1r1['text'] = self.r2g1r1['text']
            self.matchups.loc[(self.matchups['Round']==3) & (self.matchups['Game']==1),'Rank1'] = self.r2g1r1['text']
        elif ((self.r2g1w2['text']=='4') & (self.r3g1t1['text']=='TBD')):
            self.r3g1t1['text'] = self.r2g1t2['text']
            self.matchups.loc[(self.matchups['Round']==3) & (self.matchups['Game']==1),'Team1'] = self.r2g1t2['text']
            self.r3g1r1['text'] = self.r2g1r2['text']
            self.matchups.loc[(self.matchups['Round']==3) & (self.matchups['Game']==1),'Rank1'] = self.r2g1r2['text']
        elif ((self.r2g2w1['text']=='4') & (self.r3g1t2['text']=='TBD')):
            self.r3g1t2['text'] = self.r2g2t1['text']
            self.matchups.loc[(self.matchups['Round']==3) & (self.matchups['Game']==1),'Team2'] = self.r2g2t1['text']
            self.r3g1r2['text'] = self.r2g2r1['text']
            self.matchups.loc[(self.matchups['Round']==3) & (self.matchups['Game']==1),'Rank2'] = self.r2g2r1['text']
        elif ((self.r2g2w2['text']=='4') & (self.r3g1t2['text']=='TBD')):
            self.r3g1t2['text'] = self.r2g2t2['text']
            self.matchups.loc[(self.matchups['Round']==3) & (self.matchups['Game']==1),'Team2'] = self.r2g2t2['text']
            self.r3g1r2['text'] = self.r2g2r2['text']
            self.matchups.loc[(self.matchups['Round']==3) & (self.matchups['Game']==1),'Rank2'] = self.r2g2r2['text']
        self.writeMatchups()
        self.createButtons()

    def setResults(self, round_num, game, team):
        if round_num == 1:
            if game == 1:
                self.r1g1b1.place_forget()
                self.r1g1b2.place_forget()
                if team == 1:
                    self.matchups.loc[(self.matchups['Round']==1) & (self.matchups['Game']==1), 'Win1'] +=1
                    self.r1g1w1['text'] = self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==1)].iloc[0]['Win1']
                    self.r1g1b1['text'] = self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==1)].iloc[0]['Win1']
                else:
                    self.matchups.loc[(self.matchups['Round']==1) & (self.matchups['Game']==1), 'Win2'] +=1
                    self.r1g1w2['text'] = self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==1)].iloc[0]['Win2']
                    self.r1g1b2['text'] = self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==1)].iloc[0]['Win2']

            elif game ==2:
                self.r1g2b1.place_forget()
                self.r1g2b2.place_forget()
                if team == 1:
                    self.matchups.loc[(self.matchups['Round']==1) & (self.matchups['Game']==2), 'Win1'] +=1
                    self.r1g2w1['text'] = self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==2)].iloc[0]['Win1']
                    self.r1g2b1['text'] = self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==2)].iloc[0]['Win1']
                else:
                    self.matchups.loc[(self.matchups['Round']==1) & (self.matchups['Game']==2), 'Win2'] +=1
                    self.r1g2w2['text'] = self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==2)].iloc[0]['Win2']
                    self.r1g2b2['text'] = self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==2)].iloc[0]['Win2']

            elif game ==3:
                self.r1g3b1.place_forget()
                self.r1g3b2.place_forget()
                if team == 1:
                    self.matchups.loc[(self.matchups['Round']==1) & (self.matchups['Game']==3), 'Win1'] +=1
                    self.r1g3w1['text'] = self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==3)].iloc[0]['Win1']
                    self.r1g3b1['text'] = self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==3)].iloc[0]['Win1']
                else:
                    self.matchups.loc[(self.matchups['Round']==1) & (self.matchups['Game']==3), 'Win2'] +=1
                    self.r1g3w2['text'] = self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==3)].iloc[0]['Win2']
                    self.r1g3b2['text'] = self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==3)].iloc[0]['Win2']

            else:
                self.r1g4b1.place_forget()
                self.r1g4b2.place_forget()
                if team == 1:
                    self.matchups.loc[(self.matchups['Round']==1) & (self.matchups['Game']==4), 'Win1'] +=1
                    self.r1g4w1['text'] = self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==4)].iloc[0]['Win1']
                    self.r1g4b1['text'] = self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==4)].iloc[0]['Win1']
                else:
                    self.matchups.loc[(self.matchups['Round']==1) & (self.matchups['Game']==4), 'Win2'] +=1
                    self.r1g4w2['text'] = self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==4)].iloc[0]['Win2']
                    self.r1g4b2['text'] = self.matchups[(self.matchups['Round']==1) & (self.matchups['Game']==4)].iloc[0]['Win2']

        elif round_num == 2:
            if game == 1:
                self.r2g1b1.place_forget()
                self.r2g1b2.place_forget()
                if team == 1:
                    self.matchups.loc[(self.matchups['Round']==2) & (self.matchups['Game']==1), 'Win1'] +=1
                    self.r2g1w1['text'] = self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==1)].iloc[0]['Win1']
                    self.r2g1b1['text'] = self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==1)].iloc[0]['Win1']
                else:
                    self.matchups.loc[(self.matchups['Round']==2) & (self.matchups['Game']==1), 'Win2'] +=1
                    self.r2g1w2['text'] = self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==1)].iloc[0]['Win2']
                    self.r2g1b2['text'] = self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==1)].iloc[0]['Win2']

            else:
                self.r2g2b1.place_forget()
                self.r2g2b2.place_forget()
                if team == 1:
                    self.matchups.loc[(self.matchups['Round']==2) & (self.matchups['Game']==2), 'Win1'] +=1
                    self.r2g2w1['text'] = self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==2)].iloc[0]['Win1']
                    self.r2g2b1['text'] = self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==2)].iloc[0]['Win1']
                else:
                    self.matchups.loc[(self.matchups['Round']==2) & (self.matchups['Game']==2), 'Win2'] +=1
                    self.r2g2w2['text'] = self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==2)].iloc[0]['Win2']
                    self.r2g2b2['text'] = self.matchups[(self.matchups['Round']==2) & (self.matchups['Game']==2)].iloc[0]['Win2']

        else:
            if game == 1:
                self.r3g1b1.place_forget()
                self.r3g1b2.place_forget()
                if team == 1:
                    self.matchups.loc[(self.matchups['Round']==3) & (self.matchups['Game']==1), 'Win1'] +=1
                    self.r3g1w1['text'] = self.matchups[(self.matchups['Round']==3) & (self.matchups['Game']==1)].iloc[0]['Win1']
                    self.r3g1b1['text'] = self.matchups[(self.matchups['Round']==3) & (self.matchups['Game']==1)].iloc[0]['Win1']
                else:
                    self.matchups.loc[(self.matchups['Round']==3) & (self.matchups['Game']==1), 'Win2'] +=1
                    self.r3g1w2['text'] = self.matchups[(self.matchups['Round']==3) & (self.matchups['Game']==1)].iloc[0]['Win2']
                    self.r3g1b2['text'] = self.matchups[(self.matchups['Round']==3) & (self.matchups['Game']==1)].iloc[0]['Win2']

        self.advanceRound()

    def getMatchups(self):
        matchups = pd.read_csv('PlayoffSchedule.csv')
        return matchups

    def writeMatchups(self):
        self.matchups.to_csv('PlayoffSchedule.csv',index=False)
"""
To Do:
-i need to fix the games, rn 1 and 2 play in the second round
"""