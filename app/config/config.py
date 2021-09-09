from selenium import webdriver
import os

URL = os.getenv('URL')
CHROME_DRIVER_PATH = os.getenv('CHROME_DRIVER_PATH')
SAVE_DATA_DIRECTORY_PATH = os.getenv('SAVE_DATA_DIRECTORY_PATH')
BITCOIN_CURRENCY_FILE_NAME = 'bitcoin-currency.json'

WEB_DRIVER = webdriver.Chrome(CHROME_DRIVER_PATH)
