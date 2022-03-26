import Utils
import os
from pathlib import Path


def utils():
    def init_score_file_name():
        try:
            f1 = open(score_file, "a")
            f1.close()
        except IOError:
            print("Error: can't find file or read data")
        # try-except-finally
        try:
            f1 = open(score_file, "a")
        except IOError:
            print("Fatal error...")
        finally:
            f1.close()
            # print("this will run anyway")
        return

    def read_line():
        filename = Path(score_file)
        filename.touch(exist_ok=True)
        file = open(score_file)
        with open(score_file, "r+") as f:
            f.seek(0)
            if not f.read():
                # print("No text")
                no_data = True
            else:
                # print("Got text")
                no_data = False
        f.close()
        return no_data

    def write_line_with_zero():
        with open(score_file, 'w') as file1:
            file1.seek(0)
            integer = 0
            file1.write(str(integer))
        file1.close()
        return

    score_file = "./Scores.txt"
    # print(f"user_score_temp {user_score_temp}")
    # init_score_file_name()
    no_data_in_file = read_line()
    # print(no_data_in_file)
    if no_data_in_file:
        write_line_with_zero()
    # print(read_line())
    return


