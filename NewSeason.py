import pandas as pd
import numpy as np
import Scheduler

def run():
    Scheduler.run()
    records = pd.read_csv('Standings.csv')
    records['Wins'] = 0
    records['Losses'] = 0
    records.to_csv('Standings.csv',index=False)
    #run the lottery
