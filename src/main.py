from selenium import webdriver
from time import sleep
import json
from infinite_scroll import infinite_scroll
from scrap_bitcoin_and_save_in_file import scrap_bitcoin_and_save_in_file


def main():
    driver = webdriver.Chrome('./drivers/chromeDriverWindows')

    URL = 'https://exmo.me'
    driver.get(URL)

    infinite_scroll(driver)
    scrap_bitcoin_and_save_in_file(driver)

    driver.quit()


if __name__ == '__main__':
    main()
