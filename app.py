from phrasehunter.data import PHRASES
from phrasehunter.game import Game


if __name__ == "__main__":
    phrase_game = Game(PHRASES)
    phrase_game.game_initialization()
