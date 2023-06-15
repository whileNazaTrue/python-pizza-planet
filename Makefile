create-venv-windows:
	python3 -m venv venv
	cd venv/Scripts && activate.bat && cd ../..

create-venv:
	python3 -m venv venv
	source venv/bin/activate

install-app-dependencies:
	pip install -r requirements.txt

make start-app:
	python3 manage.py run

run-linters:
	tba

run-tests:
	python3 manage.py test

run-seed:
	python3 manage.py seed

start-database:
	python3 manage.py db init
	python3 manage.py db migrate
	python3 manage.py db upgrade

drop-database:
	python3 manage.py dbdrop
	python3 manage.py db migrate
	python3 manage.py db upgrade
