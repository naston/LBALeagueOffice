import tkinter as tk            
from tkinter import font as tkfont 
from DraftPage import *
from WIPPage import *
from MainPage import *
from ResultsPage import *
from StandingsPage import *
from NewSeasonPage import *
import NewSeason
import time

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, Draft, WIP, Home, Results, Standings, CreatingNew, CreatedNew):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        draftbutton = tk.Button(self, text="Go to Draft Test",
                            command=lambda: controller.show_frame("Draft"))
        testbutton = tk.Button(self, text="Go to WIP Test",
                            command=lambda: controller.show_frame("WIP"))
        homebutton = tk.Button(self, text="Go to Home Test",
                            command=lambda: controller.show_frame("Home"))
        resultsbutton = tk.Button(self, text="Go to Results Test",
                            command=lambda: controller.show_frame("Results"))
        standingsbutton = tk.Button(self, text="Go to Standings Test",
                            command=lambda: controller.show_frame("Standings"))
        newbutton = tk.Button(self, text="Go to New Season Test",
                            command=lambda: self.newSeason())
        button1.pack()
        button2.pack()
        draftbutton.pack()
        testbutton.pack()
        homebutton.pack()
        resultsbutton.pack()
        standingsbutton.pack()
        newbutton.pack()


    def newSeason(self):
        #this page doesn't show rn
        self.controller.show_frame('CreatingNew')
        time.sleep(1)
        NewSeason.run()
        time.sleep(2)
        self.controller.show_frame('CreatedNew')

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.wm_geometry("1200x1200")
    app.mainloop()


"""
To Do:
-implement bracket creation based upon standings
-have current standings and add results switch to bracket mode when bracket is created
-have create season swap to create bracket when season is completed
-have create bracket swap to perform lottery when bracket is completed
-make the lottery page
"""