.PHONY: setup run migrations createadmin

migrations:
	python apitft/manage.py makemigrations
	python apitft/manage.py migrate tisfittracker

createadmin:
	python apitft/manage.py createsuperuser --username=admin --email=admin@tft.com --noinput
	python apitft/manage.py shell < utils/superuser.py

setup:
	python -m venv apitft/venv
	. apitft/venv/bin/activate
	pip install -r apitft/requirements.txt
	make migrations
	make createadmin
	make import_perms

import_perms:
	python apitft/manage.py shell < utils/import_db.py

run:
	python apitft/manage.py runserver
