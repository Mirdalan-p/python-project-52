lint:
	poetry run flake8 task_manager

start:
	python3 manage.py runserver

migrations:
	python3 manage.py makemigrations
	python3 manage.py migrate

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage report -m --include=task_manager/* --omit=task_manager/settings.py
	poetry run coverage xml --include=task_manager/* --omit=task_manager/settings.py
