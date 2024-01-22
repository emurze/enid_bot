

run:
	docker compose up --build

test:
	docker exec enid_bot poetry run pytest -s
