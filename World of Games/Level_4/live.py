def welcome(name):

    try:
        print("\n")
        print(f"Hello {name} and Welcome to the World of Games (WoG).")
        print(f"Can find many cool games to play.")
        print_status_temp = True
    except BaseException as ex:
        print(type(ex))
        print_status_temp = False
    return print_status_temp





