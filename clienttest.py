import tkinter as tk
from Network import Network
import time
from Message import testMessageOn
import pickle

run = True
n = Network()
global player
player=testMessageOn(n.getTeam(),'white',n.getTeam())
win=[]
win.append(int(n.getTeam()))

HEIGHT=500
WIDTH=500

def createMessage(pageType,bg):
    return str(pageType)+','+bg

def readMessage(message):
    #message = message.split(',')
    #unpickle and then set player equal to recieved player
    msg = pickle.loads(message)
    #player.setColor(message.getColor())
    #player.setPage(message.getPage())

    return msg

def changeWindow(pageType):
    if pageType == 0:
        wait.place_forget()
        frame.place(relx=0,rely=0,relwidth=1,relheight=1)

    else:
        frame.place_forget()
        wait.place(relx=0,rely=0,relwidth=1,relheight=1)

def getColor():
    return frame['bg']

def changeBackground(color):
    frame['bg']=color
    wait['bg']=color
    if player.getPage()==1:
        n.send(player)
    changeWindow(player.getPage())
    root.update()

def buttonPress(color):
    #win[0]=1
    player.setPage(1)
    player.setColor(color)
    changeBackground(color)

root=tk.Tk()

canvas=tk.Canvas(root,width=WIDTH,height=HEIGHT)
canvas.pack()

frame=tk.Frame(canvas,bg='white')
frame.place(relx=0,rely=0,relwidth=1,relheight=1)

green=tk.Button(frame,text='green',command=lambda:buttonPress('green'))
green.pack()

red=tk.Button(frame,text='red',command=lambda:buttonPress('red'))
red.pack()

blue=tk.Button(frame,text='blue',command=lambda:buttonPress('blue'))
blue.pack()

wait=tk.Frame(canvas)

root.update()

n.connect()

while run:
    #global player
    time.sleep(0.5)
    #data = n.send(createMessage(win[0],getColor()))
    data = n.send(player)
    message = readMessage(data)
    player=message
    #bg = message[1]
    bg = player.getColor()
    #win[0]=int(message[0])

    changeBackground(bg) 
    root.update()


