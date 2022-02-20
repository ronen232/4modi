import os
import sys
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
    # browser = webdriver.Chrome(executable_path="/selenium/chromedriver")
    browser.get(BASE_URL)
    driver = browser
    print('Page title: ', browser.title)
    sleep(5)

    driver.find_element_by_xpath('//textarea').clear
    input_text_box_by_xpath1 = driver.find_element_by_xpath('//textarea')
    print(f"WebElement_1: {input_text_box_by_xpath1}")

    input_text_box_by_xpath2 = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
    input_text_box_by_xpath2.send_keys(input_text)
    print(f"WebElement_2: {input_text_box_by_xpath2}")

    sleep(3)
    input_text_box_by_xpath1.send_keys(input_text)
    sleep(6)
    output = driver.find_element_by_xpath('//span[@jsname="txFAF"]/span').text
    print(input_text)
    print(output)

    driver.quit()



if __name__ == '__main__':
    chrome_example()
    # firefox_example()


