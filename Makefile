.PHONY: install vector-db test run lint

install:
	pip install -r requirements.txt

vectors:
	python src/chatbot/vector_store.py

test:
	pytest src/tests

run:
	python -m chatbot.cli

lint:
	flake8 src/
