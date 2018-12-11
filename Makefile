clean:
	find . -name '*.pyc' -exec rm '{}' ';'
	find . -name '__pycache__' -type d -prune -exec rm -rf '{}' '+'

scrub: clean
	find . -name '*.egg-info' -type d -prune -exec rm -rf '{}' '+'
	rm -rf dist
	rm -rf build
	rm -rf htmlcov
	rm -f .coverage

install:
	pip install --no-cache-dir --editable .

test: install
	pip install -r requirements-test.pip
	sh run-tests.sh
