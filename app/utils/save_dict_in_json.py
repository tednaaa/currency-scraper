import json
from pathlib import Path
from config import SAVE_DATA_DIRECTORY_PATH, BITCOIN_CURRENCY_FILE_NAME


def save_dict_in_json(save_data):
    Path(SAVE_DATA_DIRECTORY_PATH).mkdir(parents=True, exist_ok=True)

    with open(f'{SAVE_DATA_DIRECTORY_PATH}/{BITCOIN_CURRENCY_FILE_NAME}', 'w+', encoding='utf-8') as json_file:
        json.dump(save_data, json_file, indent=2, ensure_ascii=False)
