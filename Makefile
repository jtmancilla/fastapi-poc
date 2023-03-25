run:
	uvicorn main:app --reload

open_docs:
	open http://0.0.0.0:8000/docs

open_redoc:
	open http://0.0.0.0:8000/redoc

run-docker:
	docker compose up