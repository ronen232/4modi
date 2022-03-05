import os
def read_line(score_file_temp):
    file1 = open(score_file_temp, 'r', encoding='utf-8')
    lines = file1.readlines()
    line = lines[0]
    print(line)
    file1.close()
    return line


def main_scores():
    score_file = "./scores.txt"
    user_score = read_line(score_file)
    # print(user_score)
    print(f"user_score is: {user_score}")
    os.system('docker rm -f my-flask')
    os.system('docker build -t my-first-flask .')
    os.system('docker run --rm -p 8083:80 -d --name my-flask my-first-flask')
    os.system('docker cp get.py my-flask:/app')
    os.system('docker cp "scores.txt" my-flask:/app')
    import requests
    r = requests.get("http://localhost:8083")
    print(r.text)

# <html>
#     <head>3
#         <title>Scores Game</title>
#     </head>
#     <body>
#         <h1>The score is <div id="score">{SCORE}</div></h1>
#     </body>
# </html>
#
