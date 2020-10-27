import tkinter as tk
import NewSeason

class CreatingNew(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.creating= tk.Label(self,text='Creating a new season...')
        self.creating.place(relx=0.2,rely=0.3,relwidth=0.6,relheight=0.4)

class CreatedNew(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.creating= tk.Label(self,text='New Season Created')
        self.creating.place(relx=0.2,rely=0.3,relwidth=0.6,relheight=0.4)