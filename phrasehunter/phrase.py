from phrasehunter.character import Character


class Phrase:
    """Class representing the phrase data
    """
    def __init__(self, phrase):
        """Constructor to setup the phrase and split it to characters
        
        Parameters
        ----------
        phrase : str
            The selected phrase to be guessed
        """
        self.phrase = phrase
        self.phrase = [Character(char) for char in self.phrase]

    def __iter__(self):
        """method to make the phase and interable
        """
        yield from self.phrase

    def validated_guessed_word(self):
        """Validate the users guess and check if the full phrase is guessed.
        """
        guessed = []
        for self.char in self.phrase:
            if self.char.was_guessed:
                guessed.append(self.char)
        if len(guessed) == len(self.phrase):
            return True

    def display_phrase(self):
        """method to display the phrase to the user.
        """
        for char in self.phrase:
            print(char.display_guess_data, end=' ')
        print("\n")
