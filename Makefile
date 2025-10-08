# Define vars
.PHONY: env checks fix

# Define commands
env: 
	curl -LsSf https://astral.sh/uv/install.sh | sh
	uv sync --all-groups  # Installs all python dependencies + those needed for code quality checks
	
checks: format-check isort-check ruff-check pylint-check bandit-check yamllint-check sqlfluff-check

fix: format-fix isort-fix ruff-fix sqlfluff-fix

format-check:
	uv run black --check src/

format-fix:
	uv run black src/

isort-check:
	uv run isort --check src/

isort-fix:
	isort src/

ruff-check:
	uv run ruff check src/

ruff-fix:
	uv run ruff check src/ --fix

pylint-check:
	uv run pylint src/

bandit-check:
	uv run bandit -r src/

yamllint-check:
	uv run yamllint devops/ liquibase/ src/

sqlfluff-check:
	uv run sqlfluff lint src/

sqlfluff-fix:
	uv run sqlfluff fix src/

run-tests:
	@pytest --cov=src/ --cov-report=xml:artifacts/coverage.xml --junitxml=artifacts/test-results.xml