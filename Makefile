_BUILD_DOCS = ./docs/_build
_STATICS_DOCS = ./docs/_static
_TEMPLATES_DOCS = ./docs/_templates
_make_FILE_DOCS = ./docs/make.bat
_MAKEFILE_FILE_DOCS = ./docs/Makefile

LINT_FAIL_THRESHOLD ?= 4
PROJECT_NAME = $(notdir $(CURDIR))

.PHONY: init
init:
	echo "installing required packages"
	pipenv install -r requirements.txt

.PHONY: test
test:
	echo "clean test"
	@rm -rf ./*.pytest_cache
	echo "Executing unit tests"
	python -m pytest tests

.PHONY: sec
sec:
	@pipenv run python -m bandit -r ${PROJECT_NAME}/${PROJECT_NAME}

.PHONY: lint
lint:
	@pipenv run python -m pylint --fail-under ${LINT_FAIL_THRESHOLD} --rcfile=.pylintrc ${PROJECT_NAME}/${PROJECT_NAME}

.PHONY: doc
doc:
	echo "Regenerating documentation"
	@rm -rf $(_BUILD_DOCS)
	@rm -rf $(_STATICS_DOCS)
	@rm -rf $(_TEMPLATES_DOCS)
	@rm -rf $(_make_FILE_DOCS)
	@rm -rf $(_MAKEFILE_FILE_DOCS)
	@pipenv run sphinx-apidoc -o docs .
	@pipenv run sphinx-build -M html docs docs/_build

.PHONY: pack
pack:
	echo "cleaning"
	@rm -rf ./build
	@rm -rf ./dist
	@rm -rf ./*.egg-info
	echo "Packaging application"
	python3 setup.py sdist bdist_wheel

.PHONY: upload
publish:
	python3 -m twine upload --repository testpypi dist/* --config-file .secrets/.env

.PHONY: all
all: init test sec lint doc pack publish