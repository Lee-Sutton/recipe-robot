.PHONY: clean
.PHONY: lint

clean: clean-pytest
	find . -name "*.pyc" -exec rm -f {} \;

clean-pytest:
	rm -rf .pytest_cache

lint:
	flake8 recipe_robot && flake8 manage.py

test: clean-pytest
	pipenv run pytest

