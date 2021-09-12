.ONESHELL:
SHELL := /bin/bash

PYTHON_MAIN_SCRIPTS := $(patsubst %.py,bin/%,$(notdir $(shell grep '__main__' -l $(CURDIR)/*.py)))

# TODO change to `python` when python 3 is fully supported
PYTHON=python3

ifeq (, $(shell which ${PYTHON}))
  $(error No python2 interpreter in PATH)
endif

python_version_full := $(wordlist 2,4,$(subst ., ,$(shell ${PYTHON} --version 2>&1)))
python_version_major := $(word 1,${python_version_full})
python_version_minor := $(word 2,${python_version_full})
python_version_patch := $(word 3,${python_version_full})

ifeq ($(shell expr $(python_version_major) \< 3), 1)
  ifeq ($(shell expr $(python_version_minor) \< 7), 1)
    $(error Python < 2.7 not supported)
  endif
endif

.PHONY: help test run doc
.EMPTY: lint

VENV?=venv
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
	virtualenv -p $(PYTHON) $(VENV)
	$(VENV)/bin/pip install --index-url https://pypi.org/simple --requirement requirements.txt
	$(VENV)/bin/pip install --index-url https://pypi.org/simple pyflakes
	$(VENV)/bin/pip install --index-url https://pypi.org/simple flake8
	touch $(VENV)/bin/activate

dist/panhunt: *.py
	${VENV}/bin/pyinstaller --onefile main.py

build: | venv dist/panhunt

lint: venv *.py
	$(VENV)/bin/flake8 --exclude=.git,${VENV} --ignore=E501 . && echo "Success"
	touch lint

rpm: build
	rpmbuild --define '_topdir $(PWD)/.rpmbuild' --define '_repodir $(PWD)' -ba package/rpm/panhunt.spec

clean:
	-rm -Rf dist build .venv .rpmbuild *.pyc panhunt.spec
