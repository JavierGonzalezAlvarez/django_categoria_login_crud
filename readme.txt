
Instalar Python 3.7.4 en local
Instalar Django 2.2.7 en entorno virtual

Comandos en windows

Instalar entorno virtual
>pip3 install pipenv

Activar entorno virtual
>pipenv shell

Instalar Django
>pipenv install Django==2.2.7

Instalar conexión postgresql
>pipenv install psycopg2

Hacer migraciones de tablas de la BBDD
>python manage.py makemigrations
>python mange.py migrate

Crear usuario administrador
>python manage.py createsuperuser

Ejecutar el  servidor
>python manage.py runserver
http://127.0.0.1:8000/

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


