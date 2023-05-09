GENERATED_DOCS = ./docs/{_build/*}
LINT_FAIL_THRESHOLD ?= 4
PROJECT_NAME = template_vierge

.PHONY: init
init:
	echo "installing required packages"
	pipenv install -r requirements.txt

.PHONY: test
test:
	echo "Executing unit tests"
	python -m pytest tests

.PHONY: sec
sec:
	@pipenv run python -m bandit -r src/${PROJECT_NAME}

.PHONY: lint
lint:
	@pipenv run python -m pylint --fail-under ${LINT_FAIL_THRESHOLD} --rcfile=.pylintrc src/${PROJECT_NAME}

.PHONY: doc
doc:
	echo "Regenerating documentation"
	@rm -rf $(GENERATED_DOCS)
	@pipenv run sphinx-apidoc -o docs .
	@pipenv run sphinx-build -M html docs docs/_build

.PHONY: pack
pack:
	echo "Packaging application"
	python3 -m pip install --upgrade build
	python3 -m build

.PHONY: all
all: init test sec lint doc pack