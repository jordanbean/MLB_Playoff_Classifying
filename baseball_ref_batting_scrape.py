# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 14:28:38 2018

@author: jbean
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

df_batting = pd.DataFrame(columns=['team', 'batters_used','batter_age','games','runs','hits','doubles','triples','homeruns',
                                   'rbi','stolen_base','walks','strikeouts','batting_average','on_base_percentage','slugging',
                                   'ops','ops_plus','total_bases','left_on_base','year'])

for i in range(1969, 2019):
    
    site = requests.get('https://www.baseball-reference.com/leagues/MLB/{}.shtml'.format(i))

    soup = BeautifulSoup(site.text, 'html.parser')

    def get_attribute(class_side, data_stat):
    
        all_instances = soup.find_all('td', attrs={'class':class_side, 'data-stat':data_stat})
        all_instances = [i.text for i in all_instances][:-2] # Eliminate league total and average after extracting text

        return all_instances

    team = soup.find_all('th', attrs={'data-stat':'team_ID'})
    team = [i.text for i in team][1:-3]

    batters_used = get_attribute('right','batters_used')
    batter_age = get_attribute('right','age_bat')
    games = get_attribute('right','G')
    runs = get_attribute('right','R')
    hits = get_attribute('right','H')
    doubles = get_attribute('left','2B')
    triples = get_attribute('left','3B')
    homeruns = get_attribute('right','HR')
    rbi = get_attribute('right','RBI')
    stolen_base = get_attribute('right','SB')
    walks = get_attribute('right','BB')
    strikeouts = get_attribute('right','SO')
    batting_average = get_attribute('right','batting_avg')
    on_base_percentage = get_attribute('right','onbase_perc')
    slugging = get_attribute('right','slugging_perc')
    ops = get_attribute('right','onbase_plus_slugging')
    ops_plus = get_attribute('right','onbase_plus_slugging_plus')
    total_bases = get_attribute('right','TB')
    left_on_base = get_attribute('right','LOB')

    df = pd.DataFrame({'team':team, 'batters_used':batters_used, 'batter_age':batter_age, 'games':games, 'runs':runs, 'hits':hits, 'doubles':doubles,
                   'triples':triples, 'homeruns':homeruns, 'rbi':rbi, 'stolen_base':stolen_base, 'walks':walks, 'strikeouts':strikeouts,
                   'batting_average':batting_average,'on_base_percentage':on_base_percentage, 'slugging':slugging, 'ops':ops,
                   'ops_plus':ops_plus, 'total_bases':total_bases, 'left_on_base':left_on_base})
    df['year'] = i
    
    df_batting = df_batting.append(df)
    
    time.sleep(3)
    
df_batting.to_csv(r'C:\Users\jbean\Dropbox\Other\Python\Baseball_2018\batting_stats.csv')