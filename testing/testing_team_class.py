import unittest
from unittest import TestCase
from team import Team
from arrays import ArrayExpanded


class TestTeam(TestCase):

    def setUp(self) -> None:
        self.team_id = "2177"
        self.results_of_events = {'win': 65, 'lose': 23, 'draw': 23}
        self.schemas_info = {'4 - 2 - 3 - 1': {'win': 55, 'lose': 19, 'draw': 19}, '4 - 4 - 2': {'win': 3, 'lose': 0, 'draw': 1}, '4 - 1 - 4 - 1': {'win': 0, 'lose': 0, 'draw': 1}}
        self.ball_posession_info = {'0-29': {'win': 0, 'lose': 0, 'draw': 0}, '30-39': {'win': 1, 'lose': 2, 'draw': 0}, '40-49': {'win': 8, 'lose': 5, 'draw': 6}, '50-59': {'win': 36, 'lose': 10, 'draw': 10}, '60-69': {'win': 13, 'lose': 4, 'draw': 2}, '70-100': {'win': 2, 'lose': 0, 'draw': 1}}
        self.fouls_info = {'23': {'win': 0, 'lose': 0, 'draw': 1}, '21': {'win': 0, 'lose': 1, 'draw': 0}, '24': {'win': 1, 'lose': 0, 'draw': 0}, '15': {'win': 3, 'lose': 1, 'draw': 1}, '18': {'win': 1, 'lose': 1, 'draw': 0}, '13': {'win': 1, 'lose': 1, 'draw': 0}, '9': {'win': 0, 'lose': 1, 'draw': 0}, '14': {'win': 1, 'lose': 0, 'draw': 1}, '22': {'win': 1, 'lose': 0, 'draw': 0}, '29': {'win': 1, 'lose': 0, 'draw': 0}, '16': {'win': 1, 'lose': 0, 'draw': 1}, '7': {'win': 0, 'lose': 1, 'draw': 0}, '11': {'win': 0, 'lose': 1, 'draw': 0}, '19': {'win': 1, 'lose': 1, 'draw': 0}, '17': {'win': 0, 'lose': 0, 'draw': 1}}
        self.shots_info = {'6': {'win': 7, 'lose': 1, 'draw': 1}, '11': {'win': 2, 'lose': 0, 'draw': 1}, '4': {'win': 5, 'lose': 2, 'draw': 4}, '5': {'win': 9, 'lose': 2, 'draw': 0}, '10': {'win': 3, 'lose': 2, 'draw': 0}, '8': {'win': 4, 'lose': 0, 'draw': 2}, '0': {'win': 0, 'lose': 2, 'draw': 2}, '3': {'win': 7, 'lose': 1, 'draw': 3}, '7': {'win': 8, 'lose': 0, 'draw': 0}, '24': {'win': 1, 'lose': 0, 'draw': 0}, '13': {'win': 3, 'lose': 0, 'draw': 0}, '9': {'win': 4, 'lose': 1, 'draw': 1}, '2': {'win': 4, 'lose': 1, 'draw': 3}, '15': {'win': 1, 'lose': 2, 'draw': 0}, '12': {'win': 1, 'lose': 0, 'draw': 0}, '1': {'win': 1, 'lose': 7, 'draw': 2}}

    def test_last_events(self):
        self.assertIs(type(Team(self.team_id).get_last_events()), ArrayExpanded)

    def test_results_of_events(self):
        self.assertEqual(Team(self.team_id).get_results_of_events(), self.results_of_events)

    def test_get_schemas_info(self):
        self.assertEqual(Team(self.team_id).get_schemas_info(), self.schemas_info)

    def test_get_ball_posession_info(self):
        self.assertEqual(Team(self.team_id).get_ball_possesion_info(), self.ball_posession_info)

    def test_get_fouls_info(self):
        self.assertEqual(Team(self.team_id).get_fouls_info(), self.fouls_info)

    def test_get_shots_info(self):
        self.assertEqual(Team(self.team_id).get_shots_info(), self.shots_info)
