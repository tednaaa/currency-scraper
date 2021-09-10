from config import WEB_DRIVER, CURRENCY_NAMES_XPATH, PRICES_XPATH, PRICES_IN_USD_XPATH, PRICES_CHANGES_PERCENT_CLASS_NAME


def get_bitcoin_info():
    currency_names = WEB_DRIVER.find_elements_by_xpath(
        CURRENCY_NAMES_XPATH)
    prices = WEB_DRIVER.find_elements_by_xpath(PRICES_XPATH)
    prices_in_usd = WEB_DRIVER.find_elements_by_xpath(PRICES_IN_USD_XPATH)
    prices_changes_percent = WEB_DRIVER.find_elements_by_class_name(
        PRICES_CHANGES_PERCENT_CLASS_NAME)

    return [currency_names, prices, prices_in_usd, prices_changes_percent]
