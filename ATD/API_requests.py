import requests


class Requests:
    APIkey = '3f561cce229d17fa05f23e5fa9f1ce750c39652d1aa8fed1ae58464da66706a4'

    @staticmethod
    def get_teams_by_league_id(league_id):
        request_url = f'https://apiv2.apifootball.com/?action=get_teams&league_id={league_id}&APIkey={Requests.APIkey}'
        response = requests.get(request_url)

        return response.json()

    @staticmethod
    def get_events_by_team_id(team_id):
        request_url = f'https://apiv2.apifootball.com/?action=get_events&from=2015-01-01&to=2019-12-31&team_id={team_id}&APIkey={Requests.APIkey}'
        response = requests.get(request_url)

        return response.json()
