import tkinter as tk
import os
import numpy as np
import pandas as pd

HEIGHT=750
WIDTH=1200
draftorder=['Grizz','Grizz','Grizz','Kings','Grizz','Nuggets','test','test','test']
roster=[['empty','empty','empty','empty','empty','empty','empty','empty','empty','empty','empty','empty','empty','empty','empty','empty','empty','empty'],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']]
topten=[]
indexes=[]
df= pd.read_csv('LeaguePlayerDataBase.csv')
search=[False]


class Draft(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.teamframe = tk.Frame(self,bg='black')
        self.teamframe.place(relx=0,rely=0,relwidth=0.6,relheight=0.2)
        self.nextframe = tk.Frame(self,bg='green')
        self.nextframe.place(relx=0.6,rely=0,relwidth=0.2,relheight=0.2)
        self.secondframe = tk.Frame(self,bg='blue')
        self.secondframe.place(relx=0.8,rely=0,relwidth=0.2,relheight=0.2)
        self.pickframe = tk.Frame(self,bg='yellow')
        self.pickframe.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.8)
        self.currentroster = tk.Frame(self,bg='orange')
        self.currentroster.place(relx=0,rely=0.2,relwidth=0.2,relheight=0.8)
        self.searchframe = tk.Frame(self,bg='purple')
        self.searchframe.place(relx=0.8,rely=0.2,relwidth=0.2,relheight=0.4)
        self.infoframe = tk.Frame(self,bg='red')
        self.infoframe.place(relx=0.8,rely=0.6,relwidth=0.2,relheight=0.4)

        self.start()
        self.draft_ticker()
        self.roster_tracker()
        self.pick_window()
        self.position_counter()
        self.search_bar()

    def start(self):
        i=0
        while i<len(df['Team']):
            if df['Team'][i]=='none':
                picktext= str(df['Rank'][i])+' '+df['Name'][i]+' '+df['Position'][i]+' '+str(df['Overall'][i])
                topten.append(picktext)
                indexes.append(df['Rank'][i]-1)
            i+=1

    def draft_ticker(self):
        #labels for team picking and next two teams up
        self.t=tk.Label(self.teamframe,text=draftorder[0])
        self.t.place(relx=0.05,rely=0.1,relwidth=0.3,relheight=0.8)
        self.t1=tk.Label(self.teamframe,text=draftorder[0])
        self.t1.place(relx=0.4,rely=0.1,relwidth=0.55,relheight=0.8)
        self.t2=tk.Label(self.nextframe,text=draftorder[1])
        self.t2.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.8)
        self.t3=tk.Label(self.secondframe,text=draftorder[2])
        self.t3.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.8)

    def roster_tracker(self):
        #labels for current roster
        #up max offseason roster size to 18
        self.rtitle=tk.Label(self.currentroster,text='Current Roster')
        self.rtitle.place(relx=0.1,rely=0,relwidth=0.8,relheight=0.075)
        self.r1=tk.Label(self.currentroster,text=roster[0][0])
        self.r1.place(relx=0.1,rely=0.0875,relwidth=0.6,relheight=0.05)
        self.r2=tk.Label(self.currentroster,text=roster[0][1])
        self.r2.place(relx=0.1,rely=0.1375,relwidth=0.6,relheight=0.05)
        self.r3=tk.Label(self.currentroster,text=roster[0][2])
        self.r3.place(relx=0.1,rely=0.1875,relwidth=0.6,relheight=0.05)
        self.r4=tk.Label(self.currentroster,text=roster[0][3])
        self.r4.place(relx=0.1,rely=0.2375,relwidth=0.6,relheight=0.05)
        self.r5=tk.Label(self.currentroster,text=roster[0][4])
        self.r5.place(relx=0.1,rely=0.2875,relwidth=0.6,relheight=0.05)
        self.r6=tk.Label(self.currentroster,text=roster[0][5])
        self.r6.place(relx=0.1,rely=0.3375,relwidth=0.6,relheight=0.05)
        self.r7=tk.Label(self.currentroster,text=roster[0][6])
        self.r7.place(relx=0.1,rely=0.3875,relwidth=0.6,relheight=0.05)
        self.r8=tk.Label(self.currentroster,text=roster[0][7])
        self.r8.place(relx=0.1,rely=0.4375,relwidth=0.6,relheight=0.05)
        self.r9=tk.Label(self.currentroster,text=roster[0][8])
        self.r9.place(relx=0.1,rely=0.4875,relwidth=0.6,relheight=0.05)
        self.r10=tk.Label(self.currentroster,text=roster[0][9])
        self.r10.place(relx=0.1,rely=0.5375,relwidth=0.6,relheight=0.05)
        self.r11=tk.Label(self.currentroster,text=roster[0][10])
        self.r11.place(relx=0.1,rely=0.5875,relwidth=0.6,relheight=0.05)
        self.r12=tk.Label(self.currentroster,text=roster[0][11])
        self.r12.place(relx=0.1,rely=0.6375,relwidth=0.6,relheight=0.05)
        self.r13=tk.Label(self.currentroster,text=roster[0][12])
        self.r13.place(relx=0.1,rely=0.6875,relwidth=0.6,relheight=0.05)
        self.r14=tk.Label(self.currentroster,text=roster[0][13])
        self.r14.place(relx=0.1,rely=0.7375,relwidth=0.6,relheight=0.05)
        self.r15=tk.Label(self.currentroster,text=roster[0][14])
        self.r15.place(relx=0.1,rely=0.7875,relwidth=0.6,relheight=0.05)
        self.r16=tk.Label(self.currentroster,text=roster[0][15])
        self.r16.place(relx=0.1,rely=0.8375,relwidth=0.6,relheight=0.05)
        self.r17=tk.Label(self.currentroster,text=roster[0][16])
        self.r17.place(relx=0.1,rely=0.8875,relwidth=0.6,relheight=0.05)
        self.r18=tk.Label(self.currentroster,text=roster[0][17])
        self.r18.place(relx=0.1,rely=0.9375,relwidth=0.6,relheight=0.05)
        #roster overalls
        self.o1=tk.Label(self.currentroster,text=roster[1][0])
        self.o1.place(relx=0.8,rely=0.0875,relwidth=0.1,relheight=0.05)
        self.o2=tk.Label(self.currentroster,text=roster[1][1])
        self.o2.place(relx=0.8,rely=0.1375,relwidth=0.1,relheight=0.05)
        self.o3=tk.Label(self.currentroster,text=roster[1][2])
        self.o3.place(relx=0.8,rely=0.1875,relwidth=0.1,relheight=0.05)
        self.o4=tk.Label(self.currentroster,text=roster[1][3])
        self.o4.place(relx=0.8,rely=0.2375,relwidth=0.1,relheight=0.05)
        self.o5=tk.Label(self.currentroster,text=roster[1][4])
        self.o5.place(relx=0.8,rely=0.2875,relwidth=0.1,relheight=0.05)
        self.o6=tk.Label(self.currentroster,text=roster[1][5])
        self.o6.place(relx=0.8,rely=0.3375,relwidth=0.1,relheight=0.05)
        self.o7=tk.Label(self.currentroster,text=roster[1][6])
        self.o7.place(relx=0.8,rely=0.3875,relwidth=0.1,relheight=0.05)
        self.o8=tk.Label(self.currentroster,text=roster[1][7])
        self.o8.place(relx=0.8,rely=0.4375,relwidth=0.1,relheight=0.05)
        self.o9=tk.Label(self.currentroster,text=roster[1][8])
        self.o9.place(relx=0.8,rely=0.4875,relwidth=0.1,relheight=0.05)
        self.o10=tk.Label(self.currentroster,text=roster[1][9])
        self.o10.place(relx=0.8,rely=0.5375,relwidth=0.1,relheight=0.05)
        self.o11=tk.Label(self.currentroster,text=roster[1][10])
        self.o11.place(relx=0.8,rely=0.5875,relwidth=0.1,relheight=0.05)
        self.o12=tk.Label(self.currentroster,text=roster[1][11])
        self.o12.place(relx=0.8,rely=0.6375,relwidth=0.1,relheight=0.05)
        self.o13=tk.Label(self.currentroster,text=roster[1][12])
        self.o13.place(relx=0.8,rely=0.6875,relwidth=0.1,relheight=0.05)
        self.o14=tk.Label(self.currentroster,text=roster[1][13])
        self.o14.place(relx=0.8,rely=0.7375,relwidth=0.1,relheight=0.05)
        self.o15=tk.Label(self.currentroster,text=roster[1][14])
        self.o15.place(relx=0.8,rely=0.7875,relwidth=0.1,relheight=0.05)
        self.o16=tk.Label(self.currentroster,text=roster[1][15])
        self.o16.place(relx=0.8,rely=0.8375,relwidth=0.1,relheight=0.05)
        self.o17=tk.Label(self.currentroster,text=roster[1][16])
        self.o17.place(relx=0.8,rely=0.8875,relwidth=0.1,relheight=0.05)
        self.o18=tk.Label(self.currentroster,text=roster[1][17])
        self.o18.place(relx=0.8,rely=0.9375,relwidth=0.1,relheight=0.05)
        #position label for each player
        self.po1=tk.Label(self.currentroster,text=roster[2][0])
        self.po1.place(relx=0.7,rely=0.0875,relwidth=0.1,relheight=0.05)
        self.po2=tk.Label(self.currentroster,text=roster[2][1])
        self.po2.place(relx=0.7,rely=0.1375,relwidth=0.1,relheight=0.05)
        self.po3=tk.Label(self.currentroster,text=roster[2][2])
        self.po3.place(relx=0.7,rely=0.1875,relwidth=0.1,relheight=0.05)
        self.po4=tk.Label(self.currentroster,text=roster[2][3])
        self.po4.place(relx=0.7,rely=0.2375,relwidth=0.1,relheight=0.05)
        self.po5=tk.Label(self.currentroster,text=roster[2][4])
        self.po5.place(relx=0.7,rely=0.2875,relwidth=0.1,relheight=0.05)
        self.po6=tk.Label(self.currentroster,text=roster[2][5])
        self.po6.place(relx=0.7,rely=0.3375,relwidth=0.1,relheight=0.05)
        self.po7=tk.Label(self.currentroster,text=roster[2][6])
        self.po7.place(relx=0.7,rely=0.3875,relwidth=0.1,relheight=0.05)
        self.po8=tk.Label(self.currentroster,text=roster[2][7])
        self.po8.place(relx=0.7,rely=0.4375,relwidth=0.1,relheight=0.05)
        self.po9=tk.Label(self.currentroster,text=roster[2][8])
        self.po9.place(relx=0.7,rely=0.4875,relwidth=0.1,relheight=0.05)
        self.po10=tk.Label(self.currentroster,text=roster[2][9])
        self.po10.place(relx=0.7,rely=0.5375,relwidth=0.1,relheight=0.05)
        self.po11=tk.Label(self.currentroster,text=roster[2][10])
        self.po11.place(relx=0.7,rely=0.5875,relwidth=0.1,relheight=0.05)
        self.po12=tk.Label(self.currentroster,text=roster[2][11])
        self.po12.place(relx=0.7,rely=0.6375,relwidth=0.1,relheight=0.05)
        self.po13=tk.Label(self.currentroster,text=roster[2][12])
        self.po13.place(relx=0.7,rely=0.6875,relwidth=0.1,relheight=0.05)
        self.po14=tk.Label(self.currentroster,text=roster[2][13])
        self.po14.place(relx=0.7,rely=0.7375,relwidth=0.1,relheight=0.05)
        self.po15=tk.Label(self.currentroster,text=roster[2][14])
        self.po15.place(relx=0.7,rely=0.7875,relwidth=0.1,relheight=0.05)
        self.po16=tk.Label(self.currentroster,text=roster[2][15])
        self.po16.place(relx=0.7,rely=0.8375,relwidth=0.1,relheight=0.05)
        self.po17=tk.Label(self.currentroster,text=roster[2][16])
        self.po17.place(relx=0.7,rely=0.8875,relwidth=0.1,relheight=0.05)
        self.po18=tk.Label(self.currentroster,text=roster[2][17])
        self.po18.place(relx=0.7,rely=0.9375,relwidth=0.1,relheight=0.05)
        self.hideEmpty()

    def pick_window(self):
        #buttons for picking players
        self.p1=tk.Button(self.pickframe, text=topten[0], command = lambda: self.changePlayer(0))
        self.p1.place(relx=0,rely=0,relwidth=1,relheight=0.1)
        self.p2=tk.Button(self.pickframe, text=topten[1], command = lambda: self.changePlayer(1))
        self.p2.place(relx=0,rely=0.1,relwidth=1,relheight=0.1)
        self.p3=tk.Button(self.pickframe, text=topten[2], command = lambda: self.changePlayer(2))
        self.p3.place(relx=0,rely=0.2,relwidth=1,relheight=0.1)
        self.p4=tk.Button(self.pickframe, text=topten[3], command = lambda: self.changePlayer(3))
        self.p4.place(relx=0,rely=0.3,relwidth=1,relheight=0.1)
        self.p5=tk.Button(self.pickframe, text=topten[4], command = lambda: self.changePlayer(4))
        self.p5.place(relx=0,rely=0.4,relwidth=1,relheight=0.1)
        self.p6=tk.Button(self.pickframe, text=topten[5], command = lambda: self.changePlayer(5))
        self.p6.place(relx=0,rely=0.5,relwidth=1,relheight=0.1)
        self.p7=tk.Button(self.pickframe, text=topten[6], command = lambda: self.changePlayer(6))
        self.p7.place(relx=0,rely=0.6,relwidth=1,relheight=0.1)
        self.p8=tk.Button(self.pickframe, text=topten[7], command = lambda: self.changePlayer(7))
        self.p8.place(relx=0,rely=0.7,relwidth=1,relheight=0.1)
        self.p9=tk.Button(self.pickframe, text=topten[8], command = lambda: self.changePlayer(8))
        self.p9.place(relx=0,rely=0.8,relwidth=1,relheight=0.1)
        self.p10=tk.Button(self.pickframe, text=topten[9], command = lambda: self.changePlayer(9))
        self.p10.place(relx=0,rely=0.9,relwidth=1,relheight=0.1)

    def position_counter(self):
        #position counter for roster
        self.pg=tk.Label(self.infoframe,text='Point Guards on roster: '+str(0))
        self.pg.place(relx=0.1,rely=0.025,relwidth=0.8,relheight=0.075)
        self.sg=tk.Label(self.infoframe,text='Shooting Guards on roster: '+str(0))
        self.sg.place(relx=0.1,rely=0.225,relwidth=0.8,relheight=0.075)
        self.sf=tk.Label(self.infoframe,text='Small Forwards on roster: '+str(0))
        self.sf.place(relx=0.1,rely=0.425,relwidth=0.8,relheight=0.075)
        self.pf=tk.Label(self.infoframe,text='Power Forwards on roster: '+str(0))
        self.pf.place(relx=0.1,rely=0.625,relwidth=0.8,relheight=0.075)
        self.c=tk.Label(self.infoframe,text='Centers on roster: '+str(0))
        self.c.place(relx=0.1,rely=0.825,relwidth=0.8,relheight=0.075)

        self.pgo=tk.Label(self.infoframe,text='Average overall: '+str(0))
        self.pgo.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.075)
        self.sgo=tk.Label(self.infoframe,text='Average overall: '+str(0))
        self.sgo.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.075)
        self.sfo=tk.Label(self.infoframe,text='Average overall: '+str(0))
        self.sfo.place(relx=0.1,rely=0.5,relwidth=0.8,relheight=0.075)
        self.pfo=tk.Label(self.infoframe,text='Average overall: '+str(0))
        self.pfo.place(relx=0.1,rely=0.7,relwidth=0.8,relheight=0.075)
        self.co=tk.Label(self.infoframe,text='Average overall: '+str(0))
        self.co.place(relx=0.1,rely=0.9,relwidth=0.8,relheight=0.075)

    def search_bar(self):
        #search bar
        self.sbar=tk.Entry(self.searchframe)
        self.sbar.insert(0,'Search Player Name')
        self.sbar.bind('<FocusIn>',self.on_entry_click)
        self.sbar.bind('<FocusOut>',self.on_focusout)
        self.sbar.config(fg='grey')
        self.sbar.place(relx=0.1,rely=0.025,relwidth=0.8,relheight=0.2)
        #position selector
        self.nullselect=tk.StringVar(self.searchframe)
        self.nullselect.set('Select a position')
        self.positiondd=tk.OptionMenu(self.searchframe,self.nullselect,'Point Guard','Shooting Guard','Small Forward','Power Forward','Center')
        self.positiondd.place(relx=0.1,rely=0.275,relwidth=0.8,relheight=0.2)
        #search button
        self.sbutton=tk.Button(self.searchframe,text='Search',command=lambda:self.Search())
        self.sbutton.place(relx=0.1,rely=0.525,relwidth=0.8,relheight=0.2)
        #clear button
        self.clear=tk.Button(self.searchframe,text='Clear',command=lambda:self.clearSearch())
        self.clear.place(relx=0.1,rely=0.775,relwidth=0.8,relheight=0.2)
        
    def pickMade(self):
        del draftorder[0]
        self.t['text']=draftorder[0]
        self.t1['text']=draftorder[0]
        self.t2['text']=draftorder[1]
        self.t3['text']=draftorder[2]
        self.setRoster(draftorder[0])
        self.changeRoster()
        self.hideEmpty()
        self.setInfoFrame()

    def changePlayer(self, player):
        df['Team'][indexes[player]]=draftorder[0]
        topten.clear()
        indexes.clear()
        i=0
        while i<len(df['Team']):
            if df['Team'][i]=='none':
                picktext= str(df['Rank'][i])+' '+df['Name'][i]+' '+df['Position'][i]+' '+str(df['Overall'][i])
                topten.append(picktext)
                indexes.append(df['Rank'][i]-1)
            i+=1
        self.p1['text']=topten[0]
        self.p2['text']=topten[1]
        self.p3['text']=topten[2]
        self.p4['text']=topten[3]
        self.p5['text']=topten[4]
        self.p6['text']=topten[5]
        self.p7['text']=topten[6]
        self.p8['text']=topten[7]
        self.p9['text']=topten[8]
        self.p10['text']=topten[9]
        if search[0]==True:
            self.clearSearch()   
        self.pickMade()

    def setInfoFrame(self):
        self.pg['text']='Point Guards on roster: '+str(self.positionCount('PG'))
        self.pgo['text']='Average overall: '+str(self.positionOverall('PG'))

        self.sg['text']='Shooting Guards on roster: '+str(self.positionCount('SG'))
        self.sgo['text']='Average overall: '+str(self.positionOverall('SG'))

        self.sf['text']='Small Forwards on roster: '+str(self.positionCount('SF'))
        self.sfo['text']='Average overall: '+str(self.positionOverall('SF'))

        self.pf['text']='Power Forwards on roster: '+str(self.positionCount('PF'))
        self.pfo['text']='Average overall: '+str(self.positionOverall('PF'))

        self.c['text']='Centers on roster: '+str(self.positionCount('C'))
        self.co['text']='Average overall: '+str(self.positionOverall('C'))

    #hides empty spots on roster list and reveals filled spots
    def hideEmpty(self):
        if self.r1['text']=='empty':
            self.r1['bg']='black'
            self.o1['bg']='black'
            self.po1['bg']='black'
        else:
            self.r1['bg']='white'
            self.o1['bg']='white'
            self.po1['bg']='white'
        if self.r2['text']=='empty':
            self.r2['bg']='black'
            self.o2['bg']='black'
            self.po2['bg']='black'
        else:
            self.r2['bg']='white'
            self.o2['bg']='white'
            self.po2['bg']='white'
        if self.r3['text']=='empty':
            self.r3['bg']='black'
            self.o3['bg']='black'
            self.po3['bg']='black'
        else:
            self.r3['bg']='white'
            self.o3['bg']='white'
            self.po3['bg']='white'
        if self.r4['text']=='empty':
            self.r4['bg']='black'
            self.o4['bg']='black'
            self.po4['bg']='black'
        else:
            self.r4['bg']='white'
            self.o4['bg']='white'
            self.po4['bg']='white'
        if self.r5['text']=='empty':
            self.r5['bg']='black'
            self.o5['bg']='black'
            self.po5['bg']='black'
        else:
            self.r5['bg']='white'
            self.o5['bg']='white'
            self.po5['bg']='white'
        if self.r6['text']=='empty':
            self.r6['bg']='black'
            self.o6['bg']='black'
            self.po6['bg']='black'
        else:
            self.r6['bg']='white'
            self.o6['bg']='white'
            self.po6['bg']='white'
        if self.r7['text']=='empty':
            self.r7['bg']='black'
            self.o7['bg']='black'
            self.po7['bg']='black'
        else:
            self.r7['bg']='white'
            self.o7['bg']='white'
            self.po7['bg']='white'
        if self.r8['text']=='empty':
            self.r8['bg']='black'
            self.o8['bg']='black'
            self.po8['bg']='black'
        else:
            self.r8['bg']='white'
            self.o8['bg']='white'
            self.po8['bg']='white'
        if self.r9['text']=='empty':
            self.r9['bg']='black'
            self.o9['bg']='black'
            self.po9['bg']='black'
        else:
            self.r9['bg']='white'
            self.o9['bg']='white'
            self.po9['bg']='white'
        if self.r10['text']=='empty':
            self.r10['bg']='black'
            self.o10['bg']='black'
            self.po10['bg']='black'
        else:
            self.r10['bg']='white'
            self.o10['bg']='white'
            self.po10['bg']='white'
        if self.r11['text']=='empty':
            self.r11['bg']='black'
            self.o11['bg']='black'
            self.po11['bg']='black'
        else:
            self.r11['bg']='white'
            self.o11['bg']='white'
            self.po11['bg']='white'
        if self.r12['text']=='empty':
            self.r12['bg']='black'
            self.o12['bg']='black'
            self.po12['bg']='black'
        else:
            self.r12['bg']='white'
            self.o12['bg']='white'
            self.po12['bg']='white'
        if self.r13['text']=='empty':
            self.r13['bg']='black'
            self.o13['bg']='black'
            self.po13['bg']='black'
        else:
            self.r13['bg']='white'
            self.o13['bg']='white'
            self.po13['bg']='white'
        if self.r14['text']=='empty':
            self.r14['bg']='black'
            self.o14['bg']='black'
            self.po14['bg']='black'
        else:
            self.r14['bg']='white'
            self.o14['bg']='white'
            self.po14['bg']='white'
        if self.r15['text']=='empty':
            self.r15['bg']='black'
            self.o15['bg']='black'
            self.po15['bg']='black'
        else:
            self.r15['bg']='white'
            self.o15['bg']='white'
            self.po15['bg']='white'
        if self.r16['text']=='empty':
            self.r16['bg']='black'
            self.o16['bg']='black'
            self.po16['bg']='black'
        else:
            self.r16['bg']='white'
            self.o16['bg']='white'
            self.po16['bg']='white'
        if self.r17['text']=='empty':
            self.r17['bg']='black'
            self.o17['bg']='black'
            self.po17['bg']='black'
        else:
            self.r17['bg']='white'
            self.o17['bg']='white'
            self.po17['bg']='white'
        if self.r18['text']=='empty':
            self.r18['bg']='black'
            self.o18['bg']='black'
            self.po18['bg']='black'
        else:
            self.r18['bg']='white'
            self.o18['bg']='white'
            self.po18['bg']='white'

    #sets roster to current teams roster
    def setRoster(self, team):
        self.resetRoster()
        count=0
        i=0
        while i<len(df['Team']):
            if df['Team'][i]==team:
                roster[0][count]=df['Name'][i]
                roster[1][count]=df['Overall'][i]
                roster[2][count]=df['Position'][i]
                count+=1
            i+=1
                
    #resets roster to default
    def resetRoster(self):
        i=0
        while i<len(roster):
            k=0
            while k<len(roster[i]):
                if i==0:
                    roster[i][k]='empty'
                elif i==1:
                    roster[i][k]=0
                elif i==2:
                    roster[i][k]=0
                k+=1
            i+=1

    #changes display to show current values of roster
    def changeRoster(self):
        self.r1['text']=roster[0][0]
        self.r2['text']=roster[0][1]
        self.r3['text']=roster[0][2]
        self.r4['text']=roster[0][3]
        self.r5['text']=roster[0][4]
        self.r6['text']=roster[0][5]
        self.r7['text']=roster[0][6]
        self.r8['text']=roster[0][7]
        self.r9['text']=roster[0][8]
        self.r10['text']=roster[0][9]
        self.r11['text']=roster[0][10]
        self.r12['text']=roster[0][11]
        self.r13['text']=roster[0][12]
        self.r14['text']=roster[0][13]
        self.r15['text']=roster[0][14]

        self.o1['text']=roster[1][0]
        self.o2['text']=roster[1][1]
        self.o3['text']=roster[1][2]
        self.o4['text']=roster[1][3]
        self.o5['text']=roster[1][4]
        self.o6['text']=roster[1][5]
        self.o7['text']=roster[1][6]
        self.o8['text']=roster[1][7]
        self.o9['text']=roster[1][8]
        self.o10['text']=roster[1][9]
        self.o11['text']=roster[1][10]
        self.o12['text']=roster[1][11]
        self.o13['text']=roster[1][12]
        self.o14['text']=roster[1][13]
        self.o15['text']=roster[1][14]
        
        self.po1['text']=roster[2][0]
        self.po2['text']=roster[2][1]
        self.po3['text']=roster[2][2]
        self.po4['text']=roster[2][3]
        self.po5['text']=roster[2][4]
        self.po6['text']=roster[2][5]
        self.po7['text']=roster[2][6]
        self.po8['text']=roster[2][7]
        self.po9['text']=roster[2][8]
        self.po10['text']=roster[2][9]
        self.po11['text']=roster[2][10]
        self.po12['text']=roster[2][11]
        self.po13['text']=roster[2][12]
        self.po14['text']=roster[2][13]
        self.po15['text']=roster[2][14]

    def Search(self):
        sposition=self.nullselect.get()
        if sposition=='Point Guard':
            sposition='PG'
        elif sposition=='Shooting Guard':
            sposition='SG'
        elif sposition=='Small Forward':
            sposition='SF'
        elif sposition=='Power Forward':
            sposition='PF'
        elif sposition=='Center':
            sposition='C'
        sname=self.sbar.get()
        i=0
        while i<len(df['Name']):
            if df['Name'][i]==sname and df['Team'][i]=='none':
                indexes.clear()
                topten.clear()
                indexes.append(df['Rank'][i]-1)
                picktext= str(df['Rank'][i])+' '+df['Name'][i]+' '+df['Position'][i]+' '+str(df['Overall'][i])
                topten.append(picktext)
                self.p1['text']=topten[0]
                self.p2.place_forget()
                self.p3.place_forget()
                self.p4.place_forget()
                self.p5.place_forget()
                self.p6.place_forget()
                self.p7.place_forget()
                self.p8.place_forget()
                self.p9.place_forget()
                self.p10.place_forget()
                search[0]=True
                return
            i+=1
        i=0
        n=0
        #bugs=when there aren't ten in position
        indexes.clear()
        topten.clear()
        while i<len(df['Position']):
            if df['Position'][i]==sposition and df['Team'][i]=='none':
                #set top ten left at position
                indexes.append(df['Rank'][i]-1)
                picktext= str(df['Rank'][i])+' '+df['Name'][i]+' '+df['Position'][i]+' '+str(df['Overall'][i])
                topten.append(picktext)
                n+=1
            i+=1
        if n>9:
            self.p1['text']=topten[0]
            self.p2['text']=topten[1]
            self.p3['text']=topten[2]
            self.p4['text']=topten[3]
            self.p5['text']=topten[4]
            self.p6['text']=topten[5]
            self.p7['text']=topten[6]
            self.p8['text']=topten[7]
            self.p9['text']=topten[8]
            self.p10['text']=topten[9]
        elif n>8:
            self.p1['text']=topten[0]
            self.p2['text']=topten[1]
            self.p3['text']=topten[2]
            self.p4['text']=topten[3]
            self.p5['text']=topten[4]
            self.p6['text']=topten[5]
            self.p7['text']=topten[6]
            self.p8['text']=topten[7]
            self.p9['text']=topten[8]
            self.p10.place_forget()
            search[0]=True
        elif n>7:
            self.p1['text']=topten[0]
            self.p2['text']=topten[1]
            self.p3['text']=topten[2]
            self.p4['text']=topten[3]
            self.p5['text']=topten[4]
            self.p6['text']=topten[5]
            self.p7['text']=topten[6]
            self.p8['text']=topten[7]
            self.p9.place_forget()
            self.p10.place_forget()
            search[0]=True
        elif n>6:
            self.p1['text']=topten[0]
            self.p2['text']=topten[1]
            self.p3['text']=topten[2]
            self.p4['text']=topten[3]
            self.p5['text']=topten[4]
            self.p6['text']=topten[5]
            self.p7['text']=topten[6]
            self.p8.place_forget()
            self.p9.place_forget()
            self.p10.place_forget()
            search[0]=True
        elif n>5:
            self.p1['text']=topten[0]
            self.p2['text']=topten[1]
            self.p3['text']=topten[2]
            self.p4['text']=topten[3]
            self.p5['text']=topten[4]
            self.p6['text']=topten[5]
            self.p7.place_forget()
            self.p8.place_forget()
            self.p9.place_forget()
            self.p10.place_forget()
            search[0]=True
        elif n>4:
            self.p1['text']=topten[0]
            self.p2['text']=topten[1]
            self.p3['text']=topten[2]
            self.p4['text']=topten[3]
            self.p5['text']=topten[4]
            self.p6.place_forget()
            self.p7.place_forget()
            self.p8.place_forget()
            self.p9.place_forget()
            self.p10.place_forget()
            search[0]=True
        elif n>3:
            self.p1['text']=topten[0]
            self.p2['text']=topten[1]
            self.p3['text']=topten[2]
            self.p4['text']=topten[3]
            self.p5.place_forget()
            self.p6.place_forget()
            self.p7.place_forget()
            self.p8.place_forget()
            self.p9.place_forget()
            self.p10.place_forget()
            search[0]=True
        elif n>2:
            self.p1['text']=topten[0]
            self.p2['text']=topten[1]
            self.p3['text']=topten[2]
            self.p4.place_forget()
            self.p5.place_forget()
            self.p6.place_forget()
            self.p7.place_forget()
            self.p8.place_forget()
            self.p9.place_forget()
            self.p10.place_forget()
            search[0]=True
        elif n>1:
            self.p1['text']=topten[0]
            self.p2['text']=topten[1]
            self.p3.place_forget()
            self.p4.place_forget()
            self.p5.place_forget()
            self.p6.place_forget()
            self.p7.place_forget()
            self.p8.place_forget()
            self.p9.place_forget()
            self.p10.place_forget()
            search[0]=True
        elif n>0:
            self.p1['text']=topten[0]
            self.p2.place_forget()
            self.p3.place_forget()
            self.p4.place_forget()
            self.p5.place_forget()
            self.p6.place_forget()
            self.p7.place_forget()
            self.p8.place_forget()
            self.p9.place_forget()
            self.p10.place_forget()
            search[0]=True
        elif n==0:
            self.p1.place_forget()
            self.p2.place_forget()
            self.p3.place_forget()
            self.p4.place_forget()
            self.p5.place_forget()
            self.p6.place_forget()
            self.p7.place_forget()
            self.p8.place_forget()
            self.p9.place_forget()
            self.p10.place_forget()
            search[0]=True
        sbutton['text']='no results'

    #clears the current search
    def clearSearch(self):
        self.sbar.delete(0,'end')
        self.sbar.insert(0,'')
        self.sbar.config(fg='black')
        self.nullselect.set('Select a position')
        topten.clear()
        indexes.clear()
        i=0
        while i<len(df['Team']):
            if df['Team'][i]=='none':
                picktext= str(df['Rank'][i])+' '+df['Name'][i]+' '+df['Position'][i]+' '+str(df['Overall'][i])
                topten.append(picktext)
                indexes.append(df['Rank'][i]-1)
            i+=1
        self.p1['text']=topten[0]
        self.p2['text']=topten[1]
        self.p3['text']=topten[2]
        self.p4['text']=topten[3]
        self.p5['text']=topten[4]
        self.p6['text']=topten[5]
        self.p7['text']=topten[6]
        self.p8['text']=topten[7]
        self.p9['text']=topten[8]
        self.p10['text']=topten[9]
        if search[0]==True:
            self.p1.place(relx=0,rely=0,relwidth=1,relheight=0.1)
            self.p2.place(relx=0,rely=0.1,relwidth=1,relheight=0.1)
            self.p3.place(relx=0,rely=0.2,relwidth=1,relheight=0.1)
            self.p4.place(relx=0,rely=0.3,relwidth=1,relheight=0.1)
            self.p5.place(relx=0,rely=0.4,relwidth=1,relheight=0.1)
            self.p6.place(relx=0,rely=0.5,relwidth=1,relheight=0.1)
            self.p7.place(relx=0,rely=0.6,relwidth=1,relheight=0.1)
            self.p8.place(relx=0,rely=0.7,relwidth=1,relheight=0.1)
            self.p9.place(relx=0,rely=0.8,relwidth=1,relheight=0.1)
            self.p10.place(relx=0,rely=0.9,relwidth=1,relheight=0.1) 

    #defines actions when search bar is clicked
    def on_entry_click(self, event):
        if self.sbar.get()=='Search Player Name':
            self.sbar.delete(0,'end')
            self.sbar.insert(0,'')
            self.sbar.config(fg='black')

    #defines actions when search bar is exited
    def on_focusout(self, event):
        if self.sbar.get()=='':
            self.sbar.insert(0,'Search Player Name')
            self.sbar.config(fg='grey')
            
    #counts number of a certain position on roster
    def positionCount(self, position):
        count=0
        i=0
        while i<len(roster[2]):
            if roster[2][i]==position:
                count+=1
            i+=1  
        return count

    #averages the overalls of a certain position on roster
    def positionOverall(self, position):
        count=self.positionCount(position)
        sum=0
        i=0
        while i<len(roster[1]):
            if roster[2][i]==position:
                sum+=roster[1][i]
            i+=1
        if sum ==0:
            return 0
        else:
            return sum/count