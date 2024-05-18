import requests
import random
from requests.exceptions import RequestException

CURRENCY_URL = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_ztB6eZcGNIxb89QvE4268H1Zo1HIn8xHIru9Usnm&currencies=ILS"


def send_currency_request():
    try:
        # Sending an HTTP GET request to currency URL
        response = requests.get(CURRENCY_URL)
        # Parsing the JSON response
        return response.json()
    except RequestException as e:  # This is the correct syntax
        raise SystemExit(e)


def get_money_interval(difficulty, value_in_usd):
    response_json = send_currency_request()
    usd_to_ils_ex_rate = response_json["data"]["ILS"]
    value_in_ils = value_in_usd * usd_to_ils_ex_rate
    return value_in_ils - (5 - difficulty), value_in_ils + (5 - difficulty)


def get_guess_from_user(value_in_usd):
    guess_num = None
    print(f'Please guess what is the value of {value_in_usd} USD in ILS:')
    while guess_num is None:
        try:
            guess_num = float(input())
        except ValueError:
            guess_num = None
            print('Please enter a valid number')
    return guess_num


def play(difficulty):
    random_number = random.randint(1, 100)
    interval_tuple = get_money_interval(difficulty, random_number)
    guess_number = get_guess_from_user(random_number)
    win = interval_tuple[0] < guess_number < interval_tuple[1]
    print(
        f'Your guess is{" " if win else " not "}within the margin of error '
        f'({"{:.2f}".format(interval_tuple[0])}, {"{:.2f}".format(interval_tuple[1])})')
    if win:
        print("Y O U   W O N")
    else:
        print("Y O U   L O S T")
    return win
