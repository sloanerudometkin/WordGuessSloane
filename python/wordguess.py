"""
WordGuess game implementation.

@author xt0fer
@version 1.0.0
@date 5/27/21 11:02 AM
"""


class WordGuess:
    def __init__(self):
    """WordGuess game class - ready for implementation."""
    pass

def play(self):
    print("Welcome to Word Guess!")
    while True:
        guess = (input("Guess a word"))
        if guess == "q":
            break #to quit the game
        print(f"You guessed: {guess}")
        

def main():
    game = WordGuess()
    game.play()

if __name__ == "__main__":
    main()
