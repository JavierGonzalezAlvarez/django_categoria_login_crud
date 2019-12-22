from django.shortcuts import render

#Para que si un suario está logeado.
from django.contrib.auth.mixins import LoginRequiredMixin

#Importo las vistas genericas
from django.views import generic

#Bebe sacar los datos del modelo que necesitamos
from .models import Categoria

# Create your views here.
#Creamos una clase con el mixin que tenemos y las vistas genericas de Django
class class_CategoriaView(LoginRequiredMixin, generic.ListView):
    #Esta vista debe tener unas catecteristicas a cumplir
    #Asignamos el modelo
    model = Categoria
    template_name = "inv/html_categoria_list.html"
    #Importante, el contexto es la variable que le va a pasar a la vista con
    # la informacion que va a renderizar a la plantilla. A la plantilla le dijimos
    # que se va a llamar obj, por defecto Dajgno le llama object, pero nosotros cambiamos 
    # el nombre con context_object_name
    context_object_name = "obj"
    #Si no estamos logeados, que nos pida logearnos
    login_url = "bases/login"
    




