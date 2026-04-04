install:
	uv sync

brain-games:
	uv run brain-games

brain-even:
	uv run python -m brain_games.scripts.brain_even

brain-calc:
	uv run python -m brain_games.scripts.brain_calc

brain-gcd:
	uv run python -m brain_games.scripts.brain_gcd

brain-arithm:
	uv run python -m brain_games.scripts.brain_progression

brain-prime:
	uv run python -m brain_games.scripts.brain_prime

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check --fix brain_games

full-build:
	uv sync
	uv run ruff check --fix brain_games
	uv build
	uv tool install dist/*.whl