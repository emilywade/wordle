"""
Wordle game
Guess the 5 letter word!
"""

import random

class Board:
    """
    Board class which initialises game play.
    Sets the length of the word, number of guesses allowed, number of guesses used
    so far, and the list of guesses taken.
    Stores the method for creating the board. 
    """
    def __init__(self, length, guesses_allowed):
        self.length = length
        self.guesses_allowed = guesses_allowed
        self.board = ["_" for x in range(length)]
        self.guesses_used = 0
        self.guesses = []

    def print_board(self):
        print(" ".join(self.board))



def generate_random_word(length):
    """
    Function to generate a random word of given length.
    Word selected from list provided words_list.txt (ref: https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt)
    """
    with open("words_list.txt") as f:
        all_words = f.read().splitlines()
        return random.choice([i for i in all_words if len(i) == length])

word = generate_random_word(5)
# print(word)


initial = Board(6, 5).print_board()