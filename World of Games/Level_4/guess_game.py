import random
import os
from time import sleep


# The screen clear function

def screen_clear(screen_time_before_clear):
    # Waiting for 0.9 sec * difficulty level  seconds to clear the screen
    sleep(screen_time_before_clear)
    # Clearing the Screen
    os.system('clear')


def random_secret_number(_difficulty):
    start = 1  # inclusive
    end = _difficulty + 1  # exclusive
    x = random.randrange(start, end)
    # print(x)
    return x


def get_guess_number_from_user(difficulty_level):
    while True:
        try:
            game_guess_number_str = input(f"Enter a number between 1 to {difficulty_level} and press enter?")
            game_guess_number = int(game_guess_number_str)
            if 1 <= game_guess_number <= int(difficulty_level):
                print(f"You're choose guess number: {game_guess_number}")
                break
        except ValueError as ex:
            print(f"Your input is invalid, Please choose again only number between 1 and 5 :{game_guess_number}")
        except ZeroDivisionError as ex:
            print(f"The number 0 must not be selected")
        except NameError as ex:
            print("Name error message")
        except BaseException as ex:
            print(type(ex))
    return int(game_guess_number)


def play_guess_game(difficulty_level):
    screen_time = difficulty_level * 0.5
    screen_clear(screen_time)
    secret_number = random_secret_number(difficulty_level)
    # print(f"secret_number = {secret_number}")
    get_guess_number = get_guess_number_from_user(difficulty_level)
    print(f"The correct answer {secret_number}")
    if get_guess_number == secret_number:
        guess_game_result = True
    else:
        guess_game_result = False

    return guess_game_result




