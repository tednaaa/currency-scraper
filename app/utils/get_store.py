from utils.append_elements_to_store import append_elements_to_store


def get_store(currency_names, prices, prices_usd, prices_changes_percent):
    store = []

    append_elements_to_store(store, [
        currency_names,
        prices,
        prices_usd,
        prices_changes_percent
    ])

    return store
