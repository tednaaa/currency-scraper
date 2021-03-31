from selenium import webdriver
from time import sleep
import json

def infinite_scroll(driver):
  show_more_button = driver.find_element_by_xpath('//div[@class="showMoreindex___2jfzg"]/span')

  while True:
    try:
      driver.execute_script('document.querySelector(".showMoreindex___2jfzg").scrollIntoView();')
      sleep(0.1)
      show_more_button.click()
    except:
      break

def get_bitcoin(driver):
  store = []

  URL = 'https://exmo.me'
  driver.get(URL)
  
  infinite_scroll(driver)

  currency_names = driver.find_elements_by_xpath('//h4[@class="currencyNameTextindex___D63V7"]')
  prices = driver.find_elements_by_xpath('//div[@class="lastPriceindex___3WMfX"]/div[1]')
  prices_usd = driver.find_elements_by_xpath('//div[@class="lastPriceindex___3WMfX"]/div[2]')
  prices_changes_percent = driver.find_elements_by_class_name('changeFor24hindex___3ek4T')

  for currency_name, price, price_usd, price_changes_percent in zip(currency_names, prices, prices_usd, prices_changes_percent):
    store.append({
      'name': currency_name.text,
      'price': f'{price.text} {price_usd.text}',
      'changes_percent': price_changes_percent.text
    })

  with open('db.json', 'w', encoding = 'utf-8') as database_file:
    json.dump(store, database_file, indent = 2, ensure_ascii = False)

def main():
  driver = webdriver.Chrome('./drivers/chromeDriverWindows')
  get_bitcoin(driver)
  driver.quit()

if __name__ == '__main__':
  main()