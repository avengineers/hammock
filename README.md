# hammock

Automatic mocking tool for C

## CI

[![Ubuntu](https://github.com/avengineers/hammock/actions/workflows/linux.yml/badge.svg)](https://github.com/avengineers/hammock/actions/workflows/linux.yml)

[![Windows](https://github.com/avengineers/hammock/actions/workflows/windows.yml/badge.svg)](https://github.com/avengineers/hammock/actions/workflows/windows.yml)

## Build

This project uses [Pipenv](https://pypi.org/project/pipenv/). Run the following command to install it using your system's Python >=3.6 installation:

```shell
pip install pipenv
```

To create a virtual environment for development run:

```shell
pipenv install --dev
```

To delete the currently used virtual environment run:

```shell
pipenv --rm
```

To debug your Python code in VS Code you need to activate the virtual environment. To activate this project's virtualenv, run:

```shell
pipenv shell
```

After that you can select the virtual env in the list of Python installations.

Run all tests:

```shell
pipenv run pytest --verbose --capture=tee-sys
```

TODO: Somehow pytest fails when already installed in the system's python distribution. Uninstall it:

```shell
pip uninstall pytest
```

## Concept

The basic idea of Hammock is to use Python and libclang to process and parse sources of an item under test (IUT) for automatic creation of mockups.

Used libraries/sources/repos:

* [libclang](https://libclang.readthedocs.io/en/latest/)


## How to create and publish a pypi package

```shell
$ # Change version in setup.py to e.g. 0.5.0
$ python setup.py sdist
$ twine upload --repository-url https://test.pypi.org/legacy/ dist/hammock-0.5.0.tar.gz
```