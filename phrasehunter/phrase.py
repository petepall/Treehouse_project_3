from phrasehunter.character import Character


class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase
        self.phrase = [Character(char) for char in self.phrase]

    def __iter__(self):
        yield from self.phrase

    def validated_guessed_word(self):
        guessed = []
        for self.char in self.phrase:
            if self.char.was_guessed:
                guessed.append(self.char)
        if len(guessed) == len(self.phrase):
            return True

    def display_phrase(self):
        for char in self.phrase:
            print(char.display_guess_data, end=' ')
        print("\n")
