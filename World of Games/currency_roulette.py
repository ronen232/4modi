import random
import time
import os
os.system('pip install --user currencyconverter')
def play_currency_roulette(difficulty_level):
    def currency_converter_func():
        from currency_converter import CurrencyConverter
        c = CurrencyConverter()
        factor = 100
        ILS = c.convert(factor, 'USD', 'ILS')
        ILS = ILS / 100
        print(f"The USD/ILS is: {ILS}")
        return ILS

    def get_guess_from_user(range_low_user, range_high_user):
        checkit = True
        while checkit:
            try:
                checkit = True
                get_guess = input(f"Enter your guess number between {range_low_user } and {range_high_user}? ")
                print("\n")
                # print(list)
                # print('list: ', user_list)
                get_guess = int(get_guess)
                if range_low_user <= get_guess <= range_high_user:
                    print(f"You're guess: {get_guess}")
                    break
            except ValueError as ex:
                print(f"""Your input is invalid, 
                Please choose again only number between {range_low_user} and {range_high_user} : {get_guess}""")
                checkit = True
            except NameError as ex:
                print("Name error message")
                checkit = True
            except ZeroDivisionError as ex:
                print(f"The number 0 must not be selected")
            except BaseException as ex:
                checkit = True
                print(type(ex))
        return get_guess

    def get_money_interval():
        x = random.randint(1, 100)
        print(x)
        t_temp = int(currency_converter_func() * x)
        range_low_temp = t_temp - (5 - difficulty_level)
        range_high_temp = t_temp + (5 - difficulty_level)
        # print(t_temp)
        return t_temp, range_low_temp, range_high_temp

    t, range_low, range_high = get_money_interval()
    print(f"The range is between: {range_low} -  {range_high}")
    user_guess = get_guess_from_user(range_low, range_high)
    # print(user_guess)
    print(f"The correct answer is:{t}")
    if user_guess == t:
        currency_game_result = True
    else:
        currency_game_result = False
    time.sleep(2)
    return currency_game_result
