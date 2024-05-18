import random


def generate_number(difficulty):
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    guess_num = None
    print(f'Please enter a number between 1 and {difficulty}:')

    while guess_num is None:
        try:
            guess_num = int(input())
            if guess_num < 1 or guess_num > difficulty:
                print('Number not in range. Please try again:')
                guess_num = None

        except ValueError:
            print('Invalid input. Please try again:')
            guess_num = None

    return guess_num


def compare_results(res1, res2):
    return res1 - res2


def play(difficulty):
    secret_number = generate_number(difficulty)
    guess_num = get_guess_from_user(difficulty)
    win = compare_results(guess_num, secret_number) == 0
    print(f'The secret number was {secret_number}')
    if win:
        print("Y O U   W O N")
    else:
        print("Y O U   L O S T")

    return win
