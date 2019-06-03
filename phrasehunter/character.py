class Character():
    def __init__(self):
        self._char = None
        self._was_guessed = None
        self._guess = None

    def __str__(self):
        return f"{self._char}"

    @property
    def char(self):
        return self._char

    @char.setter
    def char(self, char_entry):
        if len(char_entry) == 1:
            self._char = char_entry
        else:
            raise ValueError("You made a wrong entry")

    @property
    def was_guessed(self):
        return self._was_guessed

    @was_guessed.setter
    def was_guessed(self):
        if self._char == ' ':
            self._was_guessed = True
        else:
            self._was_guessed = False

    def show_guess(self):
        if self._was_guessed:
            return self._char
        else:
            return "_"

    def check_guess(self, guess):
        self._guess = guess
        if self._guess == self._char:
            self.was_guessed = True
