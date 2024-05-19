from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# LOCAL_HOST_URL = "http://127.0.0.1:5000"
LOCAL_HOST_URL = "https://www.google.com"


def get_web_driver():
    return webdriver.Chrome()


def test_scores_service(url):
    driver = get_web_driver()
    driver.get(url)
    try:
        score_element = driver.find_element(By.ID, 'score')
        score = int(score_element.text)
    except (ValueError, NoSuchElementException) as e:
        score = -1

    return 1 <= score <= 1000


def main_function():
    success = test_scores_service(LOCAL_HOST_URL)
    if success:
        return 0
    else:
        return -1


main_function()
