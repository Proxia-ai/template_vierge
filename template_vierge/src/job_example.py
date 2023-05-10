# import external packages
import pandas as pd

# import internal packages
from utils.util import get_config_section, read_yaml_data, get_log
from configs import base_config

# import internal dependancies modules
from template_vierge.src.compute import mean_compute

# import config files of the project
PROJECT_EMPL = base_config.project_empl
CONFIG_FILE_PATH = base_config.config_empl
YAML_CONFIG_FILE_PATH = base_config.yaml_config_empl

# import asset config
yaml_asset_config = read_yaml_data(YAML_CONFIG_FILE_PATH)

# specify the data : Many sources are possible :
# 1- Internal folder
data_folder = get_config_section(CONFIG_FILE_PATH, "data", "local")
# 2- Internal hdfs
# 3- External hdfs
# 4- S3 bucket (throw data loader _module)
# 5- api data (throw api data loader _module)


# Default param
seuil_old = yaml_asset_config[1]["asset_parameters"][0]["age_part"]["old"]
data_file = PROJECT_EMPL + yaml_asset_config[2]["asset_default_data"]["example_data"]


@get_log
def is_population_old(data=data_file, seuil=seuil_old):
    """
    Une fonction qui calcule si la population est agé ou non selon un parametre
    :param seuil: seuille de viellesse
    :param data: fichier de donnée en csv
    :return: Un boolean
    """

    df = pd.read_csv(data)
    age_col = df["age"]
    mean_col = mean_compute(age_col)
    return mean_col >= seuil


if __name__ == "__main__":
    print(is_population_old(data_file))