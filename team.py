"""
This module contains ADT -> Team.
"""

from event import Event
from arrays import ArrayExpanded
from API_requests import Requests
import matplotlib.pyplot as plt
import numpy


class Team:
    """
    Team ADT
    The atribute of this class is team ID.
    """

    def __init__(self, team_id: str):
        self._team_id = team_id
        self._num_events = 0
        self._events = self.get_last_events()

    def get_last_events(self):
        """
        This method return all last eventes.
        """
        print('Getting last events about your team...')

        events_json = Requests.get_events_by_team_id(self._team_id)

        events_lst = ArrayExpanded(len(events_json))
        for event in events_json:
            events_lst.insert(self._num_events, Event(event))
            self._num_events += 1

        return events_lst

    def get_results_of_events(self):
        """
        This method returns result of the chosen event.
        """
        results = {"win": 0, "lose": 0, "draw": 0}

        for event in self._events:
            results[event.get_result(self._team_id)] += 1

        return results

    def get_schemas_info(self):
        """
        This method returns information about schemas which team uses.
        """
        schemes = {}
        for event in self._events:
            scheme = event.get_scheme(self._team_id)

            if len(scheme) > 0:
                if scheme not in schemes:
                    schemes[scheme] = {"win": 0, "lose": 0, "draw": 0}

                schemes[scheme][event.get_result(self._team_id)] += 1

        return schemes

    def get_ball_possesion_info(self):
        """
        This method returns teams ball possesion.
        """
        ball_possesion_info = {'0-29': {"win": 0, "lose": 0, "draw": 0},
                               '30-39': {"win": 0, "lose": 0, "draw": 0},
                               '40-49': {"win": 0, "lose": 0, "draw": 0},
                               '50-59': {"win": 0, "lose": 0, "draw": 0},
                               '60-69': {"win": 0, "lose": 0, "draw": 0},
                               '70-100': {"win": 0, "lose": 0, "draw": 0}}

        for event in self._events:
            ball_possesion = event.get_ball_possesion(self._team_id)

            if ball_possesion:
                if 0 <= ball_possesion < 30:
                    range_possesion = '0-29'
                elif 30 <= ball_possesion < 40:
                    range_possesion = '30-39'
                elif 40 <= ball_possesion < 49:
                    range_possesion = '40-49'
                elif 50 <= ball_possesion < 59:
                    range_possesion = '50-59'
                elif 60 <= ball_possesion < 69:
                    range_possesion = '60-69'
                else:
                    range_possesion = '70-100'

                ball_possesion_info[range_possesion][event.get_result(
                    self._team_id)] += 1

        return ball_possesion_info

    def get_fouls_info(self):
        """
        This method returns information about fouls in a game.
        """
        fouls_info = {}

        for event in self._events:
            fouls = event.get_fouls(self._team_id)

            if fouls:
                if fouls not in fouls_info:
                    fouls_info[fouls] = {"win": 0, "lose": 0, "draw": 0}

                fouls_info[fouls][event.get_result(
                    self._team_id)] += 1

        return fouls_info

    def get_shots_info(self):
        """
        This method retruns information about shots in the game.
        """
        shots_info = {}

        for event in self._events:
            shots = event.get_shots(self._team_id)

            if shots:
                if shots not in shots_info:
                    shots_info[shots] = {"win": 0, "lose": 0, "draw": 0}

                shots_info[shots][event.get_result(
                    self._team_id)] += 1

        return shots_info

    def analyze_schemas(self):
        """
        This method returns analysis of the schemas displayed in graphic.
        """
        schemes = self.get_schemas_info()

        labels1, win_count, lose_count, draw_count = [], [], [], []
        for key, value in schemes.items():
            labels1.append(key)
            win_count.append(value["win"])
            lose_count.append(value["lose"])
            draw_count.append(value["draw"])

        win_count = numpy.array(win_count)
        lose_count = numpy.array(lose_count)
        draw_count = numpy.array(draw_count)

        _, ax = plt.subplots()

        ax.bar(labels1, lose_count, 0.5, label='Count of lose shemes')
        ax.bar(labels1, draw_count, 0.5,
               label='Count of draw shemes', bottom=lose_count)
        ax.bar(labels1, win_count, 0.5, label='Count of win schemes',
               bottom=lose_count + draw_count)

        ax.set_ylabel('Number of games')
        ax.set_title("Analysis of shemes' efficiency")
        ax.legend()

        plt.show()
