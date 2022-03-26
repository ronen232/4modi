import Utils

# def add_score(difficulty_level):
#     points_of_winning = (difficulty_level*3) + 5
#     # print(points_of_winning)
#     return points_of_winning


def add_score(points_of_winning):
    with open(Utils.SCORES_FILE_NAME, 'r+') as file:
        data = int(file.read())
        file.seek(0)
        file.write(str(data + points_of_winning))
        return points_of_winning
