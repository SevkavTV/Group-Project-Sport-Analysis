from API_requests import Requests
from team import Team


class Analysis:
    APIkey = '3f561cce229d17fa05f23e5fa9f1ce750c39652d1aa8fed1ae58464da66706a4'

    def __init__(self):
        self.team = None

    def choose_team(self):
        teams = {}
        teams_names = []
        league_id = 149  # Championship id in our API
        print('Downloading the info about teams...')

        teams_info = Requests.get_teams_by_league_id(league_id)

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
            chosen_team = input(
                'Choose the team which standing you want to see: ')

        self.team = Team(teams[chosen_team])

    def analyze_team_schemas(self):
        if self.team:
            self.team.analyze_schemas()
        else:
            print("You haven't chosen a team yet.")


if __name__ == '__main__':
    analysis = Analysis()
    analysis.choose_team()
    analysis.analyze_team_schemas()
