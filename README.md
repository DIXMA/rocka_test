# Rocka Test Project_ Movies App

## Description:
This is the project that is developed for the solution of the test as fullstack developer for the company Rocka.

> #### Technical specifications:
>Language: Python 3.7.1
>
>Framework: Django 2.2.1
>
>Database: SQLite3

##Install it

Clone the [github repository](https://github.com/DIXMA/rocka_test.git): 

```
git clone https://github.com/DIXMA/rocka_test.git
```

Create the virtual environment with python 3.7 or greater than 3.6:
> ####Note: 
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

##Description of the development
>
>
>