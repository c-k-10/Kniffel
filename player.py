import pygame

class Player:
    def __init__(self, scorecard, name:str, is_human:bool, ai_difficulty:str, is_finish, final_score):
        self.scorecard = scorecard
        self.name = name
        self.is_human = is_human
        self.ai_diffilculty = ai_difficulty
        self.is_finish = is_finish
        self.final_score = final_score

    def score_points_on_scorecard():
        pass

    def choose_dices():
        pass

    def reset():
        pass

    def sum_score(self):
        upper_section = sum(r.value for r in self.scorecard[:6])
        if upper_section >= 63:
            self.final_score = upper_section + 35
        else:
            self.final_score = upper_section
        
        lower_section = sum(r.value for r in self.scorecard[6:])

        self.final_score = self.final_score + lower_section

        

