# game.py
from word_manager import get_base_word, shuffle_word
from word_manager import is_valid_anagram

class Game:
    def __init__(self):
        self.base_word = get_base_word()
        self.letter_pool = shuffle_word(self.base_word)
        self.current_input = ""
        self.points = 0
        self.found_words = set()

    def add_letter(self, letter):
        if letter not in self.letter_pool:
            return False, True  # Invalid letter not in pool
        if self.current_input.count(letter) < self.letter_pool.count(letter):
            self.current_input += letter
            return True, False  # Letter used successfully
        return False, False  # Valid letter, just overused

    def backspace(self):
        self.current_input = self.current_input[:-1]

    def submit_word(self):
        if is_valid_anagram(self.base_word, self.current_input):
            if self.current_input not in self.found_words:
                self.points += 1
                self.found_words.add(self.current_input)
        self.current_input = ""
