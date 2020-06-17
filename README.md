[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/gannebamm/agrihub)

# Installation (Dev / demo)

_Since installing Python and the creation of virtual environments are plattform
dependent they are not written as bash/powershell/cmd commands. Please refer
to the corresponding installation guidelines for your plattform._ 

## Python and virtual env

* install python3(.8) and virtualenv
* create a virtual environment (venv)
* activate the venv
* clone the repository (https://git-dmz.thuenen.de/nfdi4agri/agrihub.git)
* navigate to project root and install needed packages `pip install -r requirements.txt`

## Start Django application

See if the migration graph is complete:

``python ./manage.py makemigrations``

Apply migrations to the database:

``python ./manage.py migrate``

Create a superuser for the Django / Wagtail admin:

``python ./manage.py createsuperuser``

you will be prompted for a username and password.

Start the python development server:

``python ./manage.py runserver``