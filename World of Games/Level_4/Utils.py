import os
from time import sleep
SCORES_FILE_NAME = "./Scores.txt"

# The screen clear function


def screen_cleaner():
    # Waiting for 7 seconds to clear the screen
    sleep(0.7)
    # Clearing the Screen
    os.system('clear')


screen_cleaner()
