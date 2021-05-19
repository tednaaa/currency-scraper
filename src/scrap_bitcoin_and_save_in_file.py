from open_json_and_save_dict import open_json_and_save_dict
from get_store import get_store


def scrap_bitcoin_and_save_in_file(driver):
    currency_names = driver.find_elements_by_xpath(
        '//h4[@class="currencyNameTextindex___3UaMu"]')
    prices = driver.find_elements_by_xpath(
        '//div[@class="lastPriceindex___cmcjB"]/div[1]')
    prices_usd = driver.find_elements_by_xpath(
        '//div[@class="lastPriceindex___cmcjB"]/div[2]')
    prices_changes_percent = driver.find_elements_by_xpath(
        '//div[@class="changeFor24hindex___27COs"]')

    store = get_store()
    open_json_and_save_dict('db', store)
