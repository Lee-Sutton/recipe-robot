.PHONY: clean

clean: clean-pytest
	find . -name "*.pyc" -exec rm -f {} \;

clean-pytest:
	rm -rf .pytest_cache
