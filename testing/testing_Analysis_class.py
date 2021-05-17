import unittest
from analysis import Analysis
from unittest import TestCase


class TestAnalysis(TestCase):

    def setUp(self) -> None:
        self.team_id = "2177"
        self.criterion_1 = "scheme"
        self.criterion_2 = "possesion"
        self.criterion_3 = "fouls"
        self.criterion_4 = "else"
        self.criterion_1_res = {'4 - 2 - 3 - 1': {'win': 55, 'lose': 19, 'draw': 19}, '4 - 4 - 2': {'win': 3, 'lose': 0, 'draw': 1}, '4 - 1 - 4 - 1': {'win': 0, 'lose': 0, 'draw': 1}}
        self.criterion_2_res = {'0-29': {'win': 0, 'lose': 0, 'draw': 0}, '30-39': {'win': 1, 'lose': 2, 'draw': 0}, '40-49': {'win': 8, 'lose': 5, 'draw': 6}, '50-59': {'win': 36, 'lose': 10, 'draw': 10}, '60-69': {'win': 13, 'lose': 4, 'draw': 2}, '70-100': {'win': 2, 'lose': 0, 'draw': 1}}
        self.criterion_3_res = {'23': {'win': 0, 'lose': 0, 'draw': 1}, '21': {'win': 0, 'lose': 1, 'draw': 0}, '24': {'win': 1, 'lose': 0, 'draw': 0}, '15': {'win': 3, 'lose': 1, 'draw': 1}, '18': {'win': 1, 'lose': 1, 'draw': 0}, '13': {'win': 1, 'lose': 1, 'draw': 0}, '9': {'win': 0, 'lose': 1, 'draw': 0}, '14': {'win': 1, 'lose': 0, 'draw': 1}, '22': {'win': 1, 'lose': 0, 'draw': 0}, '29': {'win': 1, 'lose': 0, 'draw': 0}, '16': {'win': 1, 'lose': 0, 'draw': 1}, '7': {'win': 0, 'lose': 1, 'draw': 0}, '11': {'win': 0, 'lose': 1, 'draw': 0}, '19': {'win': 1, 'lose': 1, 'draw': 0}, '17': {'win': 0, 'lose': 0, 'draw': 1}}
        self.criterion_4_res = {'6': {'win': 7, 'lose': 1, 'draw': 1}, '11': {'win': 2, 'lose': 0, 'draw': 1}, '4': {'win': 5, 'lose': 2, 'draw': 4}, '5': {'win': 9, 'lose': 2, 'draw': 0}, '10': {'win': 3, 'lose': 2, 'draw': 0}, '8': {'win': 4, 'lose': 0, 'draw': 2}, '0': {'win': 0, 'lose': 2, 'draw': 2}, '3': {'win': 7, 'lose': 1, 'draw': 3}, '7': {'win': 8, 'lose': 0, 'draw': 0}, '24': {'win': 1, 'lose': 0, 'draw': 0}, '13': {'win': 3, 'lose': 0, 'draw': 0}, '9': {'win': 4, 'lose': 1, 'draw': 1}, '2': {'win': 4, 'lose': 1, 'draw': 3}, '15': {'win': 1, 'lose': 2, 'draw': 0}, '12': {'win': 1, 'lose': 0, 'draw': 0}, '1': {'win': 1, 'lose': 7, 'draw': 2}}

    def test_get_info(self):
        self.assertEqual(Analysis(self.team_id).get_info(self.criterion_1), self.criterion_1_res)
        self.assertEqual(Analysis(self.team_id).get_info(self.criterion_2), self.criterion_2_res)
        self.assertEqual(Analysis(self.team_id).get_info(self.criterion_3), self.criterion_3_res)
        self.assertEqual(Analysis(self.team_id).get_info(self.criterion_4), self.criterion_4_res)

    def test_analyze_team_schemas(self):
        self.assertEqual(Analysis(self.team_id).analyze_team_schemas(), self.criterion_1_res)

    def test_analyze_team_ball_possesion(self):
        self.assertEqual(Analysis(self.team_id).analyze_team_ball_possesion(), self.criterion_2_res)

    def test_analyze_team_fouls(self):
        self.assertEqual(Analysis(self.team_id).analyze_team_fouls(), self.criterion_3_res)

    def test_analyze_team_shots(self):
        self.assertEqual(Analysis(self.team_id).analyze_team_shots(), self.criterion_4_res)
