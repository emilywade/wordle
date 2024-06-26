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
        self.valid_words = self.load_words()

    def print_board(self):
        print(" ".join(self.board))

    def load_words(self):
        """
        Load words from words_list.txt into a list.
        (doc taken from https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt)
        """
        with open("words_list.txt") as f:
            all_words = f.read().splitlines()
            valid_words = [i for i in all_words if len(i) == self.length]
            return valid_words

    def choose_random_word(self):
        """
        Randomly select a word from the load_words function
        """
        chosen_word = random.choice(self.valid_words)
        print(chosen_word)
        return chosen_word
    
    def make_guess(self, chosen_word):
        """
        Function to ask the user to make a guess, decrease the guesses allowed, increase 
        the guesses used and return the guess.
        Checks the guess has a valid length and hasn't been guessed before.
        """
        while True:
            guess = input("Enter your guess: ")
            if len(guess) != self.length:
                print(f"Invalid guess. Please enter a {self.length}-letter word.")
            elif guess in self.guesses:
                print(f"You've already guessed '{guess}'. Try a different word.")
            elif guess not in self.valid_words:
                print(f"'{guess}' is not a valid word. Try a different word.")
            else:
                self.guesses_allowed -= 1
                self.guesses_used += 1
                self.guesses.append(guess)
                self.give_feedback(guess, chosen_word)
                return guess
    
    def give_feedback(self, guess, chosen_word):
        """
        Provide feedback on the guessed word.
        """
        feedback = ["_" for _ in range(self.length)]
        chosen_word_copy = list(chosen_word)

        # check for correct letters in the correct place
        for i in range(self.length):
            if guess[i] == chosen_word[i]:
                feedback[i] = guess[i].upper()
                # marking letter as "used" so not used in next feedback step
                chosen_word_copy[i] = None

        # check for correct letters in the incorrect place
        for i in range(self.length):
            if guess[i] != chosen_word[i] and guess[i] in chosen_word_copy:
                feedback[i] = guess[i].lower()

        print("Feedback: " + " ".join(feedback))


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
    print(f"Thanks for playing, {player_name}\n")
    print("Guess the word! Simply enter your guess, review the feedback provided, and keep guessing!\n")
    print("You can choose how many letters long the word is, and how many guesses you're allowed.\n")
    print("After each guess you will be given some feedback to help you with your next guess.\n")
    print("A letter in lowercase means it is a correct letter but in the wrong place.\n")
    print("A letter in UPPERCASE means it is a correct letter in the correct place.\n") 

    length_options = [4, 5, 6]
    length_prompt = "How many letters long would you like your random word to contain? You can choose 4, 5, or 6.\n"
    length_error_message = "Invalid choice. Please choose 4, 5, or 6."
    length = get_valid_input(length_prompt, length_options, length_error_message)

    guesses_allowed_options = [4, 6, 8]
    guesses_prompt = "How many guesses would you like to have? You can choose 4, 6, or 8.\n"
    guesses_error_message = "Invalid choice. Please choose 4, 6, or 8."
    guesses_allowed = get_valid_input(guesses_prompt, guesses_allowed_options, guesses_error_message)
    print(f"Great! You will have {guesses_allowed} attempts to guess the {length}-letter word.\n")

    return player_name, length, guesses_allowed


def main():
    """
    Main game play function.
    """
    player_name, length, guesses_allowed = game_setup()
    board = Board(length, guesses_allowed)
    chosen_word = board.choose_random_word()
    board.print_board()

    while board.guesses_allowed > 0:
        guess = board.make_guess(chosen_word)
        if guess:
            print(f"You guessed: {guess}")
            print(f"Guesses remaining: {board.guesses_allowed}")
            if guess == chosen_word:
                print(f"Congratulations, {player_name}! You correctly guessed {chosen_word} with {guesses_allowed} guesses left!")
                break
    else:
        print(f"Sorry, {player_name}. Game over! The correct word was: {chosen_word}")

main()