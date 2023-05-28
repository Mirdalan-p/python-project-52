lint:
	poetry run flake8 task_manager

start:
	python3 manage.py runserver

migrations:
	python3 manage.py makemigrations
	python3 manage.py migrate