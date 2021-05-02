class Event:
    def __init__(self, event_info: object):
        self.process_event_info(event_info)

    def process_event_info(self, event_info: object):
        self.event_id = event_info['match_id']

        self.hometeam_id = event_info['match_hometeam_id']
        self.hometeam_score = event_info['match_hometeam_score']

        self.awayteam_id = event_info['match_awayteam_id']
        self.awayteam_score = event_info['match_awayteam_score']

        self.hometeam_scheme = event_info['match_hometeam_system']
        self.awayteam_scheme = event_info['match_awayteam_system']

        self.stats = event_info['statistics']

    def get_scheme(self, team_id: str):
        if team_id == self.hometeam_id:
            return self.hometeam_scheme

        return self.awayteam_scheme

    def get_result(self, team_id: str):
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
