'''
In this module you can get info about standing in the season table of the team in EPL.
'''
import requests

APIkey = '3f561cce229d17fa05f23e5fa9f1ce750c39652d1aa8fed1ae58464da66706a4'


def inputTeam():
    teams = []
    league_id = 148  # EPL id in our API
    print('Downloading the info about teams...')

    request_url = f'https://apiv2.apifootball.com/?action=get_teams&league_id={league_id}&APIkey={APIkey}'
    response = requests.get(request_url)
    teams_info = response.json()

    for team in teams_info:
        teams.append(team['team_name'])

    for i in range(len(teams)):
        print(f'{i+1}. {teams[i]}')

    chosen_team = input('Choose the team which standing you want to see: ')
    while chosen_team not in teams:
        print('You typed a wrong team, try one more time...')
        for i in range(len(teams)):
            print(f'{i+1}. {teams[i]}')

        chosen_team = input('Choose the team which standing you want to see: ')

    return chosen_team


def showTeamStanding(team_name: str):
    league_id = 148
    print(f'Downloading the info about {team_name}...')

    request_url = f'https://apiv2.apifootball.com/?action=get_standings&league_id={league_id}&APIkey={APIkey}'
    response = requests.get(request_url)
    standings = response.json()

    for standing in standings:
        if team_name == standing['team_name']:
            print(
                f'{team_name} is on the {standing["overall_league_position"]} and has {standing["overall_league_W"]} wins, {standing["overall_league_D"]} draws, and {standing["overall_league_L"]} loses.')
            break


if __name__ == '__main__':
    team = inputTeam()
    showTeamStanding(team)
