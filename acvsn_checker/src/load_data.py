import json
import os


# Loads configuration files containing controlled vocabulary
acvsn_dir = os.path.dirname(os.path.dirname(__file__))
data_folder = os.path.realpath(os.path.join(acvsn_dir, 'data'))


def find_path(file: str):
    return os.path.join(data_folder, file)


config_file = find_path('config.json')
gas_vocab_file = find_path('gas_vocab.json')
aerosol_vocab_file = find_path('aerosol_vocab.json')
cloud_vocab_file = find_path('cloud_vocab.json')
meteorology_vocab_file = find_path('meteorology_vocab.json')
photolysis_rate_vocab_file = find_path('photolysis_rate_vocab.json')
platform_vocab_file = find_path('platform_vocab.json')
radiation_vocab_file = find_path('radiation_vocab.json')


def load_config(file: str):
    with open(file) as json_data:
        temp_config_data = json.load(json_data)
    return temp_config_data


config_data = load_config(config_file)