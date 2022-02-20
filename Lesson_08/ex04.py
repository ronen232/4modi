import os
import sys
#import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import logging
logging.getLogger().setLevel(logging.INFO)
input_text = 'כלב'
BASE_URL = 'https://translate.google.co.il/?sl=auto&tl=en&op=translate'


def firefox_example():
    print("Using Firefox...")
    options = Options()
    options.add_argument("-headless")
    browser = webdriver.Firefox()
    browser.get(BASE_URL)
    print('Page title: ', browser.title)
    for i in range(0, 5):
        sleep(i)
        browser.refresh()
    browser.close()
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
    chrome_driver = webdriver.Chrome(chrome_options=chromeOptions)
    browser = chrome_driver
    # browser = webdriver.Chrome(executable_path="/home/ronen/dev/devops-experts/selenium/chromedriver")
    browser.get(BASE_URL)
    driver = browser
    print('Page title: ', browser.title)
    sleep(5)

    driver.find_element_by_xpath('//textarea').clear
    input_text_box = driver.find_element_by_xpath('//textarea')
    sleep(3)
    input_text_box.send_keys(input_text)
    sleep(4)
    output = driver.find_element_by_xpath('//span[@jsname="txFAF"]/span').text
    print(f"Translate from heb to eng: {input_text } is {output}")

    driver.quit()
    # for i in range(3, 5):
    #     sleep(i)
    #     browser.refresh()
    # browser.close()
    # browser.quit()


if __name__ == '__main__':
    chrome_example()
    # firefox_example()


