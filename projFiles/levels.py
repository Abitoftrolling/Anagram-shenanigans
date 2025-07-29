#levels.py

class LevelSystem:
    def __init__(self):
        self.level = 1                    #starts @ lvl 1
        self.score_target = 100           #subject to change, hm points needed for nxt lvl
        self.time_bonus = 10              #subject to change, time added for nxt lvl

    def should_level_up(self, current_score):
        return current_score >= self.score_target     #checks if player score reach or pass goal
    
    def level_up(self):
        self.level += 1                          #moves to next lvl
        self.score_target += 20                 #subject to change, increases score for next level
        return self.time_bonus
    
    def get_level(self):
        return self.level
    
    def get_score_target(self):
        return self.score_target
    
    def get_time_bonus(self):
        return self.time_bonus