import currency_roulette
import Utils
from guess_game import play_guess_game
from memory_game import play_memory_game
from currency_roulette import play_currency_roulette
from utils import utils
from score import add_score


def load_game():

    print("""Please choose a game to play:
     1 -  Memory Game - a sequence of numbers will apper for 1 second and you have guess it back
     2 -  Guess Game - guess a number and see if you chose like the computer
     3 -  Currency Roulette - try and guess the value of a random amount of USD in ILS""")

    def choose_game_number():

        while True:
            try:
                input_game_number = input("Please choose number between 1 to 3 for a game to play?")
                input_game_number = int(input_game_number)
                if 1 <= input_game_number <= 3:
                    print(f"You're choose to play game number: {input_game_number}")
                    break

            except ValueError as ex:
                print(f"Your input is invalid, Please choose again only number between 1 and 3 :{input_game_number}")
            except NameError as ex:
                print("Name error message")
            except BaseException as ex:
                print(type(ex))
        return int(input_game_number)

    def choose_game_difficulty_level():
        while True:
            try:
                game_difficulty_level = input("Please choose game difficulty from 1 to 5:")
                game_difficulty_level = int(game_difficulty_level)
                if 1 <= game_difficulty_level <= 5:

                    print(f"You're choose game_difficulty: {game_difficulty_level}")
                    break
            except ValueError as ex:
                print(f"Your input is invalid, Please choose again only number between 1 and 5 :{game_difficulty_level}")
            except NameError as ex:
                print("Name error message")
            except ZeroDivisionError as ex:
                print(f"The number 0 must not be selected")
            except BaseException as ex:
                print(type(ex))
        return int(game_difficulty_level)

    game_number = choose_game_number()
    difficulty_level = choose_game_difficulty_level()
    game_result = None
    # print(game_number)
    # print(difficulty_level)
    if game_number == 1:
        game_result = play_memory_game(difficulty_level)
    elif game_number == 2:
        game_result = play_guess_game(difficulty_level)
    elif game_number == 3:
        game_result = play_currency_roulette(difficulty_level)

    if game_result:
        print("You have won")
        print(difficulty_level)
        print(f"The score for this round is: {(int(difficulty_level) * 3) +5}")
        points_of_winning = ((int(difficulty_level) * 3) + 5)
        utils()
        user_score = add_score(points_of_winning)
        # print(f"user_score: {user_score}")
    else:
        # print(difficulty_level)
        print("You loose")








