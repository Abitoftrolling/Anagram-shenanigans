#point_system.py
class PointSystem:
    def __init__(self):
        self.level = 1              #starts @ lvl 1
        self.score = 0              #starts w/ 0 pts
        self.score_target = 100     #subject to change, hm points needed for nxt lvl
        self.time_bonus = 10        #subject to change, time added for nxt lvl
        self.found_words = set()    #tracks words used 

    def calculate_points(self, word):
        points_given = 10           #gives 10 pts for each word
        return points_given
    
    def add_word(self, word):
        if word in self.found_words:          #if word was already used, gives NO pts
            return 0, False
        
        self.found_words.add(word)            #adds to words used iff not used already
        points = self.calculate_points(word)  #calculates hm pts its worth
        self.score += points                  #adds pts to total score
        return points, True
    
    def level_up(self):
        if self.score >= self.score_target:          #check if player score reach or pass goal
            self.level += 1                          #moves to next lvl
            self.score_target += 150                 #subject to change, increases score for next level
            self.found_words.clear()                 #clear previously found words so player can reuse words in nxt level if needed
            return True
        return False                                 #not enough player, cant level up

    def get_level(self):
        return self.level              #gets current level number
    
    def get_score(self):
        return self.score              #gets current score
    
    def get_target(self):
        return self.score_target       #gets hm pts needed to reach next level
    
    def get_time_bonus(self):
        return self.time_bonus         #gets hm extra time shoulf be given when leveling up
