# Rocka Test Project_ Movies App

## Description:
This is the project that is developed for the solution of the test as fullstack developer for the company Rocka.

> #### Technical specifications:
>Language: Python 3.7.1
>
>Framework: Django 2.2.1
>
>Database: SQLite3

## Install it

Clone the [github repository](https://github.com/DIXMA/rocka_test.git): 

```
git clone https://github.com/DIXMA/rocka_test.git
```

Create the virtual environment with python 3.7 or greater than 3.6:
> #### Note: 
> I use virtualenvwrapper but if it is your preference you can use virtualenv normally.
```
mkvirtualenv --python=python3 rocka_test
```

With the virtual environment activated, we enter in the project directory:
```
(rocka_test)user$: cd /rocka_test
```

Install the libraries required for the project:
```
(rocka_test)user$: pip install -r requeriments.txt
```

Adjust settings file:
```
(rocka_test)user$: cat backend/settings-dist.py > backend/settings.py
```

Add the moviesApp application to the INSTALLED_APPS list in the settings.py file:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'moviesApp',
]
```

Execute migrations:
```
(rocka_test)user$: python manage.py makemigrations
(rocka_test)user$: python manage.py migrate
```

Start the server:
```
(rocka_test)user$: python manage.py runserver
```

Normally the server must be loaded in port 8000, you can enter the navigator with the url: http://127.0.0.1:8000/

## Description of the development
> To solve the problem of data loading of the file, first make a prerogative verifying that it has not been before. If the preload has not been performed, it starts reading the json file and uploading the data in the models and then saving it in the database. This process is done only once, and it is taken into account that data is not repeated.
> 
> For the design of the models, create a relationship entity structure, taking advantage of Django's ManToMay property, to model relations of this type.
>
> You can check all the movies that are registered.
>
> You can check the movies by genre, clicking on a desired genre in the list of movies.
>
> You can check the films by actor, clicking on the name of the actor in the list of films.
>
> You can see details of a movie by clicking on the button More details of the movie. In the detail of the film you can see similar movies, which contain similar genres, similar actors and the rating.