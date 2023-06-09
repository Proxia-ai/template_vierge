# Version actuelle
version = 1.0.0

# Utilisation
Le projet pourrait etre utile pour:
- Travailler un projet sur un template bien défini (git clone)
- créer un package dans pypi (make all)
- Passer la partie ci dans gitLab (ajouter gitlab_ci.yaml et faite réference au Makefile)

Pour utiliser le template. 

`git clone https://github.com/Proxia-ai/template_vierge.git`

# Prise en main
- Definir les parametre projet dans configs.?.yaml
- Travailler avec /.data pour stoquer les data
- Appeler d'autres asset en se basant sur ce projet, il va vous falloir juste de mettre le nouveau Yaml dans configs
- vous pourriez ajouter d'autre dossier comme par exemple .secrets (selon la nature du projet)

# Contenu du projet
Le template contient deja un exemple:
* le dossier .data (facultatif) : 
  * où on stoke les donnée 
  * la réference à ce dossier est dans configs/config.ini
* le dossier configs :
  * __init__.py : utile pour en faire une librairie interne surtout lors du build (à ne pas toucher)
  * base_config.py: il contient les réference vers les fichiers de configuration d'une maniére génerique ( à toucher avec précaution)
  * config.ini : il contient l'emplacement des dossier et fichier utile pour le projet. Il faut mettre des liens indépendante de l'emplacement machine
  * ?_config.yaml: il contient les parametres du projet. Il ne faut pas toucher à la partie meta-information. Le reste dépond du projet
* docs : Il contient l'ensemble de la documentation qui se génere automatiquement à partir des docs string dans les différents scripts
* ?/src : Il contient le travail çàd le source code du projet
  * __init__.py: à ne pas toucher utile lors du build
* tests/?: Un dossier qui contient l'ensemble des tests unitaires à en faire sur les données qui sont dans .data
* utils : Il contient l'enseble des fonction génerique au projet
  * __init__.py : à ne pas supprimer
* .gitignore : contient l'enseble des dossiers et fichiers à ignorer (à toucher selon le projet)
* .pylintrc : L'ensemble des regles à verifier lors de l'étape lintage du code
* LICENCE : Contient une licence Standard, utile pour pypi
* main.py : Le script de lancement par defaut si pas d'utilisation des source. mettez juste le nom du projet dans la console et il va lancer ce script tout seul
* Makefile : Ensemble d'instruction utile pour la partie Ci
* README.md : documentation pour bien utiliser le projet à lire
* requirements.txt : Il est recommandé d'extraire ce fichier requirements.txt avant un push git
* setup.cfg : fichier utile pour le build
* setup.py: fichier d'installation du projet

# NB:
- Dans cette version il faut placer les dépendances dans setup.py si vous voulez builder un package. Cette partie n'est encore automatique
- pour le build dans pypi, il faut créer un fichier de réferences qui contient les identifiants et les réference d'authentification

# Utilisation en tant que package
exemple:

`pip install -i https://test.pypi.org/simple/ template-vierge==0.0.3.35`

L'upgrade du package de l'autre coté sera comme ça:

`pip install -i https://test.pypi.org/simple/ template-vierge --upgrade --no-cache-dir`

il faut aussi pense à mettre le dossier site-package accessible à tous les users:

`sudo chmod -R ugo+rX /home/zied/PycharmProjects/pythonProject_test/venv/lib/python3.10/site-packages`

