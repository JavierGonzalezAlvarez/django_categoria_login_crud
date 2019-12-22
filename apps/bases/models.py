from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    #Quiero que se ponga la fecha en el momento que se cree
    fc = models.DateTimeField(auto_now_add=True)
    #Quiero que se modifique cunado se cambie algo
    fm = models.DateTimeField(auto_now=True)
    #Quiero heredar los valroes de la clase de User de Django
    #Coloco => from django.contrib.auths.models import User
    #Relacion => 1 a muchos
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    #El usuario modifica no puedo poner otra relacion ForeingKey
    #Creamos un campo de tipo entero. Permitimos valor nulos y vacios
    um = models.IntegerField(null=True, blank=True)
    #Le decimos a Django que este modelo no lo debe tener en
    #  cuenta a la hora de hacer una migracion. Se usa la Clase Meta con abstract=True
    #La clase Meta sirve para muchas cosas como, por ejemplo, 
    # para definir los permisos habilitados, la base de datos asociada, 
    # el nombre de la tabla, el nombre en singular o plural que se va a ver en el admin de Django.
    class Meta():
        abstract=True

