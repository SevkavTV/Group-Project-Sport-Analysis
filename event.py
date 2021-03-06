"""
This module contains class Event which will be used in Team ADT.
"""


class Event:
    """
    Event class.
    Class atribute is json file from API.
    """

    def __init__(self, event_info: object):
        self.process_event_info(event_info)

    def process_event_info(self, event_info: object):
        """
        This method creates self atributes for json file.
        """
        self.event_id = event_info['match_id']

        self.hometeam_id = event_info['match_hometeam_id']
        self.hometeam_score = event_info['match_hometeam_score']

        self.awayteam_id = event_info['match_awayteam_id']
        self.awayteam_score = event_info['match_awayteam_score']

        self.hometeam_scheme = event_info['match_hometeam_system']
        self.awayteam_scheme = event_info['match_awayteam_system']

        self.stats = event_info['statistics']

    def get_scheme(self, team_id: str):
        """
        This method returns scheme which team uses.
        """
        if team_id == self.hometeam_id:
            return self.hometeam_scheme

        return self.awayteam_scheme

    def get_ball_possesion(self, team_id: str):
        """
        This method returns ball possesion of the team.
        """
        for stat in self.stats:
            if stat['type'] == "Ball Possession":
                if team_id == self.hometeam_id:
                    return int(stat['home'][:-1])

                return int(stat['away'][:-1])

    def get_fouls(self, team_id: str):
        """
        This method returns team fouls.
        """
        for stat in self.stats:
            if stat['type'] == "Fouls":
                if team_id == self.hometeam_id:
                    return stat['home']

                return stat['away']

    def get_shots(self, team_id: str):
        """
        This method returns team shots.
        """
        for stat in self.stats:
            if stat['type'] == "Shots on Goal":
                if team_id == self.hometeam_id:
                    return stat['home']

                return stat['away']

    def get_result(self, team_id: str):
        """
        This method returns results of the mathch.
        """
        if team_id == self.hometeam_id:
            if self.hometeam_score > self.awayteam_score:
                return "win"

            if self.hometeam_score < self.awayteam_score:
                return "lose"

            return "draw"

        if self.hometeam_score > self.awayteam_score:
            return "lose"

        if self.hometeam_score < self.awayteam_score:
            return "win"

        return "draw"
