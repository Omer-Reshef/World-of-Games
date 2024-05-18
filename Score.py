from Utils import SCORES_FILE_NAME
import os


def calc_points_of_winning(difficulty):
    return (difficulty * 3) + 5


def add_score(difficulty):
    score_to_add = calc_points_of_winning(difficulty)
    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'r') as file:
            score_to_add += int(file.readline())
    with open(SCORES_FILE_NAME, 'w') as file:
        file.write(str(score_to_add))
