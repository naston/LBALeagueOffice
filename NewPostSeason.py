import pandas as pd
import numpy as np

def run():
    standings = pd.read_csv('Standings.csv')
    playoffs = standings.iloc[0:8]
    
    matchups = pd.DataFrame(columns=['Round', 'Game', 'Team1', 'Team2','Win1','Win2','Rank1','Rank2'])
    for i in range(0,int(len(playoffs)/2)):
        matchup = pd.Series(data=[1,i+1,playoffs['Team'].iloc[i],playoffs['Team'].iloc[len(playoffs)-i-1],0,0,i+1,len(playoffs)-i], index=matchups.columns)
        matchups=matchups.append(matchup,ignore_index=True)

    matchup = pd.Series(data=[2,1,'TBD','TBD',0,0,0,0], index=matchups.columns)
    matchups=matchups.append(matchup,ignore_index=True)
    matchup = pd.Series(data=[2,2,'TBD','TBD',0,0,0,0], index=matchups.columns)
    matchups=matchups.append(matchup,ignore_index=True)
    matchup = pd.Series(data=[3,1,'TBD','TBD',0,0,0,0], index=matchups.columns)
    matchups=matchups.append(matchup,ignore_index=True)
    matchups.to_csv('PlayoffSchedule.csv',index=False)

    #I will need to hard code the game numbers but the functions work

run()