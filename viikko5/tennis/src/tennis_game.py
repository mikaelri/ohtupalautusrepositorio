class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.score = ""
        self.score_dict = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def __str__(self):
        return f'{self.score_dict[self.player1_score]}-{self.score_dict[self.player2_score]}'

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):

        if self.player1_score == self.player2_score:
            if self.player1_score == 0:
                self.score = "Love-All"
            elif self.player1_score == 1:
                self.score  = "Fifteen-All"
            elif self.player1_score == 2:
                self.score  = "Thirty-All"
            else:
                self.score  = "Deuce"
        elif self.player1_score >= 4 or self.player2_score >= 4:
            minus_result = self.player1_score - self. player2_score

            if minus_result == 1:
                self.score  = "Advantage player1"
            elif minus_result == -1:
                self.score  = "Advantage player2"
            elif minus_result >= 2:
                self.score  = "Win for player1"
            else:
                self.score  = "Win for player2"
        else:
            for i in range(1, 3):
                if i == 1:
                    self.score = self.player1_score
                else:
                    self.score  = self.__str__()
                    temp_score = self.player2_score


        return self.score 