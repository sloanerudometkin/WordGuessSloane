"""
WordGuess game implementation.

@author xt0fer
@version 1.0.0
@date 5/27/21 11:02 AM
"""
import random

from person import Person

class WordGuess():
    def __init__(self):
        self.secret_word = "HELLO"
        self.guessed_letters = ["H", "O",] #temp guesses to test display
        self.max_attempts = 6
        self.wrong_guesses = 0

    def display_word(self):
        display = []

        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display.append(letter)
            else:
                display.append("_")

        return " ".join(display)


    def display_game(self):

        print("Word: ", self.display_word())
        print("Guessed letters: ", self.guessed_letters)
        print("Wrong guesses: ", self.wrong_guesses)

    def play(self):
        print("Welcome to Word Guess!")
        print()

        self.display_game()

    # while True:
    #     guess = (input("Guess a word"))
    #     if guess == "q":
    #         break #to quit the game
    #     print(f"You guessed: {guess}")

def main():
    game = WordGuess()
    game.play()

if __name__ == "__main__":
    main()



