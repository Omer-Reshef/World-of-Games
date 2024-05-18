import random
import time
import os
from subprocess import call


def generate_sequence(difficulty):
    gen_list = []
    for i in range(difficulty):
        gen_list.append(random.randint(1, 101))
    return gen_list


def get_list_from_user(difficulty):
    if difficulty == 1:
        print(f'Try to remember - what was the number?\n'
              f'Please insert a single number and press Enter:')
    else:
        print(f'Try to remember - what were the numbers?\n'
              f'Please insert a sequence of {difficulty} numbers separated by commas and press Enter:')
    valid_sequence = False
    while valid_sequence is False:
        valid_sequence = True
        input_from_user = input()
        lst = input_from_user.strip().split(",")
        if len(lst) == difficulty:
            try:
                lst = [int(x) for x in lst]
            except ValueError:
                valid_sequence = False
                print("Invalid input. Please try again:")
        else:
            valid_sequence = False
            print("Invalid input. Please try again:")
    return lst


def is_list_equal(lst1, lst2):
    return sorted(lst1) == sorted(lst2)


def temporary_display_list(ls, time_in_sec):
    print(f'A sequence of numbers will show on the screen for exactly {time_in_sec} seconds.\n'
          f'Press Enter when you\'re ready.')
    input()
    print(*ls, sep=", ", end="")
    time.sleep(time_in_sec)
    print("", end="\r")


def play(difficulty):
    gen_list = generate_sequence(difficulty)
    temporary_display_list(gen_list, 0.7)
    input_list = get_list_from_user(difficulty)
    win = is_list_equal(gen_list, input_list)
    print(f'The numbers where: {gen_list}')
    if win:
        print("Y O U   W O N")
    else:
        print("Y O U   L O S T")

    return win
