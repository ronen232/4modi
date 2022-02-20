from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import logging
logging.getLogger().setLevel(logging.INFO)
BASE_URL01 = 'http://www.walla.co.il/'
BASE_URL02 = 'http://www.ynet.co.il/'


def firefox_example():
    print("Using Firefox...")
    options = Options()
    options.add_argument("-headless")
    # browser = webdriver.Firefox()
    browser = webdriver.Firefox(options=options)
    browser.get(BASE_URL02)
    print('Page title: ', browser.title)
    browser.quit()




def chrome_example():
    print("Using Chrome...")
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--no-sandbox")
    chromeOptions.add_argument("--disable-dev-shm-using")
    chromeOptions.add_argument("--disable-extensions")
    # .add_argument(r"user-data-dir=.\cookies\\test")
    chromeOptions.headless = True
    # executable_path = "/home/ronen/dev/devops-experts/selenium/chromedriver"
    # browser = webdriver.Chrome(executable_path="/home/ronen/dev/devops-experts/selenium/chromedriver")
    # chrome_driver = webdriver.Chrome(chrome_options=chromeOptions)
    chrome_driver = webdriver.Chrome(chrome_options=chromeOptions)
    browser = chrome_driver
    browser.get(BASE_URL01)
    print('Page title: ', browser.title)
    browser.quit()


if __name__ == '__main__':
    chrome_example()
    firefox_example()

