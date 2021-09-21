from selenium import webdriver
import os

URL = os.getenv('URL')
CHROME_DRIVER_PATH = os.path.join(
    os.getcwd(), 'drivers', os.getenv('CHROME_DRIVER'))
SAVE_DATA_DIRECTORY_PATH = os.path.join(os.getcwd(), 'data')
BITCOIN_CURRENCY_FILE_NAME = 'bitcoin-currency.json'
CURRENCY_NAMES_XPATH = os.getenv('CURRENCY_NAMES_XPATH')
PRICES_XPATH = os.getenv('PRICES_XPATH')
PRICES_IN_USD_XPATH = os.getenv('PRICES_IN_USD_XPATH')
PRICES_CHANGES_PERCENT_CLASS_NAME = os.getenv(
    'PRICES_CHANGES_PERCENT_CLASS_NAME')


WEB_DRIVER = webdriver.Chrome(CHROME_DRIVER_PATH)
