# test_vehicle
Vehicle System

# To run locally

First thing we need to do is create a folder:

```
$ mkdir car_system
```

### Start your virtual environment

Create a Python 3.5 virtualenv

```
car_system $ virtualenv venv
```

And then activate the environment:

```
car_system $ source venv/bin/activate
```

### Install the project dependencies

```
(venv) car_system $ pip install -r requirements.txt
```
### Config database 
  create a postgres db and add the credentials to settings.py
  ```
    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': 'db_name',
          'USER': 'user_server',
          'PASSWORD': 'password_server',
          'HOST': 'host',
          'PORT': port
      }
  ```
 
  Migrate database
  ```
  python manage.py migrate
  ```
 
  Create admin account
   ```
  python manage.py createsuperuser
   ```

  Makemigrations for the app
  ```
  python manage.py makemigrations 
  ```

  Again run migrate
   ```
  python manage.py migrate
   ```
   
### Start the development server
  ```
  python manage.py runserver
  ```


Now just head to your favorite web browser and visit
[http://127.0.0.1:8000](http://127.0.0.1:8000)
