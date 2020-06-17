[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/gannebamm/agrihub/tree/gannebamm/gitpod-setup)

# Installation obsolete

_Since we are using gitpod ther is nothing to install_

## Python and virtual env not needed

* gitpod uses python 3.8 outside a virtual env (since it is a docker container)

## The Django application allready runs

The console should show if the migration graph is complete:

``python ./manage.py makemigrations``

And that migrations were applied to the database:

``python ./manage.py migrate``

Also a superuser for the Django / Wagtail admin was created:

``python ./manage.py createsuperuser``

the username is `admin` and the password is `changeme`. 
 
A python dev server was started at port 8000:

``python ./manage.py runserver 0.0.0.0:8000``

# straight to the funsies

Your browser should have opened a tab. Please login at `https://your-container-id.gitpod.io/admin`

There you have to:

* delete the old root page
* create a new root page which is a translatable page
* go to setting and define the new root as default site
* add english as second language
* create a subpage of the root as welcome page (ger / eng)
* create additional subpages with content