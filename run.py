"""
Wordle game
Guess the 5 letter word!
"""

import random

def generate_random_word(length):
    """
    Function to generate a random word of given length.
    Word selected from list provided words_list.txt (ref: https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt)
    """
    with open("words_list.txt") as f:
        all_words = f.read().splitlines()
        return random.choice([i for i in all_words if len(i) == length])

word = generate_random_word(5)
print(word)