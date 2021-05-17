"""
This module contains requests from API-s.
"""

import requests


class Requests:
    """
    This is requests class.
    """
    APIkey = '3f561cce229d17fa05f23e5fa9f1ce750c39652d1aa8fed1ae58464da66706a4'

    @staticmethod
    def get_available_leagues():
        """
        This method returns list of available leagues.
        """
        request_url = f'https://apiv2.apifootball.com/?action=get_leagues&APIkey={Requests.APIkey}'
        response = requests.get(request_url)

        return response.json()

    @staticmethod
    def get_teams_by_league_id(league_id):
        """
        This method returns team by its ID number.
        """
        request_url = f'https://apiv2.apifootball.com/?action=get_teams&league_id={league_id}&APIkey={Requests.APIkey}'
        response = requests.get(request_url)

        return response.json()

    @staticmethod
    def get_events_by_team_id(team_id, start_date, end_date):
        request_url = f'https://apiv2.apifootball.com/?action=get_events&from={start_date}&to={end_date}&team_id={team_id}&APIkey={Requests.APIkey}'
        print(request_url)
        response = requests.get(request_url)

        return response.json()
