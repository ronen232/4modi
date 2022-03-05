def utils(user_score_temp):
    def init_score_file_name(remark):
        try:
            f1 = open(score_file, "w")
            # f1.write(remark)
            # f1.write("\n")
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

    def write_line(score):
        with open(score_file, 'a') as file1:
            file1.write(score)
        file1.close()
        return

    def read_line():
        file1 = open(score_file, 'r', encoding='utf-8')
        for line in file1:
            print(line, end='')
        file1.close()
        return

    score_file = "./scores.txt"
    remarks = "# Score file #"
    # print(f"user_score_temp {user_score_temp}")
    init_score_file_name(remarks)
    write_line(str(user_score_temp))
    # read_line()
    return

