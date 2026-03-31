install:
	uv sync

brain-games:
	uv run brain-games

brain-even:
	uv run python -m brain_games.scripts.brain_even
build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games