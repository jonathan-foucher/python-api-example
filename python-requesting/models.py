import json


class Score:
    id: int
    game_title: str
    score: int

    def __init__(self, score: dict = None):
        if score:
            self.id = score['id']
            self.game_title = score['game_title']
            self.score = score['score']

    def __str__(self):
        return f'{self.game_title}: {self.score}'

    def __repr__(self):
        return f'{self.game_title}: {self.score}'

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class Player:
    id: int
    firstname: str
    lastname: str
    scores: list[Score] = []

    def __init__(self, player: dict = None):
        if player:
            self.id = player['id']
            self.firstname = player['firstname']
            self.lastname = player['lastname']
            self.scores = [Score(score) for score in player.get('scores')]

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def get_full_name(self) -> str:
        return f'{self.firstname} {self.lastname}'
