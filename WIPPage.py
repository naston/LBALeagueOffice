import tkinter as tk

class WIP(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        

        self.inprogressframe=tk.Frame(self)
        self.inprogressframe.place(relx=0,rely=0,relwidth=1,relheight=1)

        self.homebuttonz=tk.Button(self.inprogressframe,text='home',command=lambda:controller.show_frame("StartPage"))
        self.homebuttonz.pack()
        self.inprogresslabel=tk.Label(self.inprogressframe,text='Page in Progress')
        self.inprogresslabel.pack()