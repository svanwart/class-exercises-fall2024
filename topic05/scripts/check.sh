poetry run pytest -v
poetry run flake8
poetry run black . --check
poetry run isort . --check --diff