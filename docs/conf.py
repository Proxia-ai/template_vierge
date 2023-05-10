import os
import sys

sys.path.insert(0, os.path.abspath('..'))

from utils.util import read_yaml_data
from configs import base_config

YAML_CONFIG_FILE_PATH = base_config.yaml_config_empl
yaml_asset_config = read_yaml_data(YAML_CONFIG_FILE_PATH)

project = yaml_asset_config[0]["asset_meta_information"]["asset_name"]
copyright = yaml_asset_config[0]["asset_meta_information"]["copyright"]
author = yaml_asset_config[0]["asset_meta_information"]["author"]
release = yaml_asset_config[0]["asset_meta_information"]["asset_version"]

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']