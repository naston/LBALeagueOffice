import tkinter as tk
import pandas as pd
import numpy as np
import SchedulerMain
#scheduler needs to be changed to be in column form team1, team2, week

class Results(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #self.weekStatus = self.getWeekStatus()
        #self.standings = self.getCurrentStandings()
        #week = int((self.standings['Wins'] + self.standings['Losses']) / len(self.standings)) + 1
        #if week!=self.weekStatus['Week']:
        #   self.newWeek(week)
        #self.games = self.getThisWeek(week)

        #I may want to add getting the currents weeks status from a csv so that I can add games mid week and not worry about over adding games

        self.homeButton = tk.Button(self,text='Home',command=lambda:controller.show_frame("StartPage"))
        self.homeButton.place(relx=0,rely=0,relwidth=0.05,relheight=0.1)
        self.thisWeek = tk.Frame(self)
        self.thisWeek.place(relx=0.05,rely=0,relwidth=0.95,relheight=1)
        self.titlelabel=tk.Label(self.thisWeek,text='This Weeks Games')
        self.titlelabel.place(relx=0,rely=0,relwidth=1,relheight=0.1)

        self.resultsWindow()

    def newWeek(self,week):
        #I want to go here if the week calculated above does not equal the week in the first column of the current week status
        #here i overwrite with a clean week status csv
        data = {
            'Week':week,
            'G1':0,
            'G2':0,
            'G3':0,
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
        self.weekStatus = pd.DataFrame(data)

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
        self.standings[self.standings['Team']==winning_team]['Wins'] += 1
        self.standings[self.standings['Team']==losing_team]['Losses'] += 1

        #switch case for hiding buttons
        if game_num == 0:
            self.g1t1.place_forget()
            self.g1t2.place_forget()
            self.weekStatus['G1'] = 1
        elif game_num == 1:
            self.g2t1.place_forget()
            self.g2t2.place_forget()
            self.weekStatus['G2'] = 1
        elif game_num == 2:
            self.g3t1.place_forget()
            self.g3t2.place_forget()
            self.weekStatus['G3'] = 1
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

    def resultsWindow(self):
        self.g1 = tk.Label(self.thisWeek, text = 'Game')
        self.g2 = tk.Label(self.thisWeek, text = 'Game')
        self.g3 = tk.Label(self.thisWeek, text = 'Game')
        self.g4 = tk.Label(self.thisWeek, text = 'Game')
        self.g5 = tk.Label(self.thisWeek, text = 'Game')
        self.g6 = tk.Label(self.thisWeek, text = 'Game')
        self.g7 = tk.Label(self.thisWeek, text = 'Game')
        self.g8 = tk.Label(self.thisWeek, text = 'Game')
        self.g9 = tk.Label(self.thisWeek, text = 'Game')
        self.g10 = tk.Label(self.thisWeek, text = 'Game')
        self.g11 = tk.Label(self.thisWeek, text = 'Game')
        self.g12 = tk.Label(self.thisWeek, text = 'Game')
        self.g13 = tk.Label(self.thisWeek, text = 'Game')
        self.g14 = tk.Label(self.thisWeek, text = 'Game')
        self.g15 = tk.Label(self.thisWeek, text = 'Game')
        
        self.g1.place(relx=0,rely=0.1,relwidth=1,relheight=0.06)
        self.g2.place(relx=0,rely=0.16,relwidth=1,relheight=0.06)
        self.g3.place(relx=0,rely=0.22,relwidth=1,relheight=0.06)
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

        self.g1t1 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(0,0))
        self.g2t1 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(1,0))
        self.g3t1 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(2,0))
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

        self.g1t2 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(0,1))
        self.g2t2 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(1,1))
        self.g3t2 = tk.Button(self.thisWeek, text = 'Game', command = lambda: self.setResults(2,1))
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
        
        if self.weekStatus['G1'] == 0:
            self.g1t1.place(relx=0,rely=0.1,relwidth=0.1,relheight=0.06)
            self.g1t2.place(relx=0.9,rely=0.1,relwidth=0.1,relheight=0.06)
        elif self.weekStatus['G2'] == 0:  
            self.g2t1.place(relx=0,rely=0.16,relwidth=0.1,relheight=0.06)
            self.g2t2.place(relx=0.9,rely=0.16,relwidth=0.1,relheight=0.06)
        elif self.weekStatus['G3'] == 0:  
            self.g3t1.place(relx=0,rely=0.22,relwidth=0.1,relheight=0.06)
            self.g3t2.place(relx=0.9,rely=0.22,relwidth=0.1,relheight=0.06)
        elif self.weekStatus['G4'] == 0:  
            self.g4t1.place(relx=0,rely=0.28,relwidth=0.1,relheight=0.06)
            self.g4t2.place(relx=0.9,rely=0.28,relwidth=0.1,relheight=0.06)
        elif self.weekStatus['G5'] == 0:  
            self.g5t1.place(relx=0,rely=0.34,relwidth=0.1,relheight=0.06)
            self.g5t2.place(relx=0.9,rely=0.34,relwidth=0.1,relheight=0.06)
        elif self.weekStatus['G6'] == 0:  
            self.g6t1.place(relx=0,rely=0.4,relwidth=0.1,relheight=0.06)
            self.g6t2.place(relx=0.9,rely=0.4,relwidth=0.1,relheight=0.06)
        elif self.weekStatus['G7'] == 0:  
            self.g7t1.place(relx=0,rely=0.46,relwidth=0.1,relheight=0.06)
            self.g7t2.place(relx=0.9,rely=0.46,relwidth=0.1,relheight=0.06)
        elif self.weekStatus['G8'] == 0:  
            self.g8t1.place(relx=0,rely=0.52,relwidth=0.1,relheight=0.06)
            self.g8t2.place(relx=0.9,rely=0.52,relwidth=0.1,relheight=0.06)
        elif self.weekStatus['G9'] == 0:  
            self.g9t1.place(relx=0,rely=0.58,relwidth=0.1,relheight=0.06)
            self.g9t2.place(relx=0.9,rely=0.58,relwidth=0.1,relheight=0.06)
        elif self.weekStatus['G10'] == 0:  
            self.g10t1.place(relx=0,rely=0.64,relwidth=0.1,relheight=0.06)
            self.g10t2.place(relx=0.9,rely=0.64,relwidth=0.1,relheight=0.06)
        elif self.weekStatus['G11'] == 0:  
            self.g11t1.place(relx=0,rely=0.70,relwidth=0.1,relheight=0.06)
            self.g11t2.place(relx=0.9,rely=0.70,relwidth=0.1,relheight=0.06)
        elif self.weekStatus['G12'] == 0:  
            self.g12t1.place(relx=0,rely=0.76,relwidth=0.1,relheight=0.06)
            self.g12t2.place(relx=0.9,rely=0.76,relwidth=0.1,relheight=0.06)
        elif self.weekStatus['G13'] == 0:  
            self.g13t1.place(relx=0,rely=0.82,relwidth=0.1,relheight=0.06)
            self.g13t2.place(relx=0.9,rely=0.82,relwidth=0.1,relheight=0.06)
        elif self.weekStatus['G14'] == 0:  
            self.g14t1.place(relx=0,rely=0.88,relwidth=0.1,relheight=0.06)
            self.g14t2.place(relx=0.9,rely=0.88,relwidth=0.1,relheight=0.06)
        elif self.weekStatus['G15'] == 0:  
            self.g15t1.place(relx=0,rely=0.94,relwidth=0.1,relheight=0.06)
            self.g15t2.place(relx=0.9,rely=0.94,relwidth=0.1,relheight=0.06)

        


"""
To Do:
-fix scheduler to be in different format
-create a rankings csv
-create a hide status for the current week


"""