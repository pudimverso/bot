default:
	@just --list --justfile {{justfile()}}

install-pdm:
	curl -sSL https://pdm-project.org/install-pdm.py | python3 -

install:
	pdm install

run:
	pdm run python -m bot

activate-venv:
	@echo "Run the following command to activate the PDM virtual environment:"
	@echo 'eval "$(pdm venv activate in-project)"'

lint:
	pdm run ruff check .

lint-fix:
	poetry run ruff --fix .

check-types:
	pdm run pyright

setup-env:
	@echo "Setting up enviroment..."
	just activate
	just install-pdm
	just install
	just lint-fix
