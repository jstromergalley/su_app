# INSTALLATION

## Via Docker:

1) ensure that docker is insalled and configured : __https://docs.docker.com/get-docker/__
2) clone or download the project from github
3) navigate to the root of the git project folder (the one with the Dockerfile in it)
4) build the docker image : __docker build --tag jonsg .__
5) run a container based on the image : __docker run -d --publish 8080:8080 --name jonsg jonsg__
6) visit the website at : __http://localhost:8080/__

### Demo User Account:
* demo/letmeinletmein

### Demo Admin Account:
* admin/letmein

## Via host:

1) ensure that python is installed and available (tested with 3.8)
2) clone or download the project from github
3) navigate to the root of the git project folder (the one with the Dockerfile in it)
4) create a virtual environment : __python -m venv .venv__
5) activate the environment: __.venv/Scripts/activate__
6) install the requirements : __python -m pip install django django-tables2__
7) start the webserver : __python ./project_music/manage.py runserver 0.0.0.0:8080__ (or an alternate port if 8080 is in use)
8) If prompted allow the firewall exception (probably windows only)
9) visit the website at : __http://localhost:8080/__

### Demo User Account:
* demo / letmeinletmein

### Demo Admin Account:
* admin / letmein

## Observations

This was my first use of "Django". I selected it as I know that the iSchool makes extensive use of python and becuase I had heard that it has some good scaffolding for creating boiler plate sites like this one.

### Pros
* out of the box boiler plating was indeed useful
* integrated site auth though basic was a big help
* the tables library provided all requested UI functionality
* scaffold admin back end was helpful during dev and I left it in to manages users and libraries

### Cons
* as with all scaffolding, doing tasks that the scaffold anticipated was easy, other tasks not so much
* the framework has less documentation than I anticipated

### Recomendations

This task does not seem to align with what I belive are the requirments or needs of the iSchool, at least as far as my work with CCDS goes. I believe a task to create or manage simple workflows in Airflow, a simple ML task, or even simple implementation of non-ui based mongodb pipepline would be a better match for future candidates.
