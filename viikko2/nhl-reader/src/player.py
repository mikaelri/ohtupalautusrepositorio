class Player:
    def __init__(self, name, team, goals, assists, nationality):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality

    def __str__(self):
        points = self.assists + self.goals
        return f"{self.name:20} {self.team}  {self.goals:3} +{self.assists:>3} = {points}"