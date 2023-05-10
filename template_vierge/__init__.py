from utils.util import read_yaml_data
from configs import base_config

YAML_CONFIG_FILE_PATH = base_config.yaml_config_empl
yaml_asset_config = read_yaml_data(YAML_CONFIG_FILE_PATH)
asset_name = yaml_asset_config[0]["asset_meta_information"]["asset_name"]

import sys

sys.path.append('../{}/'.format(asset_name))
