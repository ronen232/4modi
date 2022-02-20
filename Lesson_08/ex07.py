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
BASE_URL = 'https://www.facebook.com'
USER = 'ronens.shimon@gmail.com'
PASSWORD = 'abcabc'
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
    # browser = webdriver.Chrome(executable_path="/home/ronen/dev/devops-experts/selenium/chromedriver")
    chrome_driver = webdriver.Chrome(chrome_options=chromeOptions)
    browser = chrome_driver
    browser.get(BASE_URL)
    driver = browser
    print('Page title: ', browser.title)
    sleep(5)

    driver.maximize_window()
    driver.find_element_by_xpath('//*[@id="email"]').clear
    input_text_box = driver.find_element_by_xpath('//*[@id="email"]')
    sleep(3)
    input_text_box.send_keys(USER)
    user_output = driver.find_element_by_xpath('//*[@id="email"]').text
    print(user_output)
    driver.find_element_by_xpath('//*[@id="pass"]').clear
    sleep(3)
    input_text_box = driver.find_element_by_xpath('//*[@id="pass"]')
    sleep(3)
    input_text_box.send_keys(PASSWORD)
    sleep(4)
    password_output = driver.find_element_by_xpath('//*[@id="pass"]').text
    print(password_output)
    # login_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]button'
    # login_button_xpath = '//*[@id="loginbutton"]'

    # login_button_element = driver.find_element_by_xpath(login_button_xpath)
    # login_button_element.click()
    driver.find_element(by=By.ID, value='loginbutton').click()
    print('Page title: ', browser.title)
    sleep(9)
    driver.quit()
    # for i in range(3, 5):
    #     sleep(i)
    #     browser.refresh()
    # browser.close()
    # browser.quit()


if __name__ == '__main__':
    chrome_example()
    # firefox_example()


