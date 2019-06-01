import os


def clear_screen():
    """clear the data on the screen
    """
    os.system("cls" if os.name == "nt" else "clear")
