1.- Create the Project and the respective Application:

Check the installed Django version:

python -m django --version

If you don't have Django installed, you can do so with the following command:

pip install Django

Create the project:

django-admin startproject project_name
cd project_name

Create the application inside the project:

python manage.py startapp app_name

2.- Add Applications to the Project:

In the 'settings.py' file, in the 'INSTALLED_APPS' list, add the created application:

INSTALLED_APPS = [    'django.contrib.admin',    'django.contrib.auth',    'django.contrib.contenttypes',    'django.contrib.sessions',    'django.contrib.messages',    'django.contrib.staticfiles',    'app_name',]

3._ Configure the PostgreSQL Database:

Install the PostgreSQL driver:

pip install psycopg2

In the settings.py file, configure the database connection:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database_name',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

4.- Modify the models.py file with the respective data:

In the application's models.py file, define the models and necessary fields:

from django.db import models

class Comite(models.Model):
    id_comite = models.AutoField(primary_key=True)
    fecha_requerimiento = models.DateTimeField(null=True)
    paso_produccion = models.CharField(max_length=255, null=True)
    numero_requerimiento = models.CharField(max_length=255, null=True)
    estado_flujo_req = models.CharField(max_length=255, null=True)
    # Add the remaining fields of the model

    def __str__(self):
        return str(self.id_comite)

5.- Create the Model Structure in the Database:

Run the following commands:

python manage.py makemigrations
python manage.py migrate

6.- Add the Model to the Admin Interface:

In the admin.py file, register the model to appear in the admin interface:

from django.contrib import admin
from .models import Comite

admin.site.register(Comite)

6.- Create the Administration Superuser:

Create a superuser to access the admin interface:

python manage.py createsuperuser

7.- Change the Language and Timezone:

In the settings.py file, set the language and timezone:

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

8.- Run the Application and Access it:

Start the development server:

python manage.py runserver

Access the admin interface in the browser:

http://127.0.0.1:8000/admin
