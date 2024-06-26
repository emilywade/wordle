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
    
    def make_guess(self):
        """
        Function to ask the user to make a guess, decrease the guesses allowed, and return the guess.
        """
        while True:
            guess = input("Enter your guess: ")
            if len(guess) != self.length:
                print(f"Invalid guess. Please enter a {self.length}-letter word.")
            elif guess in self.guesses:
                print(f"You've already guessed '{guess}'. Try a different word.")
            else:
                self.guesses_allowed -= 1
                self.guesses_used += 1
                self.guesses.append(guess)
                return guess


def validate_choice(choice, valid_options):
    """
    Check whether the user's input is within a specified list of valid options.
    """
    return choice in valid_options

def get_valid_input(prompt, valid_options, error_message):
    """
    Repeatedly prompt the user for input until a valid choice is made.
    Uses the validate_choice() function to check for validity. 
    """
    while True:
        try:
            user_input = int(input(prompt))
            if validate_choice(user_input, valid_options):
                return user_input
            else:
                print(error_message)
        except ValueError:
            print("Invalid input. Please enter a number.")

def game_setup():
    """
    Setting up the initial game. 
    """
    print("Welcome to Wordle!\n")
    player_name = input("What is your name?\n")
    print(f"Thanks for playing, {player_name}")
    print("INSTRUCTIONS OF GAME PLAY TO GO HERE") 

    length_options = [4, 5, 6]
    length_prompt = "How many letters long would you like your random word to contain? You can choose 4, 5, or 6.\n"
    length_error_message = "Invalid choice. Please choose 4, 5, or 6."
    length = get_valid_input(length_prompt, length_options, length_error_message)
    print(f"You have chosen {length}-letter words.\n")

    guesses_allowed_options = [4, 6, 8]
    guesses_prompt = "How many guesses would you like to have? You can choose 4, 6, or 8.\n"
    guesses_error_message = "Invalid choice. Please choose 4, 6, or 8."
    guesses_allowed = get_valid_input(guesses_prompt, guesses_allowed_options, guesses_error_message)
    print(f"You have chosen to have no more than {guesses_allowed} guesses.\n")

    return player_name, length, guesses_allowed


def main():
    """
    Main game play function.
    """
    player_name, length, guesses_allowed = game_setup()
    board = Board(length, guesses_allowed)
    chosen_word = board.generate_random_word()
    board.print_board()

    while board.guesses_allowed > 0:
        guess = board.make_guess()
        if guess:
            print(f"You guessed: {guess}")
            print(f"Guesses remaining: {board.guesses_allowed}")
            if guess == chosen_word:
                print("Congratulations! You guessed the word correctly!")
                break
    else:
        print(f"Game over! The correct word was: {chosen_word}")

main()