run:
	@python -m strava2notion.main

mypy:
	@python -m mypy strava2notion

check:
	@python -m ruff check strava2notion

format:
	@python -m ruff format strava2notion
