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
    def get_events_by_team_id(team_id):
        """
        This method returns events connected with team using team ID number.
        """
        request_url = f'https://apiv2.apifootball.com/?action=get_events&from=2015-01-01&to=2019-12-31&team_id={team_id}&APIkey={Requests.APIkey}'
        response = requests.get(request_url)

        return response.json()
