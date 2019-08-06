import tkinter as tk 
test= 'black'
def changeColor():
    optimized_canvas['bg'] = 'blue'


root = tk.Tk()
root.title('LBA League Office')
buttonLeft=tk.Frame(root,bg='black')
buttonLeft.place(relx=0,rely=0.25,relwidth=0.5,relheight=0.5)

buttonRight=tk.Frame(root,bg='blue')
buttonRight.place(relx=0.5,rely=0.25,relwidth=0.5,relheight=0.5)

titleFrame=tk.Frame(root,bg='green')
titleFrame.place(relx=0,rely=0,relwidth=1,relheight=0.25)


addResults=tk.Button(buttonLeft,text='Add Results')
addResults.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.2)

createSeason=tk.Button(buttonLeft,text='Create Season')
createSeason.place(relx=0.1,rely=0.30,relwidth=0.8,relheight=0.2)

createBracket=tk.Button(buttonLeft,text='Create Bracket')
createBracket.place(relx=0.1,rely=0.55,relwidth=0.8,relheight=0.2)

currentStandings=tk.Button(buttonLeft,text='Current Standings')
currentStandings.place(relx=0.1,rely=0.8,relwidth=0.8,relheight=0.2)


draft=tk.Button(buttonRight,text='Draft',command=lambda:changeColor())
draft.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.2)

lottery=tk.Button(buttonRight,text='Pick Lottery')
lottery.place(relx=0.1,rely=0.30,relwidth=0.8,relheight=0.2)

trade=tk.Button(buttonRight,text='Trade')
trade.place(relx=0.1,rely=0.55,relwidth=0.8,relheight=0.2)



title=tk.Label(titleFrame,text='LBA GM Room')
title.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.9)


top = tk.Toplevel()
top.title('Optimized Map')
optimized_canvas = tk.Frame(top,bg='yellow')
optimized_canvas.place(relx=0.1,rely=0.1,relwidth=0.5,relheight=0.5)



root.mainloop() 

