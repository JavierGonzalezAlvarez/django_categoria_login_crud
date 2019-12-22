from django.db import models

#Importamos la Clase de la App "Bases"
from apps.bases.models import ClaseModelo
# Create your models here.

#Hereda de ClaseModelo, y ya tiene todas las propiedades de ClaseModelo
class Categoria(ClaseModelo):
    #El id es serial, no nos ocupamos de este campo
    #Sólo usamos la descripción
    descripcion = models.CharField(
        max_length=100, 
        help_text="Descripciónde la categoría",
        unique=True
        )
    
    #Cuando hagamos referencia al modelo Categoria, Django va a poner un
    #valor hexadecimos por defecto, para transformarlo usamos STR de un campo
    #Todos lo metodos siempre reciebn algo, sino se usa self
    def __str__ (self):
        return '{}'.format(self.descripcion)
    #Para que la descripcion esté en mayusculas
    def save(self):
        self.descripcion = self.descripcion.upper()
        #Para guardar este self.description llamo al metodo save de la clase padre
        #Invocamos al Padre con Super, ¿qué invocamos? => el metodo save
        super(Categoria, self).save

    #Django añade una "s" a las tablas, para que nos ea así, desde Meta lo modificamos
    class Meta:
        #Cuando se refiera en plural
        verbose_name_plural = "Categorias"
