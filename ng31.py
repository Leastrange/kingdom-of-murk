# this is a newer edition of ngg.py.

import numpy as np
import sys

class NumberGuess:

    lives = 3
    number = np.random.randint(1, 26)
    min_ = 1
    score = 0

    def choose_game_mode(self):
        answer = input("Choose your difficulty. Easy, medium or hard? (e/m/h)\t")
        if answer.lower() == "e":
            NumberGuess.max_ = 25
            NumberGuess.score_factor = 5
        elif answer.lower() == "m":
            NumberGuess.max_ = 50
            NumberGuess.score_factor = 10
        else:
            NumberGuess.max_ = 100
            NumberGuess.score_factor = 15

    def _create_secret_number(self):
        return np.random.randint(NumberGuess.min_, NumberGuess.max_ + 1)

    def create_game(self):
        secret_number = self._create_secret_number()

        print(f"Current Score: {NumberGuess.score}")
        print(f"Current lives: {NumberGuess.lives}")


        try:
            guess = input(f"Guess a number between {NumberGuess.min_} - {NumberGuess.max_}: ")
            guess = int(guess)
            while (guess < NumberGuess.min_ or guess > NumberGuess.max_):
                print("Please enter your guess within the range.")
                guess = int(input(f"Guess a number between {NumberGuess.min_} - {NumberGuess.max_}: "))

        except:
            raise ValueError('Please enter an integer within the range given')

        flag = True
        while flag:
            guess = int(input(f"Guess a number between {NumberGuess.min_} - {NumberGuess.max_}: "))

            if guess > secret_number:
                print("Go lower.")
                guess = input(f"Guess a number between {NumberGuess.min_} - {NumberGuess.max_}: ")
                NumberGuess.lives -= 1

            elif guess < secret_number:
                print("Go higher.")
                guess = input(f"Guess a number between {NumberGuess.min_} - {NumberGuess.max_}: ")
                NumberGuess.lives -= 1

            elif guess == secret_number:
                print("Congrats! You have guessed the correct number!")
                print(f"Secret number was: {guess}")

                NumberGuess.score += NumberGuess.score_factor
                print(f"Total score: {NumberGuess.score}")

                self.play_or_quit()
                flag = False
            if NumberGuess.lives == 0:
                print("You lost.")
                self.play_or_quit()

    def play_or_quit(self):
        play_or_quit = input("\nDo you want to play again? [y]/[N]: ")
        if play_or_quit.lower() == "y":
            self.start_game()
        elif play_or_quit.lower() == "n":
            print("Game has ended.")
            sys.exit()


    def start_game(self):
        self.choose_game_mode()
        self.create_game()

game = NumberGuess()
game.start_game()

