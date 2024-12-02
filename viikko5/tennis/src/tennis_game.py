class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_score += 1
        else:
            self.p2_score += 1

    def equal(self,p1_score):
        if p1_score == 0:
            score = "Love-All"
        elif p1_score == 1:
            score = "Fifteen-All"
        elif p1_score == 2:
            score = "Thirty-All"
        else:
            score = "Deuce"
        return score

    def add_points(self,score):
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        elif score == 3:
            return "Forty"

    def get_score(self):
        score = ""
        max_points = 3
        if self.p1_score == self.p2_score:
            score = self.equal(self.p1_score)
        elif self.p1_score > max_points or self.p2_score > max_points:
            minus_result = self.p1_score - self. p2_score
            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            score = self.add_points(self.p1_score)
            score += "-"
            score += self.add_points(self.p2_score)
        return score