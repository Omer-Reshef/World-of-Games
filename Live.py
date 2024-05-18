#
# Omer Reshef
#

import time
import MemoryGame as MemoryGame
import GuessGame as GuessGame
import CurrencyRouletteGame as CurrencyRouletteGame
from Score import add_score

games = {1: MemoryGame.play, 2: GuessGame.play, 3: CurrencyRouletteGame.play}


def welcome(name):
    return f'Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.'


def choose_difficulty():
    print('Please choose game difficulty from 1 to 5:')
    try:
        diff_num = int(input())
    except ValueError:
        diff_num = -1
    while diff_num < 1 or diff_num > 5:
        print('Invalid input. Please enter a number from 1 to 5.')
        try:
            diff_num = int(input())
        except ValueError:
            diff_num = -1
    return diff_num


def choose_game():
    print("""
Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS
        """)
    try:
        game_num = int(input())
    except ValueError:
        game_num = -1
    while 3 < game_num < 1:
        print('Invalid input. Please enter a number from 1 to 3.')
        try:
            game_num = int(input())
        except ValueError:
            game_num = -1
    return game_num


def mock_loading(game_num, difficulty_num):
    print(f'Loading game {game_num} in difficulty {difficulty_num}', end=" ")
    for i in range(5):
        print('.', end=" ")
        time.sleep(0.5)
    print("\n\n***********************\n")


def load_game():
    game_num = choose_game()
    difficulty = choose_difficulty()
    mock_loading(game_num, difficulty)
    win = games[game_num](difficulty)
    if win:
        add_score(difficulty)

