from flask import Flask
from Utils import SCORES_FILE_NAME

app = Flask("Score")


def get_html_scores(score):
    return f"""
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is <div id="score">{score}</div></h1>
        </body>
    </html>
    """


def get_html_error(error):
    return f"""
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1><div id="score" style="color:red">{error}</div></h1>
        </body>
    </html>
    """


@app.route('/', methods=['GET'])
def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            score = file.readline()
            return get_html_scores(score)
    except IOError as e:
        return get_html_error(e.strerror)


app.run(host='127.0.0.1', port="5000")
