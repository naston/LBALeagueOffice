import tkinter as tk
import threading
topten=['empty']
HEIGHT=750
WIDTH=1200
def setList(templist):
    topten.clear()
    i=0
    while i<10:
        topten.append(templist[i])
        i+=1

def draft():
    #def setList(topten):
    #    p1['text']=topten[0]

    def setter():
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

    root = tk.Tk()
    root.title('LBA Draft')

    canvas= tk.Canvas(root,height=HEIGHT,width=WIDTH)
    canvas.pack()

    draftframe=tk.Frame(canvas,bg='black')
    draftframe.place(relx=0,rely=0,relwidth=1,relheight=1)

    nextteam=tk.Frame(draftframe,bg='white')
    nextteam.place(relx=0,rely=0.8,relwidth=0.2,relheight=0.2)
    draftboard=tk.Frame(draftframe,bg='yellow')
    draftboard.place(relx=0.6,rely=0.2,relwidth=0.4,relheight=0.8)
    currentteam=tk.Frame(draftframe,bg='orange')
    currentteam.place(relx=0,rely=0,relwidth=1,relheight=0.2)
    displayframe=tk.Frame(draftframe,bg='green')
    displayframe.place(relx=0,rely=0.2,relwidth=0.6,relheight=0.6)
    rostercomp=tk.Frame(draftframe,bg='blue')
    rostercomp.place(relx=0.2,rely=0.8,relwidth=0.4,relheight=0.2)

    ondeck=tk.Label(nextteam,text='Next Team')
    ondeck.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

    picking=tk.Label(currentteam,text='Pick #: Current Team')
    picking.place(relx=0.3,rely=0.1,relwidth=0.6,relheight=0.8)

    p1=tk.Label(draftboard)
    p1.place(relx=0,rely=0,relwidth=1,relheight=0.1)
    p2=tk.Label(draftboard)
    p2.place(relx=0,rely=0.1,relwidth=1,relheight=0.1)
    p3=tk.Label(draftboard)
    p3.place(relx=0,rely=0.2,relwidth=1,relheight=0.1)
    p4=tk.Label(draftboard)
    p4.place(relx=0,rely=0.3,relwidth=1,relheight=0.1)
    p5=tk.Label(draftboard)
    p5.place(relx=0,rely=0.4,relwidth=1,relheight=0.1)
    p6=tk.Label(draftboard)
    p6.place(relx=0,rely=0.5,relwidth=1,relheight=0.1)
    p7=tk.Label(draftboard)
    p7.place(relx=0,rely=0.6,relwidth=1,relheight=0.1)
    p8=tk.Label(draftboard)
    p8.place(relx=0,rely=0.7,relwidth=1,relheight=0.1)
    p9=tk.Label(draftboard)
    p9.place(relx=0,rely=0.8,relwidth=1,relheight=0.1)
    p10=tk.Label(draftboard)
    p10.place(relx=0,rely=0.9,relwidth=1,relheight=0.1)

    pg=tk.Label(rostercomp,text='PG: '+str(0))
    pg.place(relx=0.075,rely=0.2,relwidth=0.25,relheight=0.2)
    sg=tk.Label(rostercomp,text='SG: '+str(0))
    sg.place(relx=0.075,rely=0.6,relwidth=0.25,relheight=0.2)
    sf=tk.Label(rostercomp,text='SF: '+str(0))
    sf.place(relx=0.375,rely=0.2,relwidth=0.25,relheight=0.2)
    pf=tk.Label(rostercomp,text='PF: '+str(0))
    pf.place(relx=0.375,rely=0.6,relwidth=0.25,relheight=0.2)
    c=tk.Label(rostercomp,text='C: '+str(0))
    c.place(relx=0.675,rely=0.4,relwidth=0.25,relheight=0.2)

    while len(topten)>0:
        threading.Timer(15.0,setter).start()
        
    root.mainloop()

    

#need to include free agency