from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():

    score_file = "scores.txt"
    file1 = open(score_file, 'r', encoding='utf-8')
    for line in file1:
        print(line, end='')
        scores = line
    file1.close()
    print('I am in index')
    return {f"name": f"Hello from World of Games! Your scores is : {scores}"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True,port=80)