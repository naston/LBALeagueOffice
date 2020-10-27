import tkinter as tk

class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        self.homepage=tk.Frame(self)
        self.homepage.place(relx=0,rely=0,relwidth=1,relheight=1)
        #home frames
        self.buttonLeft=tk.Frame(self.homepage,bg='black')
        self.buttonLeft.place(relx=0,rely=0.25,relwidth=0.5,relheight=0.5)
        self.buttonRight=tk.Frame(self.homepage,bg='black')
        self.buttonRight.place(relx=0.5,rely=0.25,relwidth=0.5,relheight=0.5)
        self.titleFrame=tk.Frame(self.homepage,bg='black')
        self.titleFrame.place(relx=0,rely=0,relwidth=1,relheight=0.25)
        self.version=tk.Frame(self.homepage,bg='black')
        self.version.place(relx=0,rely=.75,relwidth=1,relheight=.25)
        #left side home buttons
        self.addResults=tk.Button(self.buttonLeft,text='Add Results',font=('Courier',20),command=lambda:controller.show_frame("Results"))
        self.addResults.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.2)
        self.createSeason=tk.Button(self.buttonLeft,text='Create Season',font=('Courier',20),command=lambda:controller.show_frame("WIP"))
        self.createSeason.place(relx=0.1,rely=0.30,relwidth=0.8,relheight=0.2)
        self.createBracket=tk.Button(self.buttonLeft,text='Create Bracket',font=('Courier',20),command=lambda:controller.show_frame("WIP"))
        self.createBracket.place(relx=0.1,rely=0.55,relwidth=0.8,relheight=0.2)
        self.currentStandings=tk.Button(self.buttonLeft,text='Current Standings',font=('Courier',20),command=lambda:controller.show_frame("WIP"))
        self.currentStandings.place(relx=0.1,rely=0.8,relwidth=0.8,relheight=0.2)
        #right side home buttons
        self.draft=tk.Button(self.buttonRight,text='Draft',command=lambda:controller.show_frame("Draft"),font=('Courier',20))
        self.draft.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.2)
        self.lottery=tk.Button(self.buttonRight,text='Pick Lottery',command=lambda:controller.show_frame("WIP"),font=('Courier',20))
        self.lottery.place(relx=0.1,rely=0.30,relwidth=0.8,relheight=0.2)
        self.trade=tk.Button(self.buttonRight,text='Trade',font=('Courier',20),command=lambda:controller.show_frame("WIP"))
        self.trade.place(relx=0.1,rely=0.55,relwidth=0.8,relheight=0.2)
        self.messagecenter=tk.Button(self.buttonRight,text='Message Center',font=('Courier',20),command=lambda:controller.show_frame("WIP"))
        self.messagecenter.place(relx=0.1,rely=0.8,relwidth=0.8,relheight=0.2)
        #title label
        self.title=tk.Label(self.titleFrame,text='LBA GM Room',font=('Courier',44),fg='white',bg='black')
        self.title.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.9)