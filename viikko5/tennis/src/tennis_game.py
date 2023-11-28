class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.score = ""
        self.score_list =['Love', 'Fifteen', 'Thirty', 'Forty']
        
    def __str__(self):
        """returns the scorelist items in string format"""
        return f'{self.score_list[self.player1_score]}-{self.score_list[self.player2_score]}'

    def update_points(self, player_name):
        """update score if point won"""
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1
    
    def get_score(self):
        """checks the score for equal or point won"""
        if self.player1_score == self.player2_score:
            self.score = self.equal_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.won_point()
        else: 
            self.score = self.__str__()
        return self.score

    def equal_score(self):
        """checks for equal score"""
        if self.player1_score < 3:
            self.score = f'{self.score_list[self.player1_score]}-All'
        else: 
            self.score = "Deuce"
        return self.score
    
    def won_point(self):
        """checks for points won"""
        result_difference = self.player1_score - self.player2_score

        if result_difference == 1:
            return "Advantage player1"
        if result_difference == -1:
            return "Advantage player2"
        if result_difference >= 2:
            return "Win for player1"
        return "Win for player2"