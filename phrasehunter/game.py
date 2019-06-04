import sys
from random import choice

from common.clear_screen import clear_screen
from phrasehunter.data import PHRASES
from phrasehunter.phrase import Phrase


class Game:
    """The game class is handling the main processing of the game.
    """
    def __init__(self, phrases):
        """Constructor for taking in the phrase and processing it into 
        characters
        
        Parameters
        ----------
        phrases : string
            Phrase that the user will have to guess.
        """
        self.guesses = []
        self.phrases = [Phrase(phrase) for phrase in phrases.copy()]
        self.selected_phrase = choice(self.phrases)
        self.lives = 5

    def setup_screen(self):
        """function to refresh the screen and show the latest data information
        """
        clear_screen()
        self.header()

    def game_initialization(self):
        """Setup the game loop
        """
        while not self.display_game_won():
            self.setup_screen()
            player_guess = self.get_guess()
            for item in self.selected_phrase:
                item.check_guess(player_guess)
            if self.lives == 0:
                self.setup_screen()
                self.play_again(input("Oops you did again you lost al your "
                                      "lives! Would you like to play again? "
                                      "Y/n  "))
                print()
                break
        self.play_again(input("Would you like to play again? Y/n  "))

    def get_guess(self):
        """Get the input from the user. Validate the entry and update the
        number of remaining lives
        """
        guess = ""
        while not guess:
            try:
                player_guess = input("Please guess a letter: ")
                if player_guess.isdigit():
                    input("That is not a valid guess. Press enter to continue")
                    self.setup_screen()
                    continue
                elif (len(player_guess) > 1 or
                      not player_guess.isalpha() or
                      player_guess.lower() in self.guesses):
                    input("That is not a valid guess. Press enter to continue")
                    self.setup_screen()
                    continue
                else:
                    guess = player_guess
            except KeyboardInterrupt:
                input("\nYou can't interupt the game with ctrl-c.")
                self.setup_screen()
        self.guesses.append(guess.lower())
        if guess.lower() not in [char.original.lower() for char
                                 in self.selected_phrase]:
            self.lives -= 1
        return guess.lower()

    def display_game_won(self):
        """Display the message to the user when he has won the game.
        """
        if self.selected_phrase.validated_guessed_word():
            self.setup_screen()
            print("Congratulations! You won the game!!")
            print()
            return True
        return False

    def header(self):
        """Print the game header to the screen.
        """
        welcome = "+++++ Phrase Hunter +++++"
        print("*" * len(welcome))
        print(welcome)
        print("*" * len(welcome))
        print()
        print(f"Lives Left: {self.lives}")
        print(f"Letters Guessed: {self.guesses}\n")
        self.selected_phrase.display_phrase()

    def play_again(self, answer):
        """Method to check with the user if they want to play another game
        
        Parameters
        ----------
        answer : str
            Yes or No answer provided by the user.
        """
        self.answer = answer
        if self.answer.lower() == 'y':
            return Game(PHRASES).game_initialization()
        else:
            self.setup_screen()
            print("\nThank you for playing. Have a great day!\n")
            sys.exit()
