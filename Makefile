DIR := $(shell pwd)

bump:
	python $(DIR)/bin/bump.py

test:
	nosetests --nocapture --with-coverage --cover-erase --cover-package=PackageName --cover-html --cover-html-dir=coverage_report

lint:
	pep8 src/PackageName
	pylint src/PackageName
