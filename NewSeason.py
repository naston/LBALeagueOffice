import pandas as pd
import numpy as np
import Scheduler

def run():
    Scheduler.run()
    records = pd.read_csv('Standings.csv')
    records['Wins'] = 0
    records['Losses'] = 0
    records.to_csv('Standings.csv',index=False)
    newWeek()
    #run the lottery

def newWeek():
    data = {
        'Week':0,
        'G1':[0],
        'G2':[0],
        'G3':[0]
    }
    """    ,
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
    """
    weekStatus = pd.DataFrame(data)
    weekStatus.to_csv('weekStatus.csv', index=False)