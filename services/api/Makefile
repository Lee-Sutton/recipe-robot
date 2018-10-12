.PHONY: clean
.PHONY: test
.PHONY: lint

clean: clean-pytest
	find . -name "*.pyc" -exec rm -f {} \;

clean-pytest:
	rm -rf .pytest_cache

pep8:
	flake8 recipe_robot && flake8 manage.py

lint: pep8
	pylint recipe_robot && pylint manage.py

test: clean
	pytest
