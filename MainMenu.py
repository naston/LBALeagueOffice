import tkinter as tk 
import os
import numpy as np
import pandas as pd
#import Network
"""
run=True
draft=False
n=Network()
win=[]
win.append(int(n.getTeam()))
"""
HEIGHT=750
WIDTH=1200
draftorder=['Grizz','Grizz','Grizz','Kings','Grizz','Nuggets','test','test','test']
roster=[['empty','empty','empty','empty','empty','empty','empty','empty','empty','empty','empty','empty','empty','empty','empty','empty','empty','empty'],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']]
topten=[]
indexes=[]
df= pd.read_csv('LeaguePlayerDataBase.csv')
search=[False]
    

#players=['Lebron James','Kevin Durant']
"""
def openWindow():
    top = tk.Toplevel()
    top.title('Draft Central')
    draftcanvas=tk.Canvas(top,width=WIDTH,height=HEIGHT)
    draftcanvas.pack()
    
    teamframe = tk.Frame(draftcanvas,bg='black')
    teamframe.place(relx=0,rely=0,relwidth=0.6,relheight=0.2)

    nextframe = tk.Frame(draftcanvas,bg='green')
    nextframe.place(relx=0.6,rely=0,relwidth=0.2,relheight=0.2)

    secondframe = tk.Frame(draftcanvas,bg='blue')
    secondframe.place(relx=0.8,rely=0,relwidth=0.2,relheight=0.2)

    pickframe = tk.Frame(draftcanvas,bg='yellow')
    pickframe.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.8)

    searchframe = tk.Frame(draftcanvas,bg='orange')
    searchframe.place(relx=0,rely=0.2,relwidth=0.2,relheight=0.8)

    currentroster = tk.Frame(draftcanvas,bg='purple')
    currentroster.place(relx=0.8,rely=0.2,relwidth=0.2,relheight=0.6)

    confirmframe = tk.Frame(draftcanvas,bg='red')
    confirmframe.place(relx=0.8,rely=0.8,relwidth=0.2,relheight=0.2)

    
    f=tk.Button(pickframe, text=players[0], command=lambda:changeColor())
    f.place(relx=0,rely=0,relwidth=1,relheight=0.2)
    #not a great option here, label disapears on press
    #playername=tk.Label(f,text=)
    #playername.place(relx=0,rely=0,relwidth=0.5,relheight=1)
"""

"""
def createMessage(pageType,bg):
    return str(pageType)+','+bg

def readMessage(message):
    message = message.split(',')
    return message

def changeWindow(pageType):
    if pageType == 0:
        wait.place_forget()
        frame.place(relx=0,rely=0,relwidth=1,relheight=1)

    else:
        frame.place_forget()
        wait.place(relx=0,rely=0,relwidth=1,relheight=1)
"""

#draft functions
#function that sets initial values for topten and indexes
def start():
    i=0
    while i<len(df['Team']):
        if df['Team'][i]=='none':
            picktext= str(df['Rank'][i])+' '+df['Name'][i]+' '+df['Position'][i]+' '+str(df['Overall'][i])
            topten.append(picktext)
            indexes.append(df['Rank'][i]-1)
        i+=1

#function that brings in selection order
#def setPickOrder():

#gives set of actions when pick is made
def pickMade():
    del draftorder[0]
    t['text']=draftorder[0]
    t1['text']=draftorder[0]
    t2['text']=draftorder[1]
    t3['text']=draftorder[2]
    setRoster(draftorder[0])
    changeRoster()
    hideEmpty()
    setInfoFrame()

#add team to player/, clear and reenter topten array/, reset buttons/,change teams
def changePlayer(player):
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
    p1['text']=topten[0]
    p2['text']=topten[1]
    p3['text']=topten[2]
    p4['text']=topten[3]
    p5['text']=topten[4]
    p6['text']=topten[5]
    p7['text']=topten[6]
    p8['text']=topten[7]
    p9['text']=topten[8]
    p10['text']=topten[9]
    if search[0]==True:
        clearSearch()   
    pickMade()

#sets number of players at each position and the positions avg overall
def setInfoFrame():
    pg['text']='Point Guards on roster: '+str(positionCount('PG'))
    pgo['text']='Average overall: '+str(positionOverall('PG'))

    sg['text']='Shooting Guards on roster: '+str(positionCount('SG'))
    sgo['text']='Average overall: '+str(positionOverall('SG'))

    sf['text']='Small Forwards on roster: '+str(positionCount('SF'))
    sfo['text']='Average overall: '+str(positionOverall('SF'))

    pf['text']='Power Forwards on roster: '+str(positionCount('PF'))
    pfo['text']='Average overall: '+str(positionOverall('PF'))

    c['text']='Centers on roster: '+str(positionCount('C'))
    co['text']='Average overall: '+str(positionOverall('C'))

#hides empty spots on roster list and reveals filled spots
def hideEmpty():
    if r1['text']=='empty':
        r1['bg']='black'
        o1['bg']='black'
        po1['bg']='black'
    else:
        r1['bg']='white'
        o1['bg']='white'
        po1['bg']='white'
    if r2['text']=='empty':
        r2['bg']='black'
        o2['bg']='black'
        po2['bg']='black'
    else:
        r2['bg']='white'
        o2['bg']='white'
        po2['bg']='white'
    if r3['text']=='empty':
        r3['bg']='black'
        o3['bg']='black'
        po3['bg']='black'
    else:
        r3['bg']='white'
        o3['bg']='white'
        po3['bg']='white'
    if r4['text']=='empty':
        r4['bg']='black'
        o4['bg']='black'
        po4['bg']='black'
    else:
        r4['bg']='white'
        o4['bg']='white'
        po4['bg']='white'
    if r5['text']=='empty':
        r5['bg']='black'
        o5['bg']='black'
        po5['bg']='black'
    else:
        r5['bg']='white'
        o5['bg']='white'
        po5['bg']='white'
    if r6['text']=='empty':
        r6['bg']='black'
        o6['bg']='black'
        po6['bg']='black'
    else:
        r6['bg']='white'
        o6['bg']='white'
        po6['bg']='white'
    if r7['text']=='empty':
        r7['bg']='black'
        o7['bg']='black'
        po7['bg']='black'
    else:
        r7['bg']='white'
        o7['bg']='white'
        po7['bg']='white'
    if r8['text']=='empty':
        r8['bg']='black'
        o8['bg']='black'
        po8['bg']='black'
    else:
        r8['bg']='white'
        o8['bg']='white'
        po8['bg']='white'
    if r9['text']=='empty':
        r9['bg']='black'
        o9['bg']='black'
        po9['bg']='black'
    else:
        r9['bg']='white'
        o9['bg']='white'
        po9['bg']='white'
    if r10['text']=='empty':
        r10['bg']='black'
        o10['bg']='black'
        po10['bg']='black'
    else:
        r10['bg']='white'
        o10['bg']='white'
        po10['bg']='white'
    if r11['text']=='empty':
        r11['bg']='black'
        o11['bg']='black'
        po11['bg']='black'
    else:
        r11['bg']='white'
        o11['bg']='white'
        po11['bg']='white'
    if r12['text']=='empty':
        r12['bg']='black'
        o12['bg']='black'
        po12['bg']='black'
    else:
        r12['bg']='white'
        o12['bg']='white'
        po12['bg']='white'
    if r13['text']=='empty':
        r13['bg']='black'
        o13['bg']='black'
        po13['bg']='black'
    else:
        r13['bg']='white'
        o13['bg']='white'
        po13['bg']='white'
    if r14['text']=='empty':
        r14['bg']='black'
        o14['bg']='black'
        po14['bg']='black'
    else:
        r14['bg']='white'
        o14['bg']='white'
        po14['bg']='white'
    if r15['text']=='empty':
        r15['bg']='black'
        o15['bg']='black'
        po15['bg']='black'
    else:
        r15['bg']='white'
        o15['bg']='white'
        po15['bg']='white'
    if r16['text']=='empty':
        r16['bg']='black'
        o16['bg']='black'
        po16['bg']='black'
    else:
        r16['bg']='white'
        o16['bg']='white'
        po16['bg']='white'
    if r17['text']=='empty':
        r17['bg']='black'
        o17['bg']='black'
        po17['bg']='black'
    else:
        r17['bg']='white'
        o17['bg']='white'
        po17['bg']='white'
    if r18['text']=='empty':
        r18['bg']='black'
        o18['bg']='black'
        po18['bg']='black'
    else:
        r18['bg']='white'
        o18['bg']='white'
        po18['bg']='white'

#sets roster to current teams roster
def setRoster(team):
    resetRoster()
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
def resetRoster():
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
def changeRoster():
    r1['text']=roster[0][0]
    r2['text']=roster[0][1]
    r3['text']=roster[0][2]
    r4['text']=roster[0][3]
    r5['text']=roster[0][4]
    r6['text']=roster[0][5]
    r7['text']=roster[0][6]
    r8['text']=roster[0][7]
    r9['text']=roster[0][8]
    r10['text']=roster[0][9]
    r11['text']=roster[0][10]
    r12['text']=roster[0][11]
    r13['text']=roster[0][12]
    r14['text']=roster[0][13]
    r15['text']=roster[0][14]

    o1['text']=roster[1][0]
    o2['text']=roster[1][1]
    o3['text']=roster[1][2]
    o4['text']=roster[1][3]
    o5['text']=roster[1][4]
    o6['text']=roster[1][5]
    o7['text']=roster[1][6]
    o8['text']=roster[1][7]
    o9['text']=roster[1][8]
    o10['text']=roster[1][9]
    o11['text']=roster[1][10]
    o12['text']=roster[1][11]
    o13['text']=roster[1][12]
    o14['text']=roster[1][13]
    o15['text']=roster[1][14]
    
    po1['text']=roster[2][0]
    po2['text']=roster[2][1]
    po3['text']=roster[2][2]
    po4['text']=roster[2][3]
    po5['text']=roster[2][4]
    po6['text']=roster[2][5]
    po7['text']=roster[2][6]
    po8['text']=roster[2][7]
    po9['text']=roster[2][8]
    po10['text']=roster[2][9]
    po11['text']=roster[2][10]
    po12['text']=roster[2][11]
    po13['text']=roster[2][12]
    po14['text']=roster[2][13]
    po15['text']=roster[2][14]

#when search button pressed pass full fields to this function
def Search():
    sposition=nullselect.get()
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
    sname=sbar.get()
    i=0
    while i<len(df['Name']):
        if df['Name'][i]==sname and df['Team'][i]=='none':
            indexes.clear()
            topten.clear()
            indexes.append(df['Rank'][i]-1)
            picktext= str(df['Rank'][i])+' '+df['Name'][i]+' '+df['Position'][i]+' '+str(df['Overall'][i])
            topten.append(picktext)
            p1['text']=topten[0]
            p2.place_forget()
            p3.place_forget()
            p4.place_forget()
            p5.place_forget()
            p6.place_forget()
            p7.place_forget()
            p8.place_forget()
            p9.place_forget()
            p10.place_forget()
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
        p1['text']=topten[0]
        p2['text']=topten[1]
        p3['text']=topten[2]
        p4['text']=topten[3]
        p5['text']=topten[4]
        p6['text']=topten[5]
        p7['text']=topten[6]
        p8['text']=topten[7]
        p9['text']=topten[8]
        p10['text']=topten[9]
    elif n>8:
        p1['text']=topten[0]
        p2['text']=topten[1]
        p3['text']=topten[2]
        p4['text']=topten[3]
        p5['text']=topten[4]
        p6['text']=topten[5]
        p7['text']=topten[6]
        p8['text']=topten[7]
        p9['text']=topten[8]
        p10.place_forget()
        search[0]=True
    elif n>7:
        p1['text']=topten[0]
        p2['text']=topten[1]
        p3['text']=topten[2]
        p4['text']=topten[3]
        p5['text']=topten[4]
        p6['text']=topten[5]
        p7['text']=topten[6]
        p8['text']=topten[7]
        p9.place_forget()
        p10.place_forget()
        search[0]=True
    elif n>6:
        p1['text']=topten[0]
        p2['text']=topten[1]
        p3['text']=topten[2]
        p4['text']=topten[3]
        p5['text']=topten[4]
        p6['text']=topten[5]
        p7['text']=topten[6]
        p8.place_forget()
        p9.place_forget()
        p10.place_forget()
        search[0]=True
    elif n>5:
        p1['text']=topten[0]
        p2['text']=topten[1]
        p3['text']=topten[2]
        p4['text']=topten[3]
        p5['text']=topten[4]
        p6['text']=topten[5]
        p7.place_forget()
        p8.place_forget()
        p9.place_forget()
        p10.place_forget()
        search[0]=True
    elif n>4:
        p1['text']=topten[0]
        p2['text']=topten[1]
        p3['text']=topten[2]
        p4['text']=topten[3]
        p5['text']=topten[4]
        p6.place_forget()
        p7.place_forget()
        p8.place_forget()
        p9.place_forget()
        p10.place_forget()
        search[0]=True
    elif n>3:
        p1['text']=topten[0]
        p2['text']=topten[1]
        p3['text']=topten[2]
        p4['text']=topten[3]
        p5.place_forget()
        p6.place_forget()
        p7.place_forget()
        p8.place_forget()
        p9.place_forget()
        p10.place_forget()
        search[0]=True
    elif n>2:
        p1['text']=topten[0]
        p2['text']=topten[1]
        p3['text']=topten[2]
        p4.place_forget()
        p5.place_forget()
        p6.place_forget()
        p7.place_forget()
        p8.place_forget()
        p9.place_forget()
        p10.place_forget()
        search[0]=True
    elif n>1:
        p1['text']=topten[0]
        p2['text']=topten[1]
        p3.place_forget()
        p4.place_forget()
        p5.place_forget()
        p6.place_forget()
        p7.place_forget()
        p8.place_forget()
        p9.place_forget()
        p10.place_forget()
        search[0]=True
    elif n>0:
        p1['text']=topten[0]
        p2.place_forget()
        p3.place_forget()
        p4.place_forget()
        p5.place_forget()
        p6.place_forget()
        p7.place_forget()
        p8.place_forget()
        p9.place_forget()
        p10.place_forget()
        search[0]=True
    elif n==0:
        p1.place_forget()
        p2.place_forget()
        p3.place_forget()
        p4.place_forget()
        p5.place_forget()
        p6.place_forget()
        p7.place_forget()
        p8.place_forget()
        p9.place_forget()
        p10.place_forget()
        search[0]=True
    sbutton['text']='no results'

#clears the current search
def clearSearch():
    sbar.delete(0,'end')
    sbar.insert(0,'')
    sbar.config(fg='black')
    nullselect.set('Select a position')
    topten.clear()
    indexes.clear()
    i=0
    while i<len(df['Team']):
        if df['Team'][i]=='none':
            picktext= str(df['Rank'][i])+' '+df['Name'][i]+' '+df['Position'][i]+' '+str(df['Overall'][i])
            topten.append(picktext)
            indexes.append(df['Rank'][i]-1)
        i+=1
    p1['text']=topten[0]
    p2['text']=topten[1]
    p3['text']=topten[2]
    p4['text']=topten[3]
    p5['text']=topten[4]
    p6['text']=topten[5]
    p7['text']=topten[6]
    p8['text']=topten[7]
    p9['text']=topten[8]
    p10['text']=topten[9]
    if search[0]==True:
        p1.place(relx=0,rely=0,relwidth=1,relheight=0.1)
        p2.place(relx=0,rely=0.1,relwidth=1,relheight=0.1)
        p3.place(relx=0,rely=0.2,relwidth=1,relheight=0.1)
        p4.place(relx=0,rely=0.3,relwidth=1,relheight=0.1)
        p5.place(relx=0,rely=0.4,relwidth=1,relheight=0.1)
        p6.place(relx=0,rely=0.5,relwidth=1,relheight=0.1)
        p7.place(relx=0,rely=0.6,relwidth=1,relheight=0.1)
        p8.place(relx=0,rely=0.7,relwidth=1,relheight=0.1)
        p9.place(relx=0,rely=0.8,relwidth=1,relheight=0.1)
        p10.place(relx=0,rely=0.9,relwidth=1,relheight=0.1) 

#defines actions when search bar is clicked
def on_entry_click(event):
    if sbar.get()=='Search Player Name':
        sbar.delete(0,'end')
        sbar.insert(0,'')
        sbar.config(fg='black')

#defines actions when search bar is exited
def on_focusout(event):
    if sbar.get()=='':
        sbar.insert(0,'Search Player Name')
        sbar.config(fg='grey')
        
#counts number of a certain position on roster
def positionCount(position):
    count=0
    i=0
    while i<len(roster[2]):
        if roster[2][i]==position:
            count+=1
        i+=1  
    return count

#averages the overalls of a certain position on roster
def positionOverall(position):
    count=positionCount(position)
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

#function that writes to csv at end of draft
#def endOfDraft():

#def changeColor():
    #del players[0]

def Lottery():
    homepage.place_forget()
    homebutton.place(relx=0,rely=0,relwidth=1,relheight=1)

def draftPage():
    homepage.place_forget()
    draftpage.place(relx=0,rely=0,relwidth=1,relheight=1)
    #draft=True

def progressPage():
    homepage.place_forget()
    inprogressframe.place(relx=0,rely=0,relwidth=1,relheight=1)

def pregressHome():
    inprogressframe.place_forget()
    homepage.place(relx=0,rely=0,relwidth=1,relheight=1)

#def draftHome():
    #draftframe.place_forget()
    #homepage.place(relx=0,rely=0,relwidth=1,relheight=1)

def Home():
    homebutton.place_forget()
    homepage.place(relx=0,rely=0,relwidth=1,relheight=1)


root = tk.Tk()
root.title('LBA League Office')
start()
canvas= tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()
#main home frame
homepage=tk.Frame(canvas)
homepage.place(relx=0,rely=0,relwidth=1,relheight=1)
#home frames
buttonLeft=tk.Frame(homepage,bg='black')
buttonLeft.place(relx=0,rely=0.25,relwidth=0.5,relheight=0.5)
buttonRight=tk.Frame(homepage,bg='black')
buttonRight.place(relx=0.5,rely=0.25,relwidth=0.5,relheight=0.5)
titleFrame=tk.Frame(homepage,bg='black')
titleFrame.place(relx=0,rely=0,relwidth=1,relheight=0.25)
version=tk.Frame(homepage,bg='black')
version.place(relx=0,rely=.75,relwidth=1,relheight=.25)
#left side home buttons
addResults=tk.Button(buttonLeft,text='Add Results',font=('Courier',20),command=lambda:progressPage())
addResults.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.2)
createSeason=tk.Button(buttonLeft,text='Create Season',font=('Courier',20),command=lambda:progressPage())
createSeason.place(relx=0.1,rely=0.30,relwidth=0.8,relheight=0.2)
createBracket=tk.Button(buttonLeft,text='Create Bracket',font=('Courier',20),command=lambda:progressPage())
createBracket.place(relx=0.1,rely=0.55,relwidth=0.8,relheight=0.2)
currentStandings=tk.Button(buttonLeft,text='Current Standings',font=('Courier',20),command=lambda:progressPage())
currentStandings.place(relx=0.1,rely=0.8,relwidth=0.8,relheight=0.2)
#right side home buttons
draft=tk.Button(buttonRight,text='Draft',command=lambda:draftPage(),font=('Courier',20))
draft.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.2)
lottery=tk.Button(buttonRight,text='Pick Lottery',command=lambda:progressPage(),font=('Courier',20))
lottery.place(relx=0.1,rely=0.30,relwidth=0.8,relheight=0.2)
trade=tk.Button(buttonRight,text='Trade',font=('Courier',20),command=lambda:progressPage())
trade.place(relx=0.1,rely=0.55,relwidth=0.8,relheight=0.2)
messagecenter=tk.Button(buttonRight,text='Message Center',font=('Courier',20),command=lambda:progressPage())
messagecenter.place(relx=0.1,rely=0.8,relwidth=0.8,relheight=0.2)
#title label
title=tk.Label(titleFrame,text='LBA GM Room',font=('Courier',44),fg='white',bg='black')
title.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.9)
#version label

#exit button
homebutton=tk.Button(canvas,text='home',bg='black',command=lambda:Home())

#draft page
"""
draftframe=tk.Frame(canvas,bg='black')

nextteam=tk.Frame(draftframe,bg='white')
nextteam.place(relx=0,rely=0.8,relwidth=0.2,relheight=0.2)
draftboard=tk.Frame(draftframe,bg='yellow')
draftboard.place(relx=0.6,rely=0.2,relwidth=0.4,relheight=0.8)
currentteam=tk.Frame(draftframe,bg='orange')
currentteam.place(relx=0,rely=0,relwidth=1,relheight=0.2)
displayframe=tk.Frame(draftframe,bg='green')
displayframe.place(relx=0,rely=0.2,relwidth=0.6,relheight=0.6)
homebutton1=tk.Button(currentteam,text='home',bg='black',command=lambda:draftHome())
homebutton1.place(relx=0,rely=0,relwidth=0.1,relheight=0.3)
"""
#lottery page

#bracket page

#trade page

#add results page

#create season page

#standings page

#draft page
draftpage=tk.Frame(canvas)
    

teamframe = tk.Frame(draftpage,bg='black')
teamframe.place(relx=0,rely=0,relwidth=0.6,relheight=0.2)
nextframe = tk.Frame(draftpage,bg='green')
nextframe.place(relx=0.6,rely=0,relwidth=0.2,relheight=0.2)
secondframe = tk.Frame(draftpage,bg='blue')
secondframe.place(relx=0.8,rely=0,relwidth=0.2,relheight=0.2)
pickframe = tk.Frame(draftpage,bg='yellow')
pickframe.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.8)
currentroster = tk.Frame(draftpage,bg='orange')
currentroster.place(relx=0,rely=0.2,relwidth=0.2,relheight=0.8)
searchframe = tk.Frame(draftpage,bg='purple')
searchframe.place(relx=0.8,rely=0.2,relwidth=0.2,relheight=0.4)
infoframe = tk.Frame(draftpage,bg='red')
infoframe.place(relx=0.8,rely=0.6,relwidth=0.2,relheight=0.4)

#labels for team picking and next two teams up
t=tk.Label(teamframe,text=draftorder[0])
t.place(relx=0.05,rely=0.1,relwidth=0.3,relheight=0.8)
t1=tk.Label(teamframe,text=draftorder[0])
t1.place(relx=0.4,rely=0.1,relwidth=0.55,relheight=0.8)
t2=tk.Label(nextframe,text=draftorder[1])
t2.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.8)
t3=tk.Label(secondframe,text=draftorder[2])
t3.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.8)

#labels for current roster
#up max offseason roster size to 18
rtitle=tk.Label(currentroster,text='Current Roster')
rtitle.place(relx=0.1,rely=0,relwidth=0.8,relheight=0.075)
r1=tk.Label(currentroster,text=roster[0][0])
r1.place(relx=0.1,rely=0.0875,relwidth=0.6,relheight=0.05)
r2=tk.Label(currentroster,text=roster[0][1])
r2.place(relx=0.1,rely=0.1375,relwidth=0.6,relheight=0.05)
r3=tk.Label(currentroster,text=roster[0][2])
r3.place(relx=0.1,rely=0.1875,relwidth=0.6,relheight=0.05)
r4=tk.Label(currentroster,text=roster[0][3])
r4.place(relx=0.1,rely=0.2375,relwidth=0.6,relheight=0.05)
r5=tk.Label(currentroster,text=roster[0][4])
r5.place(relx=0.1,rely=0.2875,relwidth=0.6,relheight=0.05)
r6=tk.Label(currentroster,text=roster[0][5])
r6.place(relx=0.1,rely=0.3375,relwidth=0.6,relheight=0.05)
r7=tk.Label(currentroster,text=roster[0][6])
r7.place(relx=0.1,rely=0.3875,relwidth=0.6,relheight=0.05)
r8=tk.Label(currentroster,text=roster[0][7])
r8.place(relx=0.1,rely=0.4375,relwidth=0.6,relheight=0.05)
r9=tk.Label(currentroster,text=roster[0][8])
r9.place(relx=0.1,rely=0.4875,relwidth=0.6,relheight=0.05)
r10=tk.Label(currentroster,text=roster[0][9])
r10.place(relx=0.1,rely=0.5375,relwidth=0.6,relheight=0.05)
r11=tk.Label(currentroster,text=roster[0][10])
r11.place(relx=0.1,rely=0.5875,relwidth=0.6,relheight=0.05)
r12=tk.Label(currentroster,text=roster[0][11])
r12.place(relx=0.1,rely=0.6375,relwidth=0.6,relheight=0.05)
r13=tk.Label(currentroster,text=roster[0][12])
r13.place(relx=0.1,rely=0.6875,relwidth=0.6,relheight=0.05)
r14=tk.Label(currentroster,text=roster[0][13])
r14.place(relx=0.1,rely=0.7375,relwidth=0.6,relheight=0.05)
r15=tk.Label(currentroster,text=roster[0][14])
r15.place(relx=0.1,rely=0.7875,relwidth=0.6,relheight=0.05)
r16=tk.Label(currentroster,text=roster[0][15])
r16.place(relx=0.1,rely=0.8375,relwidth=0.6,relheight=0.05)
r17=tk.Label(currentroster,text=roster[0][16])
r17.place(relx=0.1,rely=0.8875,relwidth=0.6,relheight=0.05)
r18=tk.Label(currentroster,text=roster[0][17])
r18.place(relx=0.1,rely=0.9375,relwidth=0.6,relheight=0.05)
#roster overalls
o1=tk.Label(currentroster,text=roster[1][0])
o1.place(relx=0.8,rely=0.0875,relwidth=0.1,relheight=0.05)
o2=tk.Label(currentroster,text=roster[1][1])
o2.place(relx=0.8,rely=0.1375,relwidth=0.1,relheight=0.05)
o3=tk.Label(currentroster,text=roster[1][2])
o3.place(relx=0.8,rely=0.1875,relwidth=0.1,relheight=0.05)
o4=tk.Label(currentroster,text=roster[1][3])
o4.place(relx=0.8,rely=0.2375,relwidth=0.1,relheight=0.05)
o5=tk.Label(currentroster,text=roster[1][4])
o5.place(relx=0.8,rely=0.2875,relwidth=0.1,relheight=0.05)
o6=tk.Label(currentroster,text=roster[1][5])
o6.place(relx=0.8,rely=0.3375,relwidth=0.1,relheight=0.05)
o7=tk.Label(currentroster,text=roster[1][6])
o7.place(relx=0.8,rely=0.3875,relwidth=0.1,relheight=0.05)
o8=tk.Label(currentroster,text=roster[1][7])
o8.place(relx=0.8,rely=0.4375,relwidth=0.1,relheight=0.05)
o9=tk.Label(currentroster,text=roster[1][8])
o9.place(relx=0.8,rely=0.4875,relwidth=0.1,relheight=0.05)
o10=tk.Label(currentroster,text=roster[1][9])
o10.place(relx=0.8,rely=0.5375,relwidth=0.1,relheight=0.05)
o11=tk.Label(currentroster,text=roster[1][10])
o11.place(relx=0.8,rely=0.5875,relwidth=0.1,relheight=0.05)
o12=tk.Label(currentroster,text=roster[1][11])
o12.place(relx=0.8,rely=0.6375,relwidth=0.1,relheight=0.05)
o13=tk.Label(currentroster,text=roster[1][12])
o13.place(relx=0.8,rely=0.6875,relwidth=0.1,relheight=0.05)
o14=tk.Label(currentroster,text=roster[1][13])
o14.place(relx=0.8,rely=0.7375,relwidth=0.1,relheight=0.05)
o15=tk.Label(currentroster,text=roster[1][14])
o15.place(relx=0.8,rely=0.7875,relwidth=0.1,relheight=0.05)
o16=tk.Label(currentroster,text=roster[1][15])
o16.place(relx=0.8,rely=0.8375,relwidth=0.1,relheight=0.05)
o17=tk.Label(currentroster,text=roster[1][16])
o17.place(relx=0.8,rely=0.8875,relwidth=0.1,relheight=0.05)
o18=tk.Label(currentroster,text=roster[1][17])
o18.place(relx=0.8,rely=0.9375,relwidth=0.1,relheight=0.05)
#position label for each player
po1=tk.Label(currentroster,text=roster[2][0])
po1.place(relx=0.7,rely=0.0875,relwidth=0.1,relheight=0.05)
po2=tk.Label(currentroster,text=roster[2][1])
po2.place(relx=0.7,rely=0.1375,relwidth=0.1,relheight=0.05)
po3=tk.Label(currentroster,text=roster[2][2])
po3.place(relx=0.7,rely=0.1875,relwidth=0.1,relheight=0.05)
po4=tk.Label(currentroster,text=roster[2][3])
po4.place(relx=0.7,rely=0.2375,relwidth=0.1,relheight=0.05)
po5=tk.Label(currentroster,text=roster[2][4])
po5.place(relx=0.7,rely=0.2875,relwidth=0.1,relheight=0.05)
po6=tk.Label(currentroster,text=roster[2][5])
po6.place(relx=0.7,rely=0.3375,relwidth=0.1,relheight=0.05)
po7=tk.Label(currentroster,text=roster[2][6])
po7.place(relx=0.7,rely=0.3875,relwidth=0.1,relheight=0.05)
po8=tk.Label(currentroster,text=roster[2][7])
po8.place(relx=0.7,rely=0.4375,relwidth=0.1,relheight=0.05)
po9=tk.Label(currentroster,text=roster[2][8])
po9.place(relx=0.7,rely=0.4875,relwidth=0.1,relheight=0.05)
po10=tk.Label(currentroster,text=roster[2][9])
po10.place(relx=0.7,rely=0.5375,relwidth=0.1,relheight=0.05)
po11=tk.Label(currentroster,text=roster[2][10])
po11.place(relx=0.7,rely=0.5875,relwidth=0.1,relheight=0.05)
po12=tk.Label(currentroster,text=roster[2][11])
po12.place(relx=0.7,rely=0.6375,relwidth=0.1,relheight=0.05)
po13=tk.Label(currentroster,text=roster[2][12])
po13.place(relx=0.7,rely=0.6875,relwidth=0.1,relheight=0.05)
po14=tk.Label(currentroster,text=roster[2][13])
po14.place(relx=0.7,rely=0.7375,relwidth=0.1,relheight=0.05)
po15=tk.Label(currentroster,text=roster[2][14])
po15.place(relx=0.7,rely=0.7875,relwidth=0.1,relheight=0.05)
po16=tk.Label(currentroster,text=roster[2][15])
po16.place(relx=0.7,rely=0.8375,relwidth=0.1,relheight=0.05)
po17=tk.Label(currentroster,text=roster[2][16])
po17.place(relx=0.7,rely=0.8875,relwidth=0.1,relheight=0.05)
po18=tk.Label(currentroster,text=roster[2][17])
po18.place(relx=0.7,rely=0.9375,relwidth=0.1,relheight=0.05)
hideEmpty()
#buttons for picking players
p1=tk.Button(pickframe, text=topten[0], command = lambda: changePlayer(0))
p1.place(relx=0,rely=0,relwidth=1,relheight=0.1)
p2=tk.Button(pickframe, text=topten[1], command = lambda: changePlayer(1))
p2.place(relx=0,rely=0.1,relwidth=1,relheight=0.1)
p3=tk.Button(pickframe, text=topten[2], command = lambda: changePlayer(2))
p3.place(relx=0,rely=0.2,relwidth=1,relheight=0.1)
p4=tk.Button(pickframe, text=topten[3], command = lambda: changePlayer(3))
p4.place(relx=0,rely=0.3,relwidth=1,relheight=0.1)
p5=tk.Button(pickframe, text=topten[4], command = lambda: changePlayer(4))
p5.place(relx=0,rely=0.4,relwidth=1,relheight=0.1)
p6=tk.Button(pickframe, text=topten[5], command = lambda: changePlayer(5))
p6.place(relx=0,rely=0.5,relwidth=1,relheight=0.1)
p7=tk.Button(pickframe, text=topten[6], command = lambda: changePlayer(6))
p7.place(relx=0,rely=0.6,relwidth=1,relheight=0.1)
p8=tk.Button(pickframe, text=topten[7], command = lambda: changePlayer(7))
p8.place(relx=0,rely=0.7,relwidth=1,relheight=0.1)
p9=tk.Button(pickframe, text=topten[8], command = lambda: changePlayer(8))
p9.place(relx=0,rely=0.8,relwidth=1,relheight=0.1)
p10=tk.Button(pickframe, text=topten[9], command = lambda: changePlayer(9))
p10.place(relx=0,rely=0.9,relwidth=1,relheight=0.1)
#position counter for roster
pg=tk.Label(infoframe,text='Point Guards on roster: '+str(0))
pg.place(relx=0.1,rely=0.025,relwidth=0.8,relheight=0.075)
sg=tk.Label(infoframe,text='Shooting Guards on roster: '+str(0))
sg.place(relx=0.1,rely=0.225,relwidth=0.8,relheight=0.075)
sf=tk.Label(infoframe,text='Small Forwards on roster: '+str(0))
sf.place(relx=0.1,rely=0.425,relwidth=0.8,relheight=0.075)
pf=tk.Label(infoframe,text='Power Forwards on roster: '+str(0))
pf.place(relx=0.1,rely=0.625,relwidth=0.8,relheight=0.075)
c=tk.Label(infoframe,text='Centers on roster: '+str(0))
c.place(relx=0.1,rely=0.825,relwidth=0.8,relheight=0.075)

pgo=tk.Label(infoframe,text='Average overall: '+str(0))
pgo.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.075)
sgo=tk.Label(infoframe,text='Average overall: '+str(0))
sgo.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.075)
sfo=tk.Label(infoframe,text='Average overall: '+str(0))
sfo.place(relx=0.1,rely=0.5,relwidth=0.8,relheight=0.075)
pfo=tk.Label(infoframe,text='Average overall: '+str(0))
pfo.place(relx=0.1,rely=0.7,relwidth=0.8,relheight=0.075)
co=tk.Label(infoframe,text='Average overall: '+str(0))
co.place(relx=0.1,rely=0.9,relwidth=0.8,relheight=0.075)

#search bar
sbar=tk.Entry(searchframe)
sbar.insert(0,'Search Player Name')
sbar.bind('<FocusIn>',on_entry_click)
sbar.bind('<FocusOut>',on_focusout)
sbar.config(fg='grey')
sbar.place(relx=0.1,rely=0.025,relwidth=0.8,relheight=0.2)
#position selector
nullselect=tk.StringVar(searchframe)
nullselect.set('Select a position')
positiondd=tk.OptionMenu(searchframe,nullselect,'Point Guard','Shooting Guard','Small Forward','Power Forward','Center')
positiondd.place(relx=0.1,rely=0.275,relwidth=0.8,relheight=0.2)
#search button
sbutton=tk.Button(searchframe,text='Search',command=lambda:Search())
sbutton.place(relx=0.1,rely=0.525,relwidth=0.8,relheight=0.2)
#clear button
clear=tk.Button(searchframe,text='Clear',command=lambda:clearSearch())
clear.place(relx=0.1,rely=0.775,relwidth=0.8,relheight=0.2)

#in progress temp page
inprogressframe=tk.Frame(canvas)

homebuttonz=tk.Button(inprogressframe,text='home',command=lambda:pregressHome())
homebuttonz.pack()
inprogresslabel=tk.Label(inprogressframe,text='Page in Progress')
inprogresslabel.pack()

root.mainloop()
"""
n.connect()

while run:
    time.sleep(0.5)
    data = n.send(createMessage(win[0],getColor()))
    message = readMessage(data)
    bg = message[1]
    win[0]=int(message[0])
    changeBackground(bg) 
    root.update()
"""