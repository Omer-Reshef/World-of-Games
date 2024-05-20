from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
os.environ["TEST_ENV"] = "1"

LOCAL_HOST_URL = "http://127.0.0.1:5000"
# LOCAL_HOST_URL = "https://www.google.com"


def get_web_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # return webdriver.Chrome()
    return driver


def test_scores_service(url):
    driver = get_web_driver()
    driver.get(url)
    try:
        score_element = driver.find_element(By.ID, 'score')
        score = int(score_element.text)
    except (ValueError, NoSuchElementException) as e:
        score = -1
    return 1 <= score <= 1000


def main():
    print("before test_scores_service")
    success = test_scores_service(LOCAL_HOST_URL)
    print(f'after test_scores_service.  success: {success}')
    if success:
        exit(0)
    else:
        exit(-1)


# main()
