.PHONY: build run down migrate db

exec:
	@docker compose run --rm --entrypoint /bin/bash build_src

build:
	@docker compose build build_src --no-cache

run:
	@docker compose up -d api

db:
	@docker compose up -d db

test: db
	@docker compose run --rm build_src tests

#poetry commands
lock:
	@docker compose run --rm build_src poetry lock
	@docker compose build build_src

# migrations
migration:
	echo "creating new migration..."
	@docker compose run --rm build_src makemigration "$(name)"

migrate:
	@docker compose run --rm build_src migrate "$(name)"

downgrade:
	@docker compose run --rm build_src downgrade "$(name)"

su:
	@docker compose run --rm build_src createsuperuser "$(login)"

lint:
	@docker compose run --rm build_src analyze

format:
	@docker compose run --rm build_src format

mypy:
	@docker compose run --rm build_src mypy svc tests

down:
	@docker compose down

clean:
	@docker compose down -v --remove-orphans --rmi local
