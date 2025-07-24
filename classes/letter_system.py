import random 

#function to load words from a text file 
def load_words():
    words = [] #empty list to store words 
    with open("classes/words.text", "r") as file: #opens words.txt file in classes folder
        for f in file: #reads each line in the file 
            word = f.strip() #removes any extra spaces or newline chars 
            if 3 <= len(word) <= 8: #keeps words between 3 and 8 letters long
                words.append(word) #adds the words to list
    return words

#functon to pick a random word and shuffle its letters 
def get_letters(words):
    word = random.choice(words) #picks the random word from list
    letters = list(word)  #converts word into a list of letters
    random.shuffle(letters)  #shuffles the letters randomly
    return letters, word  #returns the shuffles letters and the og word 