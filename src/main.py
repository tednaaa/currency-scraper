from selenium import webdriver
from utils.infinite_scroll import infinite_scroll
from utils.scrap_bitcoin_and_save_in_file import scrap_bitcoin_and_save_in_file


def main():
    driver = webdriver.Chrome('./drivers/chromedriver')

    URL = 'https://exmo.me'
    driver.get(URL)

    infinite_scroll(driver)
    scrap_bitcoin_and_save_in_file(driver)

    driver.quit()


if __name__ == '__main__':
    main()
