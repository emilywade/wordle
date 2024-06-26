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
    Stores the method for creating the board and generating the random word. 
    """
    def __init__(self, length, guesses_allowed):
        self.length = int(length)
        self.guesses_allowed = int(guesses_allowed)
        self.board = ["_" for x in range(int(length))]
        self.guesses_used = 0
        self.guesses = []

    def print_board(self):
        print(" ".join(self.board))

    def generate_random_word(self):
        """
        Function to generate a random word of given length.
        Word selected from list provided words_list.txt (ref: https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt)
        """
        with open("words_list.txt") as f:
            all_words = f.read().splitlines()
            chosen_word = random.choice([i for i in all_words if len(i) == self.length])
            return chosen_word


# board = Board(6, 5)
# board.print_board()
# board.generate_random_word()

def game_setup():
    print("Welcome to Wordle!\n")
    player_name = input("What is your name?\n")
    print(f"Thanks for playing, {player_name}")
    print("INSTRUCTIONS OF GAME PLAY TO GO HERE")
    length = input("How many letters long would you like your random word to contain? You can choose 4, 5 or 6.")
    print(f"You have choosen {length} letter words.")
    guesses_allowed = input("How many guesses would you like to have? You can choose 4, 6 or 8.")
    print(f"You have choosen to have no more than {guesses_allowed} guesses.")
    return player_name, length, guesses_allowed

# game_setup()


def main():
    """
    Main game play function.
    """
    player_name, length, guesses_allowed = game_setup()
    board = Board(length, guesses_allowed)
    chosen_word = board.generate_random_word()
    board.print_board()

main()