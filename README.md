# Documentation Sphinx

Pour génerer de la documentation Sphinx, voici les principales commandes à faire dans le dossier /docs

`sphinx-quickstart`

- Aprés cette premiére étape il faut ajouter le mots modules dans index.rst
- La commande suivante est à refaire cette commande surtout quand ajoute un nouveau script

`sphinx-apidoc -o . ..`

`make html`

`make clean html`

Pour plus d'info: [Cliquez ici](https://towardsdatascience.com/documenting-python-code-with-sphinx-554e1d6c4f6d)

# Package your work

`python3 -m pip install --upgrade build`

- Cette commande génere un tar.gz (code source) + .whl (code build) dans le dossier dist

`python3 -m build`

Pour plus d'info: [Cliquez ici](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

# to upload python package to pypi
`python3 setup.py sdist bdist_wheel`

`python3 -m twine upload --repository testpypi dist/* --config-file .pypirc`

L'upgrade du package de l'autre coté sera comme ça:

`pip install -i https://test.pypi.org/simple/ template-vierge --upgrade --no-cache-dir`

il faut aussi pense à mettre le dossier site-package accessible à tous les users:

`sudo chmod -R ugo+rX /home/zied/PycharmProjects/pythonProject_test/venv/lib/python3.10/site-packages`

# to extract requirements.txt via pipenv

`pipenv pip -r freeze > requirements.txt`