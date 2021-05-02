from event import Event
from arrays import ArrayExpanded
from API_requests import Requests
import matplotlib.pyplot as plt
import numpy


class Team:
    def __init__(self, team_id: str):
        self._team_id = team_id
        self._num_events = 0
        self._events = self.get_last_events()

    def get_last_events(self):
        print('Getting last events about your team...')

        events_json = Requests.get_events_by_team_id(self._team_id)

        events_lst = ArrayExpanded(len(events_json))
        for event in events_json:
            events_lst.insert(self._num_events, Event(event))
            self._num_events += 1

        print(events_lst)
        return events_lst

    def get_results_of_events(self):
        results = {"win": 0, "lose": 0, "draw": 0}

        for event in self._events:
            results[event.get_result(self._team_id)] += 1

        return results

    def get_schemas_info(self):
        schemes = {}
        for event in self._events:
            scheme = event.get_scheme(self._team_id)

            if len(scheme) > 0:
                if scheme not in schemes:
                    schemes[scheme] = {"win": 0, "lose": 0, "draw": 0}

                schemes[scheme][event.get_result(self._team_id)] += 1

        return schemes

    def analyze_schemas(self):
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
