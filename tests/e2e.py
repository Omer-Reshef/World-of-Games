from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

LOCAL_HOST_URL = "http://127.0.0.1:8080"


def get_web_driver():
    return webdriver.Chrome()


def test_scores_service():
    driver = get_web_driver()
    driver.get(LOCAL_HOST_URL)
    try:
        score_element = driver.find_element(By.ID, 'score')
        score = int(score_element.text)
    except (ValueError, NoSuchElementException) as e:
        score = -1

    return 1 >= score >= 1000


def main_function():
    success = test_scores_service()
    if success:
        return 0
    else:
        return -1
