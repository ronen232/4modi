import random
import os
from time import sleep


def random_memory_list_of_number(_difficulty):
    start = 1  # inclusive
    end = 101  # exclusive
    n = _difficulty  # size
    x = [random.randint(start, end) for _ in range(n)]
    return x


# The screen clear function
def screen_clear():
    # Waiting for 0.9 sec * difficulty level  seconds to clear the screen
    sleep(0.9)
    # Clearing the Screen
    os.system('clear')


def input_user_list_of_number(difficulty_level):
    checkit = True
    while checkit:
        try:
            checkit = True
            input_string = input(f"""Enter {difficulty_level} numbers between 1 - 101 that you're remember from the screen each elements of a list separated 
            by space?""")
            print("\n")
            user_list = input_string.split()
            # print(list)
            # print('list: ', user_list)
            if len(user_list) == difficulty_level:
                for i in range(len(user_list)):
                    # convert each item to int type
                    user_list[i] = int(user_list[i])
                    if 1 <= user_list[i] <= 101:
                        # print(f"You're choose : {user_list[i]}")
                        checkit = False
                    else:
                        checkit = True

        except ValueError as ex:
            print(f"Your input is invalid, Please choose again only number between 1 and 100 :{user_list}")
            checkit = True
        except NameError as ex:
            print("Name error message")
            checkit = True
        except ZeroDivisionError as ex:
            print(f"The number 0 must not be selected")
        except BaseException as ex:
            checkit = True
            print(type(ex))

    return user_list


def play_memory_game(difficulty_level):
    random_memory_list_of_number(difficulty_level)
    memory_list = random_memory_list_of_number(difficulty_level)
    print("\n")
    print(f"Here are the memory_list that you should remember: {memory_list}")
# wait for 0.7 seconds to clear screen
    screen_time = difficulty_level * 0.9
    sleep(screen_time)
# now call function we defined above to clear the screen

    screen_clear()
    input_user_list = input_user_list_of_number(difficulty_level)
    input_user_list.sort()
    memory_list.sort()
    input_user_list_new = set(input_user_list)
    memory_list_new = set(memory_list)

    if input_user_list_new == memory_list_new:
        print("The lists are the same")
        memory_game_result = True
    else:
        print("The lists are not the same")
        memory_game_result = False
    print(memory_list)
    print(input_user_list)

    return memory_game_result


