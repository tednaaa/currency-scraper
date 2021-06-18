import json


def save_dict_in_json(json_file_name, save_data):
    with open(f'{json_file_name}.json', encoding='utf-8') as json_file:
        json.dump(save_data, json_file, indent=2, ensure_ascii=False)
