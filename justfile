install-pdm:
	curl -sSL https://pdm-project.org/install-pdm.py | python3 -

install:
	pdm install

run:
	pdm run python -m bot

lint:
	pdm run ruff check .

lint-fix:
	poetry run ruff --fix .

check-types:
	pdm run pyright

setup-env:
	@echo "Setting up enviroment..."
	just install-poetry
	just install
	just lint-fix
