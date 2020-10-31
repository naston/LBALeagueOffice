import pandas as pd
import numpy as np

def run():
    standings = pd.read_csv('Standings.csv')
    playoffs = standings.iloc[0:8]
    playoffs['Wins'] = 0
    playoffs['Losses'] = 0
    playoffs['Rank'] = 0
    for i in range(0,len(playoffs)):
        playoffs.iloc[i,'Rank'] = i+1
    mathcups = pd.DataFrame(columns=['Round', 'GameID', 'Team1', 'Team2','Win1','Win2'])
    for i in range(0,len(playoffs)/2):
        matchup = pd.Series(data=[1,i+1,playoffs['Team'].iloc[i],playoffs['Team'].iloc[len(playoffs)-i],0,0])
        mathcups=mathcups.append(matchup,ignore_index=True)
    matchup = pd.Series(data=[2,1,'TBD','TBD',0,0])
    mathcups=mathcups.append(matchup,ignore_index=True)
    matchup = pd.Series(data=[2,2,'TBD','TBD',0,0])
    mathcups=mathcups.append(matchup,ignore_index=True)
    matchup = pd.Series(data=[3,1,'TBD','TBD',0,0])
    mathcups=mathcups.append(matchup,ignore_index=True)
    playoffs.to_csv('Playoffs.csv',index=False)
    mathcups.to_csv('PlayoffSchedule.csv',index=False)

    #I can remove the playoffs df now I believe