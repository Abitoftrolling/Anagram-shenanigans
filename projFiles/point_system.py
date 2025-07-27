#point_system.py
class PointSystem:
    def __init__(self):
        self.score = 0              #starts w/ 0 pts
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
    
    def get_score(self):
        return self.score              #gets current score

