from API_requests import Requests


def get_all_teams():
    all_teams = []

    available_leagues = Requests.get_available_leagues()
    for league in available_leagues:
        teams = Requests.get_teams_by_league_id(league['league_id'])

        for team in teams:
            all_teams.append(
                (team['team_name'], team['team_key'], team['team_badge']))

    return all_teams


def write_to_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in data:
            print(line[0])
            file.write(f'{line[0]}, {line[1]}, {line[2]}\n')


if __name__ == '__main__':
    write_to_file('all_teams.txt', get_all_teams())
