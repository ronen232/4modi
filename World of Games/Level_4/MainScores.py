from flask import Flask

import Utils

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world"


@app.route("/score")
def score_server():
    try:
        with open(Utils.SCORES_FILE_NAME) as f:
            score = f.readline()
            return f"<html> \
                        <head> \
                            <title>Scores Game</title> \
                        </head> \
                        <body> \
                            <h1>The score is <div id=\"score\">{score}</div></h1> \
                        </body> \
                    </html>"
    except BaseException as ex:
        print(ex)
        return f"<html> \
                    <head> \
                        <title>Scores Game</title> \
                    </head> \
                    <body> \
                        <h1><div id=\"score\" style=\"color:red\">{ex}</div></h1> \
                    </body> \
                </html>"


app.run(port=5001, debug=True)
