
Instalar Python 3.7.4 en local
Instalar Django 2.2.7 en entorno virtual

Comandos en windows
>pip3 install pipenv
>pipenv shell
>pipenv install Django==2.2.7
>pipenv install psycopg2
>python manage.py makemigrations
>python mange.py migrate
>python manage.py createsuperuser
Usuario Cerado
user: admin
pss: admin

>python manage.py runserver


Con la BBDD Postgresql:
-Instalar postgresql
-Crear una base de datos configurando los parametros de conexion en local

config/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nombre de la base de la datos',
        'USER': 'nombre de usuario',
        'PASSWORD': 'contraseña de la base de datos',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}


