'''
In this module you can get info about events of your team from 2016 year.
'''
import requests
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy


APIkey = '3f561cce229d17fa05f23e5fa9f1ce750c39652d1aa8fed1ae58464da66706a4'


def inputTeam():
    """
    Function reads API
    """
    teams = {}
    teams_names = []
    league_id = 149  # Championship id in our API
    print('Downloading the info about teams...')

    request_url = f'https://apiv2.apifootball.com/?action=get_teams&league_id={league_id}&APIkey={APIkey}'
    response = requests.get(request_url)
    teams_info = response.json()

    for team in teams_info:
        teams[team['team_name']] = team['team_key']
    for team in teams_info:
        teams_names.append(team['team_name'])

    for i in range(len(teams_names)):
        print(f'{i+1}. {teams_names[i]}')

    chosen_team = input('Choose the team which standing you want to see: ')
    while chosen_team not in teams_names:
        for i in range(len(teams_names)):
            print(f'{i+1}. {teams_names[i]}')

        print('You typed a wrong team, try one more time...')
        chosen_team = input('Choose the team which standing you want to see: ')

    return teams[chosen_team]


def get_last_events(team_id: str):
    """
    Function gets events from API
    """
    print('Getting last events about your team...')

    request_url = f'https://apiv2.apifootball.com/?action=get_events&from=2015-01-01&to=2019-12-31&team_id={team_id}&APIkey={APIkey}'
    response = requests.get(request_url)
    events = response.json()

    return events


def save_events_to_csv(events: object, team_id: str):
    """
    Function saves data from to csv file. 
    """
    for event in events:
        if event['match_hometeam_id'] == team_id:
            if event['match_hometeam_score'] > event['match_awayteam_score']:
                event['result'] = 'win'
            elif event['match_hometeam_score'] == event['match_awayteam_score']:
                event['result'] = 'draw'
            else:
                event['result'] = 'lose'

            event['scheme'] = event['match_hometeam_system']
        else:
            if event['match_hometeam_score'] > event['match_awayteam_score']:
                event['result'] = 'lose'
            elif event['match_hometeam_score'] == event['match_awayteam_score']:
                event['result'] = 'draw'
            else:
                event['result'] = 'win'

            event['scheme'] = event['match_awayteam_system']

    with open('events.csv', 'w',) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['match_id', 'date',
                         'result', 'scheme'])
        for event in events:
            writer.writerow([event['match_id'], event['match_date'],
                             event['result'], event['scheme']])


def analyze_schemas():
    """
    Function reads events.csv file and groups it by schemes
    that were used for games
    """
    df = pd.read_csv('events.csv')
    df.dropna(subset=['scheme'], how='all', inplace=True)
    shemes_set = df['scheme'].unique().tolist()
    dict_of_shemes = {}
    for sheme in shemes_set:
        win_match, lose_match, draw_match = 0, 0, 0
        win_match = len(df[(df['result'] == 'win') & (df['scheme'] == sheme)])
        lose_match = len(df[(df['result'] == 'lose') & (df['scheme'] == sheme)])
        draw_match = len(df[(df['result'] == 'draw') & (df['scheme'] == sheme)])
        dict_of_shemes[sheme] = (win_match, lose_match, draw_match)
    
    return dict_of_shemes

def visualize_shemas(schemes):
    """
    Function visualzies schemes of the games and builds a chart
    based on this information
    """
    labels1, win_count, lose_count, draw_count = [], [], [], []
    for key, value in schemes.items():
        labels1.append(key)
        win_count.append(value[0])
        lose_count.append(value[1])
        draw_count.append(value[2])
    
    win_count = numpy.array(win_count)
    lose_count = numpy.array(lose_count)
    draw_count = numpy.array(draw_count)
    
    _, ax = plt.subplots()

    ax.bar(labels1, lose_count, 0.5, label='Count of lose shemes')
    ax.bar(labels1, draw_count, 0.5, label='Count of draw shemes', bottom = lose_count)
    ax.bar(labels1, win_count, 0.5, label='Count of win schemes', bottom = lose_count + draw_count)

    ax.set_ylabel('Number of games')
    ax.set_title("Analysis of shemes' efficiency")
    ax.legend()

    plt.show()



if __name__ == '__main__':
    team_id = inputTeam()
    events = get_last_events(team_id)
    save_events_to_csv(events, team_id)
    tuple_n = analyze_schemas()
    visualize_shemas(tuple_n)