'''
In this module you can get info about events of your team from 2016 year.
'''
import requests
import pandas as pd
import csv


APIkey = '3f561cce229d17fa05f23e5fa9f1ce750c39652d1aa8fed1ae58464da66706a4'


def inputTeam():
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
    print('Getting last events about your team...')

    request_url = f'https://apiv2.apifootball.com/?action=get_events&from=2015-01-01&to=2019-12-31&team_id={team_id}&APIkey={APIkey}'
    response = requests.get(request_url)
    events = response.json()

    return events


def save_events_to_csv(events: object, team_id: str):
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


if __name__ == '__main__':
    team_id = inputTeam()
    events = get_last_events(team_id)
    save_events_to_csv(events, team_id)
