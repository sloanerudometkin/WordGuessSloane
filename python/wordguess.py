"""
WordGuess game implementation.

@author xt0fer
@version 1.0.0
@date 5/27/21 11:02 AM
"""
from person import Person

def play():
    print("Welcome to Word Guess!")
    while True:
        guess = (input("Guess a word"))
        if guess == "q":
            break #to quit the game
        print(f"You guessed: {guess}")

class WordGuess:
    def __init__(self, word):
        words = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
        index = random.randint(0, len(words)-1)
        self.word = words[index]
        self.guessed_letters = set()
        self.max_attempts = 6
        self.wrong_guesses = 0

    def display_word(self):
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + ""
            else:
                display += "_"
        return display.strip()
    
def make_guess(self, letter):
    letter = letter.upper()
    if len(letter) != 1 or not letter.isalpha():
        return "Please guess a single letter"
    if letter in self.guessed.letters
        return "You already guessed that letter"
    self.guessed_letters.add(letter)
    if letter in self.word:
        return f"Good guess! {letter} is in the word"
    else:
        self.wrong_guesses +- 1
        return f"Sorry, {letter} is not in the word"
    
def is_won(self):
    return all(letter in self.guessed_letters for letter in self.word)

def is_lost(self):
    return self.wrong_guesses >= self.max_attempts

def is_game_over(self):
    return self.is_won() or self.is_lot()

def get_game_status(self):
    status = f"Word: {self.display_word()}\n"
    status += f"Guessed: {', '.join(sorted(self.guessed_letters))}\n"
    status += f"Attempts remaining: {self.max_attempts - self.wrong_guesses}"
    return status
        
def main():
    game = WordGuess()
    game.play()

if __name__ == "__main__":
    main()
