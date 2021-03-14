# NewsBoard

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [API](#api)

## General info
This project for posting your articles with the ability to comment and vote for the article. There is also an API for site management.
	
## Technologies
Project is created with:
* Python 3.8
* Django 3.1
* Django-rest-framework
* Bootstrap 4
* Docker
* PostgreSQL
* Heroku
	
## Setup
To run this project, do this:

1) Clone project in your PC
```
$ git clone https://github.com/Grayder0152/NewsBoard.git
```
2) Go to the root directory of the project and install requirements:
```
$ pip install requirements.txt
```
3) There is no database on your local machine. First, configure access to the [PostgreSQL](https://djangocentral.com/using-postgresql-with-django/) or use deffault [SQLite](https://docs.djangoproject.com/en/3.1/ref/settings/#databases) database. You need to change dictionary *`DATABASES`* in file `settings.py`
4) Then you have to make migrations
```
$ python manage.py makemigrations
$ python manage.py migrate
```
5) Finally, run the server
```
$ python manage.py runserver
```
## API
The CRUD API interface is implemented on the site. You can see its documentation [here](https://documenter.getpostman.com/view/14942069/Tz5qawy3)
