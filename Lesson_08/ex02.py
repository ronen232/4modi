from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import logging
logging.getLogger().setLevel(logging.INFO)
BASE_URL = 'http://www.walla.co.il/'


def chrome_example():
    print("Using Chrome...")
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--no-sandbox")
    chromeOptions.add_argument("--disable-dev-shm-using")
    chromeOptions.add_argument("--disable-extensions")
    # .add_argument(r"user-data-dir=.\cookies\\test")
    chromeOptions.headless = True
    # executable_path = "/home/ronen/dev/devops-experts/selenium/chromedriver"
    chrome_driver = webdriver.Chrome(chrome_options=chromeOptions)
    browser = chrome_driver
    # browser = webdriver.Chrome(executable_path="/home/ronen/dev/devops-experts/selenium/chromedriver")
    browser.get(BASE_URL)
    page_title01 = browser.title
    sleep(2)
    browser.refresh()
    page_title02 = browser.title
    print('Page title01: ', page_title01)
    print('Page title02: ', page_title02)
    if page_title01 == page_title02:
        print(f"The Title are the same:{page_title01}")
    browser.quit()


if __name__ == '__main__':
    chrome_example()
    # firefox_example()