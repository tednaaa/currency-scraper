import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

WEB_DRIVER = webdriver.Chrome(
    CHROME_DRIVER_PATH, chrome_options=chrome_options)
