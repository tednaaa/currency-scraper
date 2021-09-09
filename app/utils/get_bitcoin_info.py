from config import WEB_DRIVER


def get_bitcoin_info():
    currency_names = WEB_DRIVER.find_elements_by_xpath(
        '//div[@class="currencyNameTextindex___3UaMu"]')
    prices = WEB_DRIVER.find_elements_by_xpath(
        '//div[@class="lastPriceindex___cmcjB"]/div[1]')
    prices_in_usd = WEB_DRIVER.find_elements_by_xpath(
        '//div[@class="lastPriceindex___cmcjB"]/div[2]')
    prices_changes_percent = WEB_DRIVER.find_elements_by_class_name(
        'changeFor24hindex___27COs')

    return [currency_names, prices, prices_in_usd, prices_changes_percent]
