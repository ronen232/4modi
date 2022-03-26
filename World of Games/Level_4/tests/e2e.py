from selenium.webdriver.common.by import By


def test_scores_service():
    from selenium import webdriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-using")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument(r"user-data-dir=.\cookies\\test")
    chrome_options.headless = True
    chrome_driver = webdriver.Chrome(chrome_options=chrome_options)
    chrome_driver.get('http://localhost:5001/score')
    score = int(chrome_driver.find_element(by=By.ID, value='score').text)
    return 1 < score < 1000


if __name__ == "__main__":
    if test_scores_service():
        exit(0)
    else:
        exit(1)
