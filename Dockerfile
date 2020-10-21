FROM python:3.8

ENV FLASK_DEBUG=1
ENV SECRET_KEY=letmein
ENV ADMIN_USERNAME=admin
ENV ADMIN_PASSWORD=change_on_install
ENV WEB_SERVER_PORT=9001
ENV SQLALCHEMY_DATABASE_URI=sqlite:///database/database.sqlite
ENV SQLALCHEMY_TRACK_MODIFICATIONS=False

## ---------------------------
## Bring the platform uptodate
## ---------------------------
RUN apt-get update && apt-get upgrade -y
RUN python -m pip install --upgrade pip
RUN python -m pip install setuptools --upgrade setuptools
## ---------------------------

## ---------------------------
## Install Dependencies
## ---------------------------
RUN python -m pip install django django-tables2
## ---------------------------

EXPOSE 8080

VOLUME /var/webapp/
COPY . /var/webapp/
WORKDIR /var/webapp/project_music/

## ---------------------------
# Run Site
## ---------------------------
CMD /usr/local/bin/python ./manage.py runserver 0.0.0.0:8080
## ---------------------------
