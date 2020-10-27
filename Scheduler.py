import pandas as pd
import numpy as np
import random

def run():
    schedule = pd.read_csv('Schedule.csv')
    max_week = schedule['Week'].max()
    schedule['Week'] = schedule.apply(offset_weeks, args=(max_week,), axis = 1)
    weeks = schedule['Week'].unique().tolist()
    schedule = setWeeks(schedule,weeks,max_week)
    schedule = schedule.sort_values(by=['Week'])
    schedule.to_csv('Schedule.csv', index=False)

def offset_weeks(row, offset):
    return row['Week']+offset

def setWeeks(df,week_list, max_week):
    for i in range(1, max_week+1):
        k = random.randint(0,len(week_list)-1)
        week = week_list[k]
        del week_list[k]
        df.loc[df['Week']==week, 'Week']=i
    return df