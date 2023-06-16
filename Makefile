create-venv-windows:
	python3 -m venv venv
	cd venv/Scripts && activate.bat && cd ../..

create-venv:
	python3 -m venv venv
	source venv/bin/activate

start-venv:
	cd venv/Scripts && Activate && cd ../..


install-app-dependencies:
	pip install -r requirements.txt

make start-app:
	python3 manage.py run

run-linters:
	ruff check . --fix

run-tests:
	python3 manage.py test

run-seed:
	python3 manage.py seed

update-requirements:
	pip3 freeze > requirements.txt

start-database:
	python3 manage.py db init
	python3 manage.py db migrate
	python3 manage.py db upgrade

drop-database:
	python3 manage.py dbdrop
<<<<<<< HEAD
	python3 manage.py db init
=======
	python3 manage.py db migrate
	python3 manage.py db upgrade
>>>>>>> d849ca8c4c20e72941ffca6543f8e3d545cb3193
