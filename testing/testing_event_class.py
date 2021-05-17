from arrays import ArrayExpanded
from event import Event
import unittest
from API_requests import Requests
from unittest import TestCase


class TestEvent(TestCase):
    @staticmethod
    def get_event():
        events_json = Requests.get_events_by_team_id("2177")
        for event in events_json:
            return event

    def setUp(self) -> None:
        self.team_id = "2177"
        self.event = self.get_event()
        self.scheme = "4 - 2 - 3 - 1"
        self.shots = "6"
        self.ball_posession = 50
        self.fouls = "23"
        self.result = "draw"

    def test_get_scheme(self):
        self.assertEqual(Event(self.event).get_scheme(self.team_id), self.scheme)

    def test_get_shots(self):
        self.assertEqual(Event(self.event).get_shots(self.team_id), self.shots)

    def test_get_ball_posession(self):
        self.assertEqual(Event(self.event).get_ball_possesion(self.team_id), self.ball_posession)

    def test_fouls(self):
        self.assertEqual(Event(self.event).get_fouls(self.team_id), self.fouls)

    def test_get_result(self):
        self.assertEqual(Event(self.event).get_result(self.team_id), self.result)
