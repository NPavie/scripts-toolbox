# Environnement d'exécution
if [ ! -d "flask" ]
then
	python3 -m venv flask

	flask/bin/pip install wheel
	flask/bin/pip install flask
	flask/bin/pip install flask-login
	flask/bin/pip install flask-mail
	flask/bin/pip install flask-sqlalchemy
	flask/bin/pip install sqlalchemy-migrate
	flask/bin/pip install flask-whooshalchemy
	flask/bin/pip install flask-wtf

fi

# fichier de configuration par défaut
if [ ! -e "config.py" ]
then
	echo "WTF_CSRF_ENABLED = True" > "config.py"
	echo "SECRET_KEY = 'to-replace'" >> "config.py"
fi

# base du projet
if [ ! -d "app" ]
then
	# Arborescence du module app
	mkdir app
	mkdir app/assets
	mkdir app/assets/css
	mkdir app/assets/js

	mkdir app/templates

	mkdir tmp

	# fichier d'initialisation du module "app"
	echo "from flask import Flask" > "app/__init__.py"
	echo "app = Flask(__name__)" >> "app/__init__.py"
	echo "app.config.from_object('config')" >> "app/__init__.py"
	echo "from app import views" >> "app/__init__.py"

	#
	echo "from app import app" > "app/views.py"

fi

if [ ! -e "run.py" ]
then # runner scripts
	echo "from app import app" > "run.py"
	echo "app.run(debug=True)" >> "run.py"
fi

# launching the runner script from virtual env
echo "flask/bin/python run.py" > "launch_app.sh"
chmod +x "launch_app.sh"