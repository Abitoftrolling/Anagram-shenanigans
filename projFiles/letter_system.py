import random
from projFiles.anagram_solver import find_anagrams

#function to load words from a text file 
def load_words():
    words = [] #empty list to store words 
    with open("projFiles/words.txt", "r") as file: #opens words.txt file in proj files folder
        for f in file: #reads each line in the file 
            word = f.strip() #rm any whitespace/newlines
            if 3 <= len(word) <= 8: #keeps words between 3 and 8 letters long
                words.append(word) #adds the words to list
    return words

#functon to pick a random word and shuffle its letters 
def get_letters(word):
    letters = list(word)  #converts word into a list of letters
    random.shuffle(letters)  #shuffles the letters randomly
    return letters, word  #returns the shuffles letters and the og word 

def get_valid_anagrams(word_list, min_anagrams=10):
    while True:
        word = random.choice(word_list)
        anagrams = find_anagrams(word, word_list)
        if len(anagrams) >= min_anagrams:
            return word, anagrams
