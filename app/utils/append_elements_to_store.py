def append_elements_to_store(store, elements):
    for currency_name, price, price_usd, price_changes_percent in zip(*elements):
        store.append({
            'name': currency_name.text.replace('\n', ''),
            'price': f'{price.text} {price_usd.text}',
            'changes_percent': price_changes_percent.text
        })
