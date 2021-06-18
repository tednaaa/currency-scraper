from selenium import webdriver
from utils.infinite_scroll import infinite_scroll
from utils.get_bitcoin_info import get_bitcoin_info
from utils.save_dict_in_json import save_dict_in_json
from utils.get_store import get_store


def main():
    driver = webdriver.Chrome('./drivers/chromedriver')

    URL = 'https://exmo.me'
    driver.get(URL)

    infinite_scroll(driver)

    bitcoin_info = get_bitcoin_info(driver)
    store = get_store(*bitcoin_info)

    save_dict_in_json('db', store)

    driver.quit()


if __name__ == '__main__':
    main()
