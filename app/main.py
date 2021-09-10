from utils import infinite_scroll, get_bitcoin_info, save_dict_in_json, get_store
from config import URL, WEB_DRIVER


def main():
    try:
        WEB_DRIVER.get(URL)

        infinite_scroll()

        bitcoin_info = get_bitcoin_info()
        store = get_store(*bitcoin_info)

        save_dict_in_json(store)
    finally:
        WEB_DRIVER.quit()


if __name__ == '__main__':
    main()
