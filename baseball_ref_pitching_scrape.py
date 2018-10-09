# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 16:06:07 2018

@author: jbean
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

df_pitching = pd.DataFrame(columns=['team', 'pitchers_used','pitcher_age', 'innings_pitched','complete_game','hits','runs',
                                   'earned_runs','homeruns','walks','strikeouts','hbp','whip','hits_per_nine', 'hr_per_nine','walks_per_nine',
                                   'so_per_nine','so_walk','left_on_base'])

for i in range(1969, 2019):
    
    site = requests.get('https://www.baseball-reference.com/leagues/MLB/{}-standard-pitching.shtml'.format(i))

    soup = BeautifulSoup(site.text, 'html.parser')

    def get_attribute(data_stat):
    
        stats = soup.find_all('td', {'class':'right', 'data-stat':data_stat})
        stats = [i.text for i in stats][:-2] # Eliminate league total and average after extracting text

        return stats

    team = soup.find_all('th', attrs={'data-stat':'team_ID'})
    team = [i.text for i in team][1:-3]

    pitchers_used = get_attribute('pitchers_used')
    pitcher_age = get_attribute('age_pitch')
    innings_pitched = get_attribute('IP')
    complete_game = get_attribute('CG')
    hits = get_attribute('H')
    runs = get_attribute('R')
    earned_runs = get_attribute('ER')
    homeruns = get_attribute('HR')
    walks = get_attribute('BB')
    strikeouts = get_attribute('SO')
    hbp = get_attribute('HBP')
    whip = get_attribute('whip')
    hits_per_nine = get_attribute('hits_per_nine')
    hr_per_nine = get_attribute('home_runs_per_nine')
    walks_per_nine = get_attribute('bases_on_balls_per_nine')
    so_per_nine = get_attribute('strikeouts_per_nine')
    so_walk = get_attribute('strikeouts_per_base_on_balls')
    left_on_base = get_attribute('LOB')

    df = pd.DataFrame({'team':team, 'pitchers_used':pitchers_used, 'pitcher_age':pitcher_age, 'innings_pitched': innings_pitched,
                       'complete_game':complete_game, 'hits':hits, 'runs':runs, 'earned_runs':earned_runs, 'homeruns':homeruns, 
                       'walks':walks, 'strikeouts':strikeouts, 'hbp':hbp,'whip':whip, 'hits_per_nine':hits_per_nine, 'hr_per_nine':hr_per_nine, 
                       'walks_per_nine':walks_per_nine, 'so_per_nine':so_per_nine, 'so_walk':so_walk, 'left_on_base':left_on_base})
    df['year'] = i
    
    df_pitching = df_pitching.append(df)
    
    time.sleep(3)
    
df_pitching.to_csv(r'C:\Users\jbean\Dropbox\Other\Python\Baseball_2018\pitching_stats.csv', index=False)