#anagram_solver.py
from collections import Counter

def find_anagrams(og_word, word_list):    
    og_counter = Counter(og_word)     
    valid_anagrams = []

    for word in word_list:
        if len(word) < 3 or word == og_word:
            continue

        if Counter(word) <= og_counter:
            valid_anagrams.append(word)

    return valid_anagrams
