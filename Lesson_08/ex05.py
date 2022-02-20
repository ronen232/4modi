from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import logging
logging.getLogger().setLevel(logging.INFO)
BASE_URL = 'http://www.youtube.com/'


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
    sleep(1)

    # search by xpath
    search_box_by_xpath = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
    search_box_by_xpath.send_keys('hello adele')
    search_box_by_xpath = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button')
    search_box_by_xpath.click()

    for i in range(3, 5):
        sleep(i)
        browser.refresh()
    browser.close()
    browser.quit()


if __name__ == '__main__':
    chrome_example()
    # firefox_example()

