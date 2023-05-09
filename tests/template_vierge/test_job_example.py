def test_is_population_old():
    """
    Ceci est une fonction exemle pour tester la fonction associé dans le dossier src
    Pour executer tous les tests dans la ligne de commande on utilise : python -m pytest tests
    :return: resultats du test unitaire
    """
    from utils.util import get_config_section
    from configs import base_config

    config_file_path = base_config.config_empl

    data_folder = get_config_section(config_file_path, "data", "local")
    data_file = data_folder + "/emp.csv"

    from src.template_vierge import job_example
    job_example.seuil_old = 20

    assert job_example.is_population_old(data_file) == False
