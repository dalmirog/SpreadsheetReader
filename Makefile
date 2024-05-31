.PHONY: check_dependencies run

check_dependencies:
	pip3 install --no-cache-dir -r requirements.txt

run: check_dependencies
	python3 run.py
start_local_environment:
	docker-compose up