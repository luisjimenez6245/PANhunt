.ONESHELL:
SHELL := /bin/bash

PYTHON_MAIN_SCRIPTS := $(patsubst %.py,bin/%,$(notdir $(shell grep '__main__' -l $(CURDIR)/*.py)))

.PHONY: help test run doc
.EMPTY: lint

VENV?=.venv
VENV_ACTIVATE=. $(VENV)/bin/activate

.DEFAULT: help

define MSG_HELP
Usage:
    make help
    make lint
    make build
    make rpm
    make clean
endef
export MSG_HELP

help:
	@: $(info ${MSG_HELP})

venv: $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	test -d $(VENV) || virtualenv -p python2 $(VENV)
	${VENV}/bin/pip install --extra-index-url https://pypi.org/simple --requirement requirements.txt
	${VENV}/bin/pip install --extra-index-url https://pypi.org/simple pyflakes==1.3.0
	${VENV}/bin/pip install --extra-index-url https://pypi.org/simple flake8==2.0
	touch $(VENV)/bin/activate

dist/panhunt: *.py
	${VENV}/bin/pyinstaller --onefile panhunt.py

build: | venv dist/panhunt

lint: venv *.py
	$(VENV)/bin/flake8 --exclude=.git,${VENV} --ignore=E501 . && echo "Success"
	touch lint

rpm: build
	rpmbuild --define '_topdir $(PWD)/.rpmbuild' --define '_repodir $(PWD)' -ba package/rpm/panhunt.spec

clean:
	-rm -Rf dist build .venv .rpmbuild *.pyc panhunt.spec
