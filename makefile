

run:
	docker compose up --build


run_daemon:
	docker compose up --build -d


test:
	docker exec enid_bot poetry run pytest -s
