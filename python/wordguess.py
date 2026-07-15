"""
WordGuess game implementation.

@author xt0fer
@version 1.0.0
@date 5/27/21 11:02 AM
"""
from person import Person

class WordGuess():
    def __init__(self):
        self.player = Person()
        self.secret_word = "PERSON"
        self.guessed_letters = []
        self.max_attempts = 6
        self.wrong_guesses = 0

    def setup_player(self):
        print("\n--- Player Setup ---")
        first_name = input("Enter your first name")
        self.player.set_first_name(first_name)
        last_name = input("Enter your last name")
        self.player.set_last_name(last_name)

        while True:
            age_input = input("Enter your age: ").strip()
            if age_input.isdigit():
                self.player.set_age(int(age_input))
                break
            else:
                print("Invalid input... enter a number for your age.")
    
    def display_game(self):
        print("Word: ", self.display_word())
        print("Guessed letters: ", self.guessed_letters)
        print("Wrong guesses: ", self.wrong_guesses)
    
    def get_guess(self) -> str:
        while True:
            guess = input("Guess a letter or press 'q' to quit: ").strip().upper()
            if guess == "Q":
                return 'Q'
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input, enter a single letter from A-Z")
                continue
            if guess in self.guessed_letters:
                print(f"You already guessed '{guess}'. Try a different letter.")
                continue

            return guess
        
    def display_word(self):
        # asks self.guessed_letters list and adds letter if not in list with a space in between
        return " ".join(letter if letter in self.guessed_letters else "_" for letter in self.secret_word)

    def play(self):
        print("Welcome to Word Guess!")
        self.setup_player()
        print(f"\nHello, {self.player.get_first_name()}! Let's play.")

        while self.wrong_guesses < self.max_attempts:
            self.display_game()
            guess = self.get_guess()

            if guess == "Q":
                print("Thanks for playing!")
                break

            print(f"You successfully guessed: {guess}")
            self.guessed_letters.append(guess)

            if guess in self.secret_word:
                print(f"Good job! '{guess} is in the word!")
                if all(letter in self.guessed_letters for letter in self.secret_word):
                    print("\n--- UR A WINNER! ---")
                    self.display_game()
                    print(f"Congratulations! You guessed the word: {self.secret_word}!")
                    break
            else:
                self.wrong_guesses += 1
                print(f"Sorry, '{guess}' is not in the secret word.")

        if self.wrong_guesses == self.max_attempts:
            print("\n--- GAME OVERRR ---")
            self.display_game()
            print(f"You ran out of guesses... the secret word was: {self.secret_word}")

def main():
    game = WordGuess()
    game.play()

if __name__ == "__main__":
    main()

