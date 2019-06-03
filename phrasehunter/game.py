import sys
from random import choice

from common.clear_screen import clear_screen
from phrasehunter.data import PHRASES
from phrasehunter.phrase import Phrase


class Game:
    def __init__(self, phrases):
        self.guesses = []
        self.phrases = [Phrase(phrase) for phrase in phrases.copy()]
        self.selected_phrase = choice(self.phrases)
        self.lives = 5

    def get_guess(self):
        guess = ""
        while not guess:
            try:
                player_guess = input("Please guess a letter: ")
                if player_guess.isdigit():
                    input("That is not a valid guess. Press enter to continue")
                    clear_screen()
                    self.welcome()
                    continue
                elif len(player_guess) > 1:
                    input("That is not a valid guess. Press enter to continue")
                    clear_screen()
                    self.welcome()
                    continue
                elif not player_guess.isalpha():
                    input("That is not a valid guess. Press enter to continue")
                    clear_screen()
                    self.welcome()
                    continue
                elif player_guess.lower() in self.guesses:
                    input("That letter is already guessed!"
                          " Press enter to continue")
                    clear_screen()
                    self.welcome()
                    continue
                else:
                    guess = player_guess
            except KeyboardInterrupt:
                input("\nNice try, but you can't leave without finishing"
                      "the game.")
                clear_screen()
                self.welcome()
        self.guesses.append(guess.lower())
        if guess.lower() not in [letter.original.lower() for letter
                                 in self.selected_phrase]:
            self.lives -= 1
        return guess.lower()

    def game_won(self):
        if self.selected_phrase.validated_guessed():
            clear_screen()
            self.welcome()
            print("Congratulations! You won the game!!")
            print()
            return True
        return False

    def welcome(self):
        welcome = "+++++ Phrase Hunter +++++"
        print("*" * len(welcome))
        print(welcome)
        print("*" * len(welcome))
        print()
        print("Lives Left: {}".format(self.lives))
        print("Letters Guessed: {guesses}\n".format(guesses=self.guesses))
        # print()
        self.selected_phrase.display_phrase()

    def play_again(self, answer):
        self.answer = answer
        if self.answer.lower() == 'y':
            return Game(PHRASES).game_initialization()
        else:
            clear_screen()
            self.welcome()
            print("\nThank you for playing. Have a great day!\n")
            sys.exit()

    def game_initialization(self):
        while not self.game_won():
            clear_screen()
            self.welcome()
            player_guess = self.get_guess()
            for item in self.selected_phrase:
                item.check_guess(player_guess)
            if self.lives == 0:
                clear_screen()
                self.welcome()
                self.play_again(
                    input("Oh no! You ran out of lives. "
                          "Would you like to play again? Y/n  "))
                print()
                break
        self.play_again(input("Would you like to play again? Y/n  "))
