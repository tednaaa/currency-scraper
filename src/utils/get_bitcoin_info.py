from utils.save_dict_in_json import save_dict_in_json
from utils.get_store import get_store


def get_bitcoin_info(driver):
    currency_names = driver.find_elements_by_xpath(
        '//h4[@class="currencyNameTextindex___3UaMu"]')
    prices = driver.find_elements_by_xpath(
        '//div[@class="lastPriceindex___cmcjB"]/div[1]')
    prices_in_usd = driver.find_elements_by_xpath(
        '//div[@class="lastPriceindex___cmcjB"]/div[2]')
    prices_changes_percent = driver.find_elements_by_xpath(
        '//div[@class="changeFor24hindex___27COs"]')

    return [currency_names, prices, prices_in_usd, prices_changes_percent]
