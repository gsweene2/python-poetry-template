## python-poetry-template

## How this project was created

Install
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

source $HOME/.poetry/env
```

Initialize new project
```bash
poetry new python-poetry-template
```

## What about pre existing projects?

[Initialising a pre-existing project](https://python-poetry.org/docs/basic-usage/#initialising-a-pre-existing-project)

## Activate virtual env

```bash
poetry shell
```

## Install dependencies

```bash
poetry install
```

## Run Tests

```bash
poetry run pytest
```

## Setting up the precommit hook

```bash
poetry run pre-commit sample-config > .pre-commit-config.yaml
poetry run pre-commit install
```
